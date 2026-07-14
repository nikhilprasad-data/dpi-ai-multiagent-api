from bs4 import BeautifulSoup
from langchain.tools import tool
import requests
from rich import print

# tool

@tool
def url_scrapper(url: str)-> str:
     """
     Extract the primary content from a webpage.

     Use this tool to retrieve information from a specific URL after it
     has been identified. It is intended for reading webpage content,
     not for searching the web.

     Args:
          url: The webpage URL to scrape.

     Returns:
          The webpage title, metadata (if available), and the cleaned main
          textual content extracted from the page.
     """

     try:
          resp = requests.get(
               url,
               timeout=8,
               headers={"User-Agent": "Mozilla/5.0"}
          )

          soup = BeautifulSoup(resp.text, "html.parser")

          for tag in soup(["script", "style", "nav", "footer"]):
               tag.decompose()

          return soup.get_text(separator=" ", strip=True)[:3000]

     except Exception as e:
          return f"Could not scrape URL: {str(e)}"
     
# terminal

# print(url_scrapper.invoke(""))