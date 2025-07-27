import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import os
import signal
import time

# Global variable to hold subprocess
keylogger_process = None

# === Start the Keylogger ===
def start_keylogger():
    global keylogger_process
    if keylogger_process is None:
        try:
            keylogger_process = subprocess.Popen(
                ["python", "keylogger.py"], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
            )
            messagebox.showinfo("Keylogger", "Keylogger started.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start keylogger:\n{e}")
    else:
        messagebox.showwarning("Warning", "Keylogger is already running.")

# === Stop the Keylogger ===
def stop_keylogger():
    global keylogger_process
    if keylogger_process:
        try:
            os.kill(keylogger_process.pid, signal.CTRL_BREAK_EVENT)
            keylogger_process = None
            messagebox.showinfo("Keylogger", "Keylogger stopped.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stop keylogger:\n{e}")
    else:
        messagebox.showwarning("Warning", "Keylogger is not running.")

# === View the Log File ===
def view_log():
    log_file = "log.txt"
    if os.path.exists(log_file):
        with open(log_file, "r", encoding="utf-8") as f:
            content = f.read()
        log_window = tk.Toplevel(root)
        log_window.title("View Log File")
        log_text = scrolledtext.ScrolledText(log_window, width=80, height=25)
        log_text.pack(padx=10, pady=10)
        log_text.insert(tk.END, content)
        log_text.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("Log", "No log file found.")

# === GUI Setup ===
root = tk.Tk()
root.title("Keylogger GUI")
root.geometry("400x250")
root.resizable(False, False)

title = tk.Label(root, text="🛡️ Keylogger Controller", font=("Arial", 18, "bold"))
title.pack(pady=10)

start_btn = tk.Button(root, text="Start Keylogger", width=20, bg="green", fg="white", command=start_keylogger)
start_btn.pack(pady=10)

stop_btn = tk.Button(root, text="Stop Keylogger", width=20, bg="red", fg="white", command=stop_keylogger)
stop_btn.pack(pady=10)

view_btn = tk.Button(root, text="View Log File", width=20, command=view_log)
view_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", width=20, command=root.destroy)
exit_btn.pack(pady=10)

root.mainloop()
