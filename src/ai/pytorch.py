"""
TensorFlow
https://www.tensorflow.org/ 
https://en.wikipedia.org/wiki/TensorFlow 
https://github.com/tensorflow/tensorflow 


Keras
https://keras.io/examples/ 
https://en.wikipedia.org/wiki/Keras 
https://github.com/keras-team/keras 


Theano
https://en.wikipedia.org/wiki/Theano_(software) 
https://github.com/Theano/Theano


PyTorch
https://pytorch.org/ 
https://en.wikipedia.org/wiki/PyTorch 
https://github.com/pytorch 


JAX
https://github.com/jax-ml/jax
pip install -U "jax[cuda12]"


Hugging Face Transformers
https://huggingface.co/docs/transformers/index
https://huggingface.co/docs/transformers/pipeline_tutorial
https://github.com/huggingface/transformers/tree/main
uv pip install "transformers[torch]"


LangChain
https://www.langchain.com/ 
https://python.langchain.com/docs/introduction/
https://github.com/langchain-ai/langchain 
LangGraph
LangSmith


Unsloth
https://github.com/unslothai/unsloth
https://docs.unsloth.ai/
pip install unsloth
"""

import torch
from transformers import pipeline

import jax
import numpy as np
import jax.numpy as jnp
from jax import jit

