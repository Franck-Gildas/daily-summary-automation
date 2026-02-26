import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, body_text, body_html=None):
    sender = os.getenv("DAILY_SUMMARY_EMAIL_FROM")
    recipient = os.getenv("DAILY_SUMMARY_EMAIL_TO")
    password = os.getenv("DAILY_SUMMARY_EMAIL_PASSWORD")
    smtp_server = os.getenv("DAILY_SUMMARY_EMAIL_SMTP")
    smtp_port = int(os.getenv("DAILY_SUMMARY_EMAIL_PORT", "587"))

    if not all([sender, recipient, password, smtp_server]):
        return "Email configuration missing."

    if body_html is not None:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = recipient
        part_plain = MIMEText(body_text, "plain", "utf-8")
        part_html = MIMEText(body_html, "html", "utf-8")
        msg.attach(part_plain)
        msg.attach(part_html)
    else:
        msg = MIMEText(body_text, "plain", "utf-8")
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
