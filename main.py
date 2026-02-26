from fetchers import get_weather, get_quote
from formatter import build_summary, build_html_summary
from output import save_summary
from emailer import send_email
from datetime import datetime

import zoneinfo
from config import load_config


def main():
    config = load_config()

    city = config["location"]["city"]
    country = config["location"]["country"]
    timezone = config["timezone"]
    time_format = config["time_format"]

    weather_enabled = config["features"]["weather"]
    quote_enabled = config["features"]["quote"]
    email_enabled = config["features"]["email"]

    email_subject = config["email_subject"]
    email_format = config.get("email_format", "text")

    # 1. Fetch data
    weather = get_weather() if weather_enabled else "Weather disabled"
    quote = get_quote() if quote_enabled else "Quote disabled"

    # 2. Get timestamp
    tz = zoneinfo.ZoneInfo(timezone)
    now = datetime.now(tz)
    timestamp = now.strftime(time_format)

    # 3. Build summary text
    summary_text = build_summary(weather, quote, timestamp)

    # 4. Save summary
    save_summary(summary_text)

    # 5. Send email (optional)
    if email_enabled:
        if email_format == "html":
            html_summary = build_html_summary(weather, quote, timestamp)
            email_status = send_email(email_subject, summary_text, html_summary)
        else:
            email_status = send_email(email_subject, summary_text)
        print(email_status)
    else:
        print("Email disabled")


if __name__ == "__main__":
    main()
