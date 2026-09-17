# Hugging Face

CLI Tool to manage login, download of models etc.

create an access token on the website:

https://huggingface.co/settings/tokens

Install the package, that contains the CLI tool:

```bash
uv add huggingface_hub[cli]
```

In the terminal (inside PyCharm):

```bash
huggingface-cli login
# paste in the access token

# huggingface-cli == hf
uv run hf auth login
uv run hf download user/model-name

# clean models cache
hf cache scan
hf cache delete
# select model to delete with space, enter, enter
# newer versions use:
hf cache ls
hf cache rm
```

