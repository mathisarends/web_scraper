# **Web Scraper mit OpenAI-Integration**

Dieses Projekt kombiniert **Web Scraping** mit der **OpenAI API**, um dynamische Webseiten zu analysieren und Inhalte automatisch zusammenzufassen. Ziel ist es, Texte von JavaScript-lastigen Webseiten (SPAs) zu extrahieren und mithilfe eines LLMs (Large Language Model) eine kompakte Zusammenfassung zu erstellen.

---

## **Funktionen**

1. **Web Scraping**:

   - Webseiten mit **JavaScript-generierten Inhalten** werden vollständig gerendert.
   - Verwendung von **Playwright** oder **Selenium** zur Browsersteuerung und HTML-Extraktion.

2. **Zusammenfassung mit OpenAI**:
   - Der extrahierte Text wird an die **OpenAI API** gesendet (z. B. GPT-4).
   - Das Modell erstellt automatisch eine kompakte und verständliche Zusammenfassung der Seite.

---

## **Verwendete Technologien**

- **Python 3.9+**
- [Playwright](https://playwright.dev/python/): Browser-Automatisierung zur Ausführung von JavaScript.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): HTML-Parsing und Textverarbeitung.
- [OpenAI API](https://platform.openai.com/): KI-Modelle für Textzusammenfassungen.
- [Python-Dotenv](https://pypi.org/project/python-dotenv/): Verwaltung von Umgebungsvariablen.

---

## **Projektstruktur**

```plaintext
web_scraper/
│-- .venv/                  # Virtuelle Python-Umgebung
│-- .env                    # OpenAI API-Schlüssel (nicht im Repository speichern!)
│-- header_config.py        # Enthält Header-Informationen für Anfragen
│-- llm_summarizer.py       # Hauptmodul zur Verwendung der OpenAI API
│-- web_scraper.py          # Modul für das Scrapen von Webseiten
│-- requirements.txt        # Abhängigkeiten des Projekts
│-- README.md               # Projektbeschreibung
└-- __pycache__/            # Python-Cache-Dateien
```
