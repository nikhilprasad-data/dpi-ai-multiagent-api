# loading .env variables

from dotenv import load_dotenv
load_dotenv()

import os

class Config:
     
     """Project Configuration and Environment Variables"""

    # for search llm
     GROQ_API_KEY=os.environ.get("GROQ_API_KEY","")    

     SEARCH_LLM=os.environ.get("SEARCH_LLM","llama-3.3-70b-versatile")


     # for reader llm 

     GOOGLE_API_KEY=os.environ.get("GOOGLE_API_KEY","")

     READER_LLM=os.environ.get("READER_LLM","gemini-2.5-flash")

     # for Tavily

     TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY","")
 