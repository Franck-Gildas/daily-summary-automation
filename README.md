---

Daily Summary Automation
A Python-based automation system that generates a personalized daily summary—including weather, a quote of the day, and a timestamp—then delivers it as a clean HTML email. The summary is also saved locally and can be scheduled to run automatically using Windows Task Scheduler.
This project demonstrates end to end automation: API integration, formatting, environment based configuration, email delivery, and OS level scheduling.

---

Features
• Weather integration using a public API
• Quote of the day fetched dynamically
• Timezone aware timestamping
• Config driven architecture (config.json)
• HTML and plain text email support
• Environment variable based credentials
• Local file output (daily_summary.txt)
• Windows Task Scheduler automation
• Modular, production ready code structure

---

Project Structure
daily-summary-automation/
│
├── main.py
├── formatter.py
├── fetchers.py
├── emailer.py
├── output.py
├── config.py
├── config.json
├── requirements.txt
├── .env.example
└── README.md
Each component has a clear responsibility:
• fetchers.py — retrieves weather and quote data
• formatter.py — builds plain text and HTML summaries
• emailer.py — sends multipart emails (text + HTML)
• output.py — saves the summary locally
• main.py — orchestrates the workflow
• config.json — user editable settings
• .env — secure email credentials (not committed)

---

Installation

1. Clone the repository
   git clone https://github.com/YOUR_USERNAME/daily-summary-automation.git
   cd daily-summary-automation
2. Create a virtual environment
   python -m venv venv
   source venv/bin/activate # macOS/Linux
   venv\Scripts\activate # Windows
3. Install dependencies
   pip install -r requirements.txt

---

Configuration

1. Environment variables
   Copy .env.example to .env:
   cp .env.example .env
   Fill in your email credentials:
   DAILY_SUMMARY_EMAIL_FROM=your_email@example.com
   DAILY_SUMMARY_EMAIL_TO=recipient@example.com
   DAILY_SUMMARY_EMAIL_PASSWORD=your_app_password
   DAILY_SUMMARY_EMAIL_SMTP=smtp.yourprovider.com
   DAILY_SUMMARY_EMAIL_PORT=587
2. Edit config.json
   {
   "location": {
   "city": "Bathurst",
   "country": "CA"
   },
   "output_file": "daily_summary.txt",
   "timezone": "America/Moncton",
   "time_format": "%Y-%m-%d %H:%M %Z",
   "features": {
   "weather": true,
   "quote": true,
   "email": true
   },
   "email_subject": "Your Daily Summary",
   "email_format": "html"
   }

---

Running the Script
Run manually:
python main.py
You should receive:
• A new daily_summary.txt file
• An HTML formatted email in your inbox

---

Automating with Windows Task Scheduler

1. Open Task Scheduler
2. Create a Basic Task
3. Choose your schedule (e.g., daily at 7:00 AM)
4. Action → Start a program
5. Program/script:
6. python
7. Add arguments:
8. C:\path\to\your\project\main.py
9. Conditions → enable:
   o Wake the computer to run this task
10. Power Options → enable:
    o Allow wake timers
    Your daily summary will now run automatically.

---

Example Output (HTML Email)
(Insert a screenshot of your formatted email here)
This visual element dramatically improves the professionalism of your GitHub repo.

---

Why This Project Matters
This automation demonstrates:
• API consumption
• Modular Python design
• HTML email generation
• Secure credential handling
• OS level automation
• Real world usefulness
It’s the kind of project employers and clients immediately understand and value.

---

License
MIT License — free to use, modify, and distribute.

---
