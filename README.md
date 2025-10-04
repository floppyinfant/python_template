# Documentation of Language and Tools

## PyCharm (IDE)
https://www.jetbrains.com/help/pycharm/getting-started.html  

## VScode (IDE)
https://code.visualstudio.com/docs  
https://vscode.dev (Online Editor)  

## git
https://git-scm.com/doc
https://docs.github.com/en
https://www.jetbrains.com/help/pycharm/2025.1/sync-with-a-remote-repository.html#update  

### Markdown
https://de.wikipedia.org/wiki/Markdown  
https://docs.github.com/de/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax  
https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet  

## Docker
https://docs.docker.com/  

Vagrant  
https://developer.hashicorp.com/vagrant/intro  

## Python
https://docs.python.org/3/  
https://docs.python.org/3/howto/index.html  

Python 3.13 @since 2014-10: no GIL  
https://www.heise.de/news/Python-3-13-Bessere-interaktive-Shell-und-endlich-Multithreading-ohne-GIL-9968435.html  
https://docs.python.org/3/whatsnew/3.13.html  

### uv (Project Management)
https://docs.astral.sh/uv/  
https://docs.astral.sh/uv/getting-started/installation/    
https://www.datacamp.com/tutorial/python-uv  
```
# installation  
pip install uv          # better use PowerShell Installer from webpage, to add uv to your path  

uv help  

uv init .               # creates a toml-file, main.py  
uv add pygame           # creates a .venv with dependencies  
uv run ./main.py        # automatically activates the .venv  

uv venv  
source .venv/bin/activate  
uv pip install .  

# example: using oterm for ollama  
uvx oterm               # uvx equals ‘uv run’  
uv run oterm            # runs oterm in a temporary venv  
uv tool install oterm   # ~/.local/bin  
uv tool dir             # show directories  
```

### pip  
https://pypi.org/project/pip/   
https://packaging.python.org/en/latest/tutorials/installing-packages/  
installs to PYTHONHOME/Lib/site-packages  
```
pip list  
pip install <package>  
pip install -r requirements.txt  
pip freeze > requirements.txt  
```

### venv  
https://docs.python.org/3/tutorial/venv.html  
https://docs.python.org/3/library/venv.html  
https://code.visualstudio.com/docs/python/environments  
```
python -m venv .venv       # Create  

source .venv/bin/activate  # Linux  
.venv\Scripts\activate     # Windows  
which python               # check, if venv is running  

pip install -r requirements.txt  
Deactivate  
```

## Anaconda
https://www.anaconda.com/docs/main  

### conda  
https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html  
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html  
https://conda.io/projects/conda/en/latest/commands.html?highlight=conda-vs-pip-vs-virtualenv-commands\#conda-vs-pip-vs-virtualenv-commands  
```
# create conda environment  
conda create --help  
conda create -n .venv [--file requirements.txt]  
#conda env create -f environment.yml  

# activate  
conda activate .venv  
#c:\Anaconda3\Scripts\activate  

conda init --help  

# info  
conda env list  
conda info --envs  
conda info  
conda list --explicit > spec-file.txt  

# package management  
conda search <package>  
conda install <package>  

conda list --export              # create requirements.txt  
conda list -e > requirements.txt # save all the info about packages  

conda update --all
```

## Jupyter
https://docs.jupyter.org/en/latest/  
https://code.visualstudio.com/docs/datascience/notebooks-web  

Google CoLab  
https://colab.research.google.com/  

Datalore Jetbrains  
https://datalore.jetbrains.com/  

### Libraries
Numpy  
https://numpy.org/doc/  

Pandas  
https://pandas.pydata.org/docs/  

@see Libraries (down below)  

### Cheat Sheets 
https://www.datacamp.com/cheat-sheet  
https://www.geeksforgeeks.org/python/python-cheat-sheet/  
https://www.pythoncheatsheet.org/  

## AI Code Assistants (Vibe Coding)

### Gemini
https://developers.google.com/gemini-code-assist/docs/overview  
https://developers.google.com/gemini-code-assist/docs/write-code-gemini  

https://cloud.google.com/gemini/docs/codeassist/gemini-cli  
https://github.com/google-gemini/gemini-cli  

https://ai.google.dev/gemini-api/docs  

### others
Copilot  
https://code.visualstudio.com/docs/copilot/overview  

Claude Code  
https://www.anthropic.com/claude-code  

Cursor  
https://cursor.com/  

Windsurf  
https://windsurf.com/  

## Blender
https://docs.blender.org/  
https://docs.blender.org/api/current/index.html  

---

# Learn

## Python
https://docs.python.org/3/  
https://docs.python.org/3/howto/index.html  

### Language features
asyncio (async/await)  
https://docs.python.org/3/library/asyncio.html  
https://docs.python.org/3/library/asyncio-task.html (Coroutines)  
https://docs.python.org/3/reference/expressions.html#await  
https://www.heise.de/hintergrund/async-await-in-Python-Nebenlaeufigkeit-leicht-gemacht-6193925.html  

Concurrency (threading, subprocess)  
https://docs.python.org/3/library/concurrency.html  

Typing  
https://docs.python.org/3/library/typing.html  

Annotaions  
https://docs.python.org/3/howto/annotations.html  

Decorators  
https://docs.python.org/3/glossary.html#term-decorator  

Context Manager (with)  
https://docs.python.org/3/library/stdtypes.html#context-manager-types  

sys  
https://docs.python.org/3/library/sys.html  

os  
https://docs.python.org/3/library/os.html  

argparse  
https://docs.python.org/3/howto/argparse.html#argparse-tutorial  

logging  
https://docs.python.org/3/howto/logging.html#logging-howto  
https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook  

re  
https://docs.python.org/3/howto/regex.html#regex-howto  

Functional programming  
https://docs.python.org/3/howto/functional.html#functional-howto  

### Tutorials
https://docs.python.org/3/tutorial/  
https://www.w3schools.com/python/  
https://www.datacamp.com/tutorial  
https://www.geeksforgeeks.org/python/python-programming-language-tutorial/  
https://www.learnpython.org/  

---

## Project management
uv  
https://docs.astral.sh/uv/  
https://www.datacamp.com/tutorial/python-uv  

venv  
https://docs.python.org/3/library/venv.html  

Dotenv  
https://pypi.org/project/python-dotenv/  
https://www.geeksforgeeks.org/python/using-python-environment-variables-with-python-dotenv/  

pip  
https://packaging.python.org/en/latest/tutorials/installing-packages/  

pipx  
https://pipx.pypa.io/  

conda  
https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html  
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html  

PyPA  
https://packaging.python.org/en/latest/key_projects/  

wheel  
https://pypi.org/project/wheel/  
https://packaging.python.org/en/latest/specifications/binary-distribution-format/  

PyInstaller  
https://pyinstaller.org/  

---

## Libraries

### CUI  
termcolor  
https://pypi.org/project/termcolor/  

colorama  
https://pypi.org/project/colorama/  
https://github.com/tartley/colorama/  
https://www.geeksforgeeks.org/python/introduction-to-python-colorama/
@see Rich  

pyfiglet  
https://pypi.org/project/pyfiglet/  

ASCIIMATICS  
https://github.com/peterbrittain/asciimatics  

Terminal TextEffects (TTE)  
https://github.com/ChrisBuilds/terminaltexteffects  

### TUI  
Textual  
https://textual.textualize.io/  

Rich  
https://github.com/Textualize/rich  
https://rich.readthedocs.io/  

Typer  
https://typer.tiangolo.com/  

PyTermGUI  
https://pypi.org/project/PyTermGUI/7.1.0/  

### GUI
PyQt | Pyside  
https://realpython.com/qt-designer-python/  

PyGTK  
https://www.gtk.org/docs/language-bindings/python  

wxPython  
https://www.wxpython.org/  
https://docs.wxpython.org/index.html  
https://github.com/wxWidgets/Phoenix  
wxWidgets  
https://www.wxwidgets.org/  
wxFormBuilder  
https://github.com/wxFormBuilder/wxFormBuilder  
wxGlade  
https://wxglade.sourceforge.net/  
BoaConstructor  
https://wiki.wxpython.org/BoaInstallGuide  

Tkinter  
https://docs.python.org/3/library/tkinter.html  

Pygame  
https://www.pygame.org/docs/  

Arcade  
https://api.arcade.academy/  

### Web
Requests  
https://pypi.org/project/requests/  
https://requests.readthedocs.io/  
https://www.w3schools.com/python/module_requests.asp  

httpx  
https://www.python-httpx.org/  
https://pypi.org/project/httpx/  

Django  
https://www.djangoproject.com/  

Flask  
https://flask.palletsprojects.com/en/stable/  

FastAPI  
https://fastapi.tiangolo.com/  
https://github.com/fastapi  
https://www.datacamp.com/de/tutorial/introduction-fastapi-tutorial  

Scrapy  
https://www.scrapy.org/  

Beautiful Soup (bs4)  
https://pypi.org/project/beautifulsoup4/  

### Media
Pillow, PIL  
https://pillow.readthedocs.io/en/stable/handbook/tutorial.html  

OpenCV  
https://opencv.org/get-started/  

@see Computer Vision (CV)  

### DataScience (DS) | Machine Learning (ML) | Artificial Intelligence (AI)
NumPy  
https://numpy.org/  
https://numpy.org/learn/  
https://numpy.org/doc/  
https://github.com/numpy/numpy  
https://www.w3schools.com/python/numpy/numpy_intro.asp  

Pandas  
https://pandas.pydata.org/  
https://www.w3schools.com/python/pandas/default.asp  

SciPy  
https://scipy.org/  

Matplotlib  
https://matplotlib.org/  
https://matplotlib.org/cheatsheets/  
https://www.w3schools.com/python/matplotlib_pyplot.asp  
PyLab: deprecated MATLAB like Interface to Matplotlib  

Seaborn  
https://seaborn.pydata.org/index.html  

Bokeh  
https://bokeh.org/  

scikit-learn  
https://scikit-learn.org/stable/  
https://github.com/scikit-learn  

NLTK  
https://www.nltk.org/  

PyTorch  
https://pytorch.org/  
https://github.com/pytorch  

TensorFlow  
https://www.tensorflow.org/  
https://github.com/tensorflow/tensorflow  

Keras  
https://keras.io/examples/  
https://github.com/keras-team/keras  

Theano  
https://github.com/Theano/Theano  

JAX  
https://github.com/jax-ml/jax  

Hugging Face Transformers  
https://huggingface.co/docs/transformers/index  
https://huggingface.co/docs/transformers/pipeline_tutorial   
https://github.com/huggingface/transformers/tree/main  
uv pip install "transformers[torch]"  

GGML  
https://github.com/ggml-org/ggml   
https://ggml.ai/  
https://huggingface.co/blog/introduction-to-ggml  
GGUF  
checkpoints (ckpt)  
safetensor  

Ollama Python SDK  
https://github.com/ollama/ollama-python  

Unsloth  
https://github.com/unslothai/unsloth  
https://docs.unsloth.ai/  
Fine Tune LLMs, LoRAs  

MCP Python SDK  
https://github.com/modelcontextprotocol/python-sdk  

LangChain  
https://www.langchain.com/   
https://python.langchain.com/docs/introduction/  
https://github.com/langchain-ai/langchain   
LangGraph  
LangSmith  
build AI Agents  

OpenAI SDK  
https://ai.google.dev/gemini-api/docs/openai  

Google Gemini API  
https://ai.google.dev/gemini-api/docs   
https://ai.google.dev/gemini-api/docs/libraries  
https://github.com/google-gemini/cookbook (Gemini API Cookbook)  
https://ai.google.dev/gemini-api/docs  

Google GenAI  
https://github.com/googleapis/python-genai  
https://googleapis.github.io/python-genai/  

Nvidia Omniverse  
https://www.nvidia.com/en-us/omniverse/  

Genesis Physics Engine  
https://genesis-embodied-ai.github.io/  

### Computer Vision (CV)  

OpenCV  
https://opencv.org/   
https://www.opencv.ai/  

SimpleCV  
https://simplecv.org/   

skimage (scikit-image)  
https://scikit-image.org/   

PyTorch (torchvision)  
https://docs.pytorch.org/vision/stable/index.html   

YOLO  
https://pjreddie.com/darknet/yolo/   
https://datascientest.com/de/you-only-look-once-yolo-was-ist-das  
https://en.wikipedia.org/wiki/You_Only_Look_Once  
