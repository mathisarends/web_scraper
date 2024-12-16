from bs4 import BeautifulSoup
from header_config import headers
import requests
from playwright.sync_api import sync_playwright



class WebScraper:
    """Class that is used to scrape a website by its url"""
        
    def __init__(self, url):
        self.url = url
        
        with sync_playwright() as p:
            # Browser im headless-Modus starten
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Gehe zur Seite und warte auf Netzwerkaktivität
            page.goto(url, wait_until="networkidle")
            
            # Extrahiere den gesamten Seiteninhalt
            page_source = page.content()
            browser.close()
        
        soup = BeautifulSoup(page_source, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)
