# Daily Summary Automation

A small Python automation that generates a daily summary including weather, quotes, and other optional data sources.

## Features

- Fetches daily data (weather, quotes, etc.)
- Formats a clean summary
- Saves it to a file

## Project Structure

- `main.py` — orchestrates the workflow
- `fetchers.py` — functions to fetch external data
- `formatter.py` — builds the summary text
- `output.py` — saves or emails the summary
