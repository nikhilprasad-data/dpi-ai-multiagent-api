# loading .env variables

from dotenv import load_dotenv
load_dotenv()

import os

# for chatbot

GROQ_API_KEY=os.environ.get("GROQ_API_KEY","")    

CHAT_LLM=os.environ.get("CHAT_LLM","llama-3.3-70b-versatile")