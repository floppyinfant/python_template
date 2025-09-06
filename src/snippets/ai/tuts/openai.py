"""

"""

# ----------------------------------------------------------------------------

"""
Hugging Face Inference Providers

https://github.com/huggingface/hub-docs/blob/main/docs/inference-providers/index.md

Shell:
pip install huggingface_hub
hf auth login # get a read token from hf.co/settings/tokens
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    messages=[
        {
            "role": "user",
            "content": "How many 'G's in 'huggingface'?"
        }
    ],
)

# ----------------------------------------------------------------------------

"""
Hugging Face Inference Providers

https://github.com/huggingface/hub-docs/blob/main/docs/inference-providers/index.md

Shell:
pip install huggingface_hub
hf auth login # get a read token from hf.co/settings/tokens
"""

import os
import requests

API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {"Authorization": f"Bearer {os.environ['HF_TOKEN']}"}
payload = {
    "messages": [
        {
            "role": "user",
            "content": "How many 'G's in 'huggingface'?"
        }
    ],
    "model": "deepseek-ai/DeepSeek-V3-0324",
}

response = requests.post(API_URL, headers=headers, json=payload)
print(response.json()["choices"][0]["message"])
