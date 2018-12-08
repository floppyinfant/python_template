TODO

.. reStructuredText (README.rst)
.. @see Python Docutils
.. http://docutils.sourceforge.net/rst.html
.. http://docutils.sourceforge.net/docs/user/rst/quickstart.html
.. http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt

.. example: https://raw.githubusercontent.com/takluyver/pynsist/master/README.rst

-------------------------------------------------------------------------------

@see comments in src/main.py
@see /docs

-------------------------------------------------------------------------------

Install Software
----------------
Anaconda

...and Tools
------------
git
https://git-scm.com/downloads

One of...
Microsoft VSCode + Extension Python
Github Atom Editor
Jetbrains PyCharm


Virtual Environment
-------------------
https://conda.io/docs/commands.html#conda-vs-pip-vs-virtualenv-commands

# Anaconda
conda info --envs
conda create --name <environment-name> python
source activate <environment-name>
source deactivate

# to export environment file
activate <environment-name>
conda env export > <environment-name>.yml
# for other person to use the environment
conda env create -f <environment-name>.yml


# virtualenv
lsvirtualenv
cd $ENV_BASE_DIR
virtualenv $ENVIRONMENT_NAME
source $ENV_BASE_DIR/$ENVIRONMENT_NAME/bin/activate
deactivate


Requirements
------------
# Anaconda
conda install --yes --file requirements.txt

# if one dependency fails, all the rest will fail; better use this:
# Linux or Cygwin Bash
while read requirement; do conda install --yes $requirement; done < requirements.txt 2>error.log
# Windows cmd.exe
for /f %i in (requirements.txt) do conda install --yes %i - when run manually
for /f %%i in (requirements.txt) do conda install --yes %%i - when inside a BAT script


# pip
# https://pip.pypa.io/en/stable/user_guide/#requirements-files
pip install -r requirements.txt


# Package Management, manually
# Anaconda
conda search $SEARCH_TERM
conda list --name $ENVIRONMENT_NAME
# create requirements file
conda list --export > requirements.txt

conda update <package>
conda update --all
conda update python

conda install <package>
conda remove --name $ENVIRONMENT_NAME $PACKAGE_NAME


# pip
pip search $SEARCH_TERM
pip list
# create requirements file
pip freeze

pip install <package>
pip install --upgrade $PACKAGE_NAME
pip uninstall $PACKAGE_NAME


# "special packages"
# upgrade pip
python -m pip install --upgrade pip wheel setuptools
# Kivy
conda install kivy -c conda-forge
# Kivy installed with pip
# https://kivy.org/doc/stable/installation/installation.html
# Kivy Dependencies (sdl2, glew, gstreamer)
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer  # skip this, if video is not needed
python -m pip install kivy
python -m pip install kivy_examples
# run examples showcase
python share\kivy-examples\demo\showcase\main.py

# PyInstaller
# https://www.pyinstaller.org/
pip install pyinstaller
# Pygame
# https://www.pygame.org/wiki/GettingStarted
python3 -m pip install -U pygame --user
# OpenCV 2.0
# Pillow


Build & Deploy
--------------
PyInstaller
https://pyinstaller.readthedocs.io/en/stable/usage.html

Buildozer VM
https://kivy.org/doc/stable/guide/packaging-android.html
https://github.com/kivy/buildozer


Workflow
--------
# use existing repository
clone https://github.com/<useraccount>/<repository>.git
# update local repository (merge)
git pull origin master

# create new repository
git init
# once
git remote add origin https://github.com/floppyinfant/python_template.git

# commit new code
git add *
git commit -m "comment"
git push origin master

# anytime
git status

# workflow cycles:
# 1. workflow: pull (update | merge), edit, stage/commit changes, push files to server
# 2. workflow: feature branch
# 3. workflow: pull requests (from forked repository)

-------------------------------------------------------------------------------
