from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
from header_config import headers

class WebScraper:
    """Class that is used to scrape a website by its url"""
        
    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=headers, timeout=10000)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)


ed = WebScraper("https://edwarddonner.com")
print(ed.title)
print(ed.text)