# load GROQ_API_KEY, CHAT_LLM

from src.config import GROQ_API_KEY, CHAT_LLM

# langchain

from langchain_groq import ChatGroq

# history

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# prompts

from src.prompts import system_message as sys_prompt_text

chat_llm = ChatGroq(
     model= CHAT_LLM,
     max_tokens= 1024,
     temperature= 0.8
)

# history = []

system_message = SystemMessage(
     content= sys_prompt_text
)

# history.append(system_message)

# for terminal 

# def test_chat():

#      while True:
#           user_input = input('User: ')
#           if user_input == '0':
#                break

#           history.append(HumanMessage(content= user_input))

#           response = chat_llm.invoke(history)

#           history.append(AIMessage(content= response.content))

#           print('AI: ', response.content)
     
# for routes 

def get_ai_response(user_request: str, chat_history: list):

     messages_to_send: list = [SystemMessage(content= sys_prompt_text)]

     for msg in chat_history:
          if msg['role'] == 'user':
               messages_to_send.append(HumanMessage(content= msg['content']))
          
          elif msg['role'] == 'ai':
               messages_to_send.append(AIMessage(content= msg['content']))

     messages_to_send.append(HumanMessage(content= user_request))

     stream = chat_llm.stream(messages_to_send)

     full_response = ""

     for chunk in stream:
          token = str(chunk.content)

          full_response += token

          yield token

