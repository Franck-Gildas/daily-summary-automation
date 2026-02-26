def build_summary(weather, quote, timestamp):
    return (
        f"📝 Daily Summary\n"
        f"📅 {timestamp}\n\n"
        f"🌤️ Weather\n"
        f"{weather}\n\n"
        f"💬 Quote of the Day\n"
        f"{quote}\n"
    )


def build_html_summary(weather, quote, timestamp):
    return f"""
<html><body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
<h2 style="margin-bottom: 0;">Daily Summary</h2>
<p style="margin-top: 4px; color: #555;">📅 {timestamp}</p>
<h3 style="margin-bottom: 4px;">🌤️ Weather</h3>
<p>{weather}</p>
<h3 style="margin-bottom: 4px;">💬 Quote of the Day</h3>
<p>{quote}</p>
</body></html>
""".strip()
