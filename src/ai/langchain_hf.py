"""
Example from YT: "Tech with Tim"
https://youtu.be/1h6lfzJ0wZw
"""

import os
from dotenv import load_dotenv

from transformers import pipeline
from transformers.utils.logging import set_verbosity_error
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate

import torch

#set_verbosity_error()

# ----------------------------------------------------------------------------
# check if GPU is available
print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda.current_device())
print(torch.cuda.get_device_name(0))
# ----------------------------------------------------------------------------

load_dotenv(verbose=True)
key = os.getenv("API_KEY")

model = pipeline("summarization", model="facebook/bart-base", device="0")
response = model("text to summarize")
print(response)

# ----------------------------------------------------------------------------
# langchain pipeline wrapper
model_hf = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1", device="0", max_len=256, truncation=True)
llm = HuggingFacePipeline(pipeline=model_hf)

template = PromptTemplate.from_template("Explain {topic} in detail for a {age} year old human")

chain = template | llm
topic = input("Topic: ")
age = input("Age: ")

response_hf = chain.invoke({"topic": topic, "age": age})
print(response_hf)

# ----------------------------------------------------------------------------

