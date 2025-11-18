import requests
from bs4 import BeautifulSoup

# Step 1: Website URL
url = "https://www.bbc.com/news"

# Step 2: Fetch HTML
response = requests.get(url)
html_content = response.text

# Step 3: Parse using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Step 4: Find headlines (usually h2 tags)
headlines = soup.find_all("h2")

# Step 5: Store headlines in a list
news_list = []
for h in headlines:
    text = h.get_text(strip=True)
    if text:  # Avoid empty strings
        news_list.append(text)

# Step 6: Save to file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for line in news_list:
        file.write(line + "\n")

print("Headlines scraped and saved to headlines.txt")
