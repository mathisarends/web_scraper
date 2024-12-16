from dotenv import load_dotenv
import os
from openai import OpenAI
from web_scraper import WebScraper

load_dotenv()

class LLmSummarizer:
    """Class that is used to summarize websites via the openAI-API"""
        
    def __init__(self):
        self.openai = OpenAI()
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.system_prompt = "You are an assistant that analyzes the contents of a website \
                                and provides a short summary, ignoring text that might be navigation related. \
                                Respond in markdown."
                                
    def messages_for(self, website):
        """Generates messages for the OpenAI API"""
        return [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": self.user_prompt_for(website)}  
        ]
    
    def user_prompt_for(self, website):
        """Generates a user prompt based on the website content."""
        return f"Please summarize the following website content:\n\n{website.text}"
        
    def summarize(self, website_url):
        website = WebScraper(website_url)
        response = self.openai.chat.completions.create(
            model = "gpt-4o-mini",
            messages = self.messages_for(website)
        )
        return response.choices[0].message.content
        
llmSummarizer = LLmSummarizer()
summary = llmSummarizer.summarize(website_url = "https://edwarddonner.com")
print(summary)