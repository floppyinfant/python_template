"""
LangChain
https://www.langchain.com/
https://python.langchain.com/docs/introduction/
https://github.com/langchain-ai/langchain

"""

from langchain.chat_models  import ChatOpenAI
import dotenv
import os

dotenv.load_dotenv
api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(openai_api_key=api_key, temperature=0)
result = chat_model.predict("Hello World!")
print(result)
