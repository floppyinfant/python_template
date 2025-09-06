"""
https://github.com/ollama/ollama-python
https://github.com/ollama/ollama/blob/main/docs/api.md

pip install ollama
"""

from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='gemma3', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)
