"""
Fine-Tuning of LLMs

using Unsloth
run in Google CoLab (using GPUs)
https://research.google.com/colaboratory/faq.html#gpu-availability

!pip install unsloth trl peft accelerate bitsandbytes

from unsloth import FastLanguageModel
from datasets import Dataset
from trl import SFTTrainer
from transformers import TrainingArguments
from google.colab import files

import torch
import json
import os
"""

