"""
Hugging Face Inference Providers

https://github.com/huggingface/hub-docs/blob/main/docs/inference-providers/index.md

Shell:
pip install huggingface_hub
hf auth login # get a read token from hf.co/settings/tokens
"""

import os
from huggingface_hub import InferenceClient

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

