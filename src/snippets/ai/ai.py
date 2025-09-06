"""
AI - Generative AI

@see Notebooks/Python_template.ipynb

---

self-hosted AI (run locally)
- Ollama
- HuggingFace Hub
- ComfyUI, CivitAI

LLM API
- OpenAI API
- Google Gemini API

Agentic AI
- LangChain

Diffusion Models
- Stable Diffusion, Flux
- Imagen, Nano Banana

Video Generation
- Wan
- Veo3, dreamseek
"""

# load environment variables from .env-file
import dotenv
dotenv.load_dotenv()

# ----------------------------------------------------------------------------

"""
Ollama

https://github.com/ollama/ollama
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

# ----------------------------------------------------------------------------

"""
HuggingFace Hub

https://github.com/huggingface
https://huggingface.co/docs

https://github.com/huggingface/huggingface_hub
https://huggingface.co/docs/huggingface_hub/index
https://github.com/huggingface/hub-docs/blob/main/docs/inference-providers/index.md

pip install huggingface_hub
hf auth login --token $HUGGINGFACE_TOKEN # get a read token from hf.co/settings/tokens
"""

from huggingface_hub import InferenceClient
from huggingface_hub import login  # alternative to CLI: 'hf auth login'
# login()                          # load_dotenv(); os.getenv("HUGGINGFACE_TOKEN")

client = InferenceClient()

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    messages=[
        {
            "role": "user",
            "content": "How many 'G's in 'huggingface'?"
        }
    ],
)

print(completion.choices[0].message)

# ----------------------------------------------------------------------------

"""
OpenAI REST API

https://platform.openai.com/docs/api-reference/introduction
https://github.com/openai/openai-python/blob/main/api.md
https://platform.openai.com/docs/api-reference/responses

# get OpenAI API key:
https://platform.openai.com/settings/organization/api-keys

pip install openai
"""

import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.responses.create(
    model="gpt-4o",
    instructions="You are a coding assistant that talks like a pirate.",
    input="How do I check if a Python object is an instance of a class?",
)

print(response.output_text)

# ----------------------------------------------------------------------------

"""
Google Gemini

https://ai.google.dev/gemini-api/docs?hl=de
https://medium.com/google-cloud/model-context-protocol-mcp-with-google-gemini-llm-a-deep-dive-full-code-ea16e3fac9a3

pip install google-genai mcp
"""

import os

from google import genai
from google.genai import types
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

client = genai.Client()
#client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)

# ----------------------------------------------------------------------------

"""
LangChain
https://www.langchain.com/
https://python.langchain.com/docs/introduction/
https://github.com/langchain-ai/langchain

LangGraph - Gemini Agent Quickstart
https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart
"""

from langchain_openai  import ChatOpenAI
#import dotenv
import os

#dotenv.load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY ist nicht gesetzt.")

chat_model = ChatOpenAI(api_key=api_key, temperature=0)
result = chat_model.invoke("Hello World!")
print(result.content)

# ----------------------------------------------------------------------------

"""
PyTorch
https://pytorch.org/
https://pytorch.org/get-started/locally/
https://github.com/pytorch/pytorch
https://docs.nvidia.com/cuda/

# for Nvidia GeForce GTX 1060 6GB GPU: Arch sm_61
# get Nvidia CUDA-Toolkit v12.6 from https://developer.nvidia.com/cuda-toolkit-archive
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126
"""

import torch

# check if GPU is available
print("CUDA available: ", torch.cuda.is_available())
print("GPU name:       ", torch.cuda.get_device_name(0))  # sm_61
print("Current Device: ", torch.cuda.current_device())
print("Torch Version:  ", torch.__version__)
print("Torch CUDA:     ", torch.version.cuda)
print("Torch CUDNN:    ", torch.backends.cudnn.version())
print("Torch Arch List:", torch.cuda.get_arch_list())

# ----------------------------------------------------------------------------
