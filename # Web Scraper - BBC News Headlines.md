# Web Scraper - BBC News Headlines

This Python script scrapes the latest headlines from the BBC News website and saves them into a text file.

## 📌 What It Does
- Sends GET request to BBC News homepage
- Extracts headlines from `<h2>` tags using BeautifulSoup
- Stores cleaned headlines in `headlines.txt`

## 🛠 Requirements
Install required libraries:

```bash
pip install requests beautifulsoup4
How to Run
python scraper.py
Output

Creates a file:

headlines.txt


Containing lines like:

US election latest updates
Global markets rise...
Tech firms face new regulations