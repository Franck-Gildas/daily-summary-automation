import os
import smtplib
from email.mime.text import MIMEText


def send_email(subject, body):
    sender = os.getenv("DAILY_SUMMARY_EMAIL_FROM")
    recipient = os.getenv("DAILY_SUMMARY_EMAIL_TO")
    password = os.getenv("DAILY_SUMMARY_EMAIL_PASSWORD")
    smtp_server = os.getenv("DAILY_SUMMARY_EMAIL_SMTP")
    smtp_port = int(os.getenv("DAILY_SUMMARY_EMAIL_PORT", "587"))

    if not all([sender, recipient, password, smtp_server]):
        return "Email configuration missing."

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
        return "Email sent successfully."
    except Exception as e:
        return f"Email error: {e}"
