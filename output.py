def save_summary(text):
    with open("daily_summary.txt", "w", encoding="utf-8") as f:
        f.write(text)