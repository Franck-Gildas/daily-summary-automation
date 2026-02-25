from fetchers import get_weather, get_quote
from formatter import build_summary
from output import save_summary
from datetime import datetime
import zoneinfo


def main():
    # 1. Fetch data
    weather = get_weather()
    quote = get_quote()

    # 2. Get timestamp
    tz = zoneinfo.ZoneInfo("America/Moncton")
    now = datetime.now(tz)
    timestamp = now.strftime("%Y-%m-%d %H:%M %Z")

    # 3. Build summary text
    summary_text = build_summary(weather, quote, timestamp)

    # 4. Save summary
    save_summary(summary_text)


if __name__ == "__main__":
    main()
