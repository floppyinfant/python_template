"""
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

TensorFlow
https://www.tensorflow.org/
https://en.wikipedia.org/wiki/TensorFlow
https://github.com/tensorflow/tensorflow


Keras
https://keras.io/examples/
https://en.wikipedia.org/wiki/Keras
https://github.com/keras-team/keras

"""

import torch
from transformers import pipeline

import jax
import numpy as np
import jax.numpy as jnp
from jax import jit

import tensorflow as tf
