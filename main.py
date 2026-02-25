from fetchers import get_weather, get_quote
from formatter import build_summary
from output import save_summary


def main():
    # 1. Fetch data
    weather = get_weather()
    quote = get_quote()

    # 2. Build summary text
    summary_text = build_summary(weather, quote)

    # 3. Save summary
    save_summary(summary_text)


if __name__ == "__main__":
    main()
