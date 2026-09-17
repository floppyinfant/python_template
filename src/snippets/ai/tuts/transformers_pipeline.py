"""
Tech with Tim
https://www.youtube.com/watch?v=1h6lfzJ0wZw

create an access token on the website:
https://huggingface.co/settings/tokens

# install the package, that contains the CLI tool:
uv add huggingface_hub[cli]

in the terminal (inside PyCharm):
huggingface-cli login

# huggingface-cli == hf
uv run hf auth login
uv run hf download user/model-name

# clean models cache
hf cache scan
hf cache delete
# select model to delete with space, enter, enter
"""

from transformers import pipeline

model = pipeline("summarization", "facebook/bart-large-cnn")
response = model("text to summarize")

print(response)

