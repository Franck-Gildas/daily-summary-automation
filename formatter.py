def build_summary(weather, quote, timestamp):
    return (
        f"📝 Daily Summary\n"
        f"📅 {timestamp}\n\n"
        f"🌤️ Weather\n"
        f"{weather}\n\n"
        f"💬 Quote of the Day\n"
        f"{quote}\n"
    )
