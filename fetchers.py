import os
import requests


def get_weather():
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        return "Weather unavailable"

    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "q": "Bathurst,CA",
                "appid": api_key,
                "units": "metric",
            },
            timeout=10,
        )

        if response.status_code != 200:
            return "Weather unavailable"

        data = response.json()
        main = data.get("main") or {}
        weather_list = data.get("weather") or []

        temp = main.get("temp")
        description = (
            weather_list[0].get("description") if weather_list and isinstance(
                weather_list[0], dict) else None
        )

        if temp is None or not description:
            return "Weather unavailable"

        temp_rounded = int(round(float(temp)))
        description_text = str(description).lower()

        return f"{temp_rounded}°C, {description_text} in Bathurst"
    except Exception:
        return "Weather unavailable"


def get_quote():
    return "Quote not implemented yet."
