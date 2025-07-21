README

# Markdown
https://de.wikipedia.org/wiki/Markdown  
https://docs.github.com/de/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax  
https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet  

# Python
https://docs.python.org/3/  

## IDEs
VScode  
https://code.visualstudio.com/  
https://vscode.dev (Online Editor)  
Copilot  
https://code.visualstudio.com/docs/copilot/overview  
Continue.dev  
https://www.continue.dev/  

Jupyter Notebook  
https://jupyter.org/  

Google CoLab  
https://colab.research.google.com/  

Anaconda  
https://www.anaconda.com/docs/main  

Jetbrains PyCharm IDE  
https://www.jetbrains.com/pycharm/  

MuCode  
https://codewith.mu/  

## Tutorials
https://docs.python.org/3/tutorial/  
https://www.w3schools.com/python/  
https://www.geeksforgeeks.org/python/python-programming-language-tutorial/  
https://www.learnpython.org/  
https://www.datacamp.com/tutorial  

------------------------------------------------------------------------------  

# Libraries

# Project management
uv  
https://docs.astral.sh/uv/  
https://www.datacamp.com/tutorial/python-uv  

Dotenv  
https://pypi.org/project/python-dotenv/  
https://www.geeksforgeeks.org/python/using-python-environment-variables-with-python-dotenv/  

venv  
https://docs.python.org/3/library/venv.html  

pip  
https://packaging.python.org/en/latest/tutorials/installing-packages/  

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

## CUI  
termcolor  
colorama  
pyfiglet  

ASCIIMATICS  
https://github.com/peterbrittain/asciimatics  

Terminal TextEffects  
https://github.com/ChrisBuilds/terminaltexteffects  

## TUI  
Textual  
https://textual.textualize.io/  

Typer  
https://typer.tiangolo.com/  

Rich  
https://github.com/Textualize/rich  
https://rich.readthedocs.io/  

PyTermGUI  
https://pypi.org/project/PyTermGUI/7.1.0/  

## GUI
wxPython  
https://www.wxpython.org/  
wxFormBuilder  
https://github.com/wxFormBuilder/wxFormBuilder  

Arcade  
https://api.arcade.academy/  

Pygame  
https://www.pygame.org/docs/  

Flask  
https://flask.palletsprojects.com/en/stable/  

## Web
Requests  
https://pypi.org/project/requests/  
https://requests.readthedocs.io/  
https://www.w3schools.com/python/module_requests.asp  

httpx  
https://www.python-httpx.org/  
https://pypi.org/project/httpx/  

Scrapy  
https://www.scrapy.org/  

Beautiful Soup (bs4)  
https://pypi.org/project/beautifulsoup4/  

## Media
Pillow, PIL  
https://pillow.readthedocs.io/en/stable/handbook/tutorial.html  

Bokeh  
https://bokeh.org/  

OpenCV  
https://opencv.org/get-started/  

## DS | ML | AI
NumPy  
https://numpy.org/  
https://www.w3schools.com/python/numpy/numpy_intro.asp  

Pandas  
https://pandas.pydata.org/  
https://www.w3schools.com/python/pandas/default.asp  

Matplotlib  
https://matplotlib.org/  
https://matplotlib.org/cheatsheets/  
https://www.w3schools.com/python/matplotlib_pyplot.asp  

SciPy  
https://scipy.org/  

scikit-learn  
https://scikit-learn.org/stable/  

PyTorch  
https://pytorch.org/  
TensorFlow  
Keras  
Theano  



------------------------------------------------------------------------------

# venv
https://docs.python.org/3/tutorial/venv.html  
https://docs.python.org/3/library/venv.html  

python -m venv .venv       \#Create  

source .venv/bin/activate  \#Linux  
.venv\Scripts\activate     \#Windows  
which python               \#check, if venv is running  

pip install -r requirements.txt  
Deactivate  

https://code.visualstudio.com/docs/python/environments  

------------------------------------------------------------------------------

# uv
https://docs.astral.sh/uv/getting-started/installation/  

\# installation  
pip install uv  \# better use PowerShell Installer from webpage, to add uv to your path  

uv help  


\# example: using oterm for ollama  
uvx oterm  \# uvx equals ‘uv run’  
uv run oterm  \# runs oterm in a temporary venv  
uv tool install oterm  \# ~/.local/bin  
uv tool dir  \# show directories  


uv init .  
\# creates a toml-file, main.py  
uv add pygame  
\# creates a .venv with dependencies  
uv run ./main.py  
\# automatically activates the .venv  

uv venv  
source .venv/bin/activate  
uv pip install .  

------------------------------------------------------------------------------

# pip
https://pypi.org/project/pip/   
https://packaging.python.org/en/latest/tutorials/installing-packages/  
site-packages  

pip list  
pip install <package>  
pip install -r requirements.txt  
pip freeze > requirements.txt  

------------------------------------------------------------------------------

# conda
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html  
https://conda.io/projects/conda/en/latest/commands.html?highlight=conda-vs-pip-vs-virtualenv-commands\#conda-vs-pip-vs-virtualenv-commands  

\# create  
conda create --help  
conda create -n .venv [--file requirements.txt]  
\#conda env create -f environment.yml  

\# activate  
conda activate .venv  
\#c:\Anaconda3\Scripts\activate  

conda init --help  

\# info  
conda env list  
conda info --envs  
conda info  
conda list --explicit > spec-file.txt  

\# packages  
conda search <package>  
conda install <package>  

conda list --export              \# create requirements.txt  
conda list -e > requirements.txt \# save all the info about packages  

conda update --all  

------------------------------------------------------------------------------

