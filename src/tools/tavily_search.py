from langchain.tools import tool
import requests
from tavily import TavilyClient
import os
from src.config.settings import Config
from rich import print

# tavily init

tavily = TavilyClient(api_key= Config.TAVILY_API_KEY)

# tool

@tool
def tavily_search(query: str)-> str:
     """
     Search the web for accurate and up-to-date information.

     Invoke this tool whenever answering the user's request requires
     internet search, current events, recent updates, live information,
     official documentation, or facts beyond the model's knowledge.

     Args:
          query: A precise search query describing the information to retrieve.

     Returns:
          A list of the most relevant search results, including their URLs,
          titles, and content snippets.
     """

     out = []

     results = tavily.search(
          query= query,
          max_results= 4
     )

     for r in results['results']:
          out.append(
               f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
          )

     return "\n---\n".join(out)

# terminal

# print(tavily_search.invoke("What is the top news of Delhi"))
