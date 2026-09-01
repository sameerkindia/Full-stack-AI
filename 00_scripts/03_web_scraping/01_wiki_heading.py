import requests
from bs4 import BeautifulSoup
import os

# URL = "https://en.wikipedia.org/wiki/Marvel_Cinematic_Universe"
# URL = "https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing"
URL = "https://www.scrapingbee.com/blog/scraper-sites"

FILE_NAME = '01_scrap_file.txt'

# if not os.path.exists(FILE_NAME):
#     with open(FILE_NAME, 'w', encoding='utf-8') as f:
#         print("File created")

def get_h2_header(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page: \n {e}")
        return []

    # print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")
    print(h2_tags)
    headers = []
    for tag in h2_tags:
        header_text = tag.get_text(strip=True)

    with open(FILE_NAME, 'w', newline='', encoding='utf-8') as f:
        f.write(str(h2_tags))


get_h2_header(URL)