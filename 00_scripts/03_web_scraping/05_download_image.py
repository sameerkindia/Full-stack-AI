import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

BASE_URL = 'https://books.toscrape.com/'
IMAGE_DIR = 'images'

def sanitize_filename(title):
    return re.sub(r'[^\W\-_. ]', '', title).replace(" ", " _")

def download_image(img_url, filename):
    try:
        response = requests.get(img_url, stream=True, timeout=10)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
    except Exception as e:
        print(f"Failed to download {filename} - {e}")
    