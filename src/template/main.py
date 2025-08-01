#!/usr/bin/env python

# -*- coding: utf-8 -*-

# make file executable in Linux Terminal: 'chmod a+x main.py'

# Alternative Shebangs:
# #!/usr/bin/env python3
# don't use:
# #!/usr/bin/python
# #!/usr/local/bin/python
# #!/bin/python

# -------------------------------------------------------------------------------------------

"""
Author: Thorsten Mauthe, <email@host>
Date: 20XX-XX-XX
Version: 0.1

License: e.g. Apache 2
https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licenses
https://choosealicense.com/licenses/
https://tldrlegal.com/

Created by Thorsten Mauthe on 20XX-XX-XX.
Copyright (c) 20XX Thorsten Mauthe. All rights reserved.

"""

__author__ = 'TM'
__date__ = '20170208'
__version__ = 0.1
__description__ = ''


# -------------------------------------------------------------------------------------------
# comments - Tools, Documentation, Resources, Links
# -------------------------------------------------------------------------------------------

"""
Version Control System (VCS) | Software Versionsverwaltung
Source Code Management | Source Control Management (SCM)
Software Configuration Management (SCM)
e.g. Git, Mercurial (hg), Subversion (svn) Concurrent Versions System (CVS), ... Microsoft Visual Studio Team Services | Team Foundation Version Control | Visual SourceSafe (1994)
https://en.wikipedia.org/wiki/List_of_version_control_software
https://git-scm.com/downloads
https://atom.io/#github (Atom Editor has Git and Github integration)

# GitHub

# create repository online without any files
# (if you created files (e.g. .gitignore, README.md) do git pull (merge) before git push)
cd app/
git init
git add *
# anytime
git status
git commit -m "comment"
# once
git remote add origin https://github.com/floppyinfant/python_template.git
git push origin master

# on a new machine
git clone https://github.com/floppyinfant/python_template.git
# update local repository (merge)
git pull origin master

# workflow cycles:
# 1. workflow: pull (update | merge), edit, stage/commit changes, push files to server
# 2. workflow: feature branch
# 3. workflow: pull requests (from forked repository)
"""

# -------------------------------------------------------------------------------------------

"""
### Python Distributions:
#
## Python.org
# https://www.python.org/
## Anaconda
# https://www.anaconda.com/what-is-anaconda/
## Enthought
# https://www.enthought.com/product/enthought-python-distribution/
## ActivePython
# https://www.activestate.com/activepython
"""

# -------------------------------------------------------------------------------------------

"""
### Virtual Environments:
# https://conda.io/docs/commands.html#conda-vs-pip-vs-virtualenv-commands

## venv
# https://docs.python.org/3/library/venv.html
# python -m venv .venv
# source .venv/bin/activate  #Linux
# .venv/Scripts/activate     #Windows

## virtualenv
# https://virtualenv.pypa.io/en/stable/
# # list environments
# lsvirtualenv
# cd $ENV_BASE_DIR; virtualenv $ENVIRONMENT_NAME
# source $ENV_BASE_DIR/$ENVIRONMENT_NAME/bin/activate
# deactivate

## conda
# # list all environments
# conda info --envs
# conda create --name $ENVIRONMENT_NAME python
# source activate $ENVIRONMENT_NAME
# source deactivate

## uv
# @see Package Management
"""

# Shell:
# create virtual environment in current directory:
# python -m venv .venv

# Activate virtual environment:
# source .venv/bin/activate  #Linux
# .venv\Scripts\activate     #Windows

# Install packages in virtual environment:
# pip install -r requirements.txt


# Alternatives:
# conda
# uv

# -------------------------------------------------------------------------------------------

"""
### Package Management:

## conda
# https://conda.io/docs/user-guide/overview.html
# https://conda.io/docs/_downloads/conda-cheatsheet.pdf
# conda search $SEARCH_TERM
# conda list --name $ENVIRONMENT_NAME
# # create requirements file
# conda list --export
#
# conda update <package>
# conda update --all
# conda update python
#
# conda install <package>
# conda remove --name $ENVIRONMENT_NAME $PACKAGE_NAME


## pip, PyPI (Python Package Index)
# https://pypi.org/
# https://pip.pypa.io/en/stable/
# https://pip.pypa.io/en/stable/user_guide/#requirements-files
# https://packaging.python.org/tutorials/packaging-projects/
#
# pip search $SEARCH_TERM
# pip list
# # create requirements file
# pip freeze
# pip install -r requirements.txt
#
# pip install <package>
# pip install --upgrade $PACKAGE_NAME
# pip uninstall $PACKAGE_NAME


## uv
# https://docs.astral.sh/uv/
# https://docs.astral.sh/uv/getting-started/features/
#
# Python Versions:
# uv python list
#
# Scripts:
ä uv run <script_name>
#
# Projects:
# https://docs.astral.sh/uv/guides/projects/
# https://docs.astral.sh/uv/guides/migration/pip-to-project/#requirements-files
# uv init .
#
# uv init <project_name>  # pyproject.toml
# cd <project_name>
# uv add <package_name>   # creates .venv
#
# uv sync                 # install packages in .venv
# uv tree                 # show package tree
# uv build                # build package
# uv publish              # publish package to a package index
#
# Tools:
# https://docs.astral.sh/uv/guides/tools/
# uvx <package_name>      # run in a temporary environment
# uv tool run <package>   # run in a temporary environment (=uvx)
# uv tool install <package_name>
# uv tool list
# uv tool update-shell
#
# Pip Interface:
# https://docs.astral.sh/uv/pip/environments/
# uv venv                 # create virtual environment .venv
# https://docs.astral.sh/uv/pip/packages/
# uv pip install <package_name>  # install package in .venv
# .venv/Scripts/activate  # Windows: make packages of .venv available
# deactivate              # exit virtual environment
# uv pip install -e .     # install current project as an editable package
# uv pip install -r requirements.txt
# uv pip install -r pyproject.toml
# uv pip list
# uv pip tree
# uv pip freeze
# uv pip check
# https://docs.astral.sh/uv/pip/compile/
# uv pip compile pyproject.toml -o requirements.txt
# uv pip sync requirements.txt
#
# Utility:
# uv cache dir
# uv cache clear
# uv tool dir
# uv python dir
# uv self update
"""

# Shell:
# pip install -r requirements.txt


# Alternatives:
# conda
# uv

# -------------------------------------------------------------------------------------------

"""
### DEPLOYMENT:

## setuptools:

## easy_install:

## distutils:

# egg (2004), wheel (2012):
# https://packaging.python.org/discussions/wheel-vs-egg/


## Py2exe:
# http://www.py2exe.org/
# http://www.py2exe.org/index.cgi/Tutorial
#
# create a setup.py file
from distutils.core import setup
import py2exe
setup(console=['hello.py'])
# run the file in DOS Command Window
python setup.py py2exe


## PyInstaller:
# http://www.pyinstaller.org/, https://pyinstaller.readthedocs.io/en/stable/, https://github.com/pyinstaller/pyinstaller
# Libraries:
# (pefile)
# (PyWin32: http://sourceforge.net/projects/pywin32/files/)
# UDX
# PyCrypto: https://www.dlitz.net/software/pycrypto/
#
# Installation:
# pip install pyinstaller
# on error: pip install future --upgrade
#
# Usage: https://pyinstaller.readthedocs.io/en/stable/usage.html
# -D, --onedir
# -F, --onefile
# -c, --console, --nowindowed
# -w, --windowed, --noconsole
# -i, --icon <FILE.ico or FILE.exe,ID or FILE.icns>
# --upx-dir UPX_DIR
# ^ Windows Line Delimiter
# <backslash> Linux Line Delimiter
#
# Exampes:
pyinstaller --onefile --noconsole --icon=icon.ico --upx-dir=../PyInstaller-3.2/upx app.py
pyinstaller --onefile --windowed --icon=res/icon.ICO /path/to/yourscript.py


## Buildozer VM (Kivy, P4A, Plyer)
# Android *.apk export in a VirtualBox VM
# https://kivy.org/docs/guide/packaging-android-vm.html
# http://buildozer.readthedocs.io/en/latest/
# https://github.com/kivy/buildozer
#
# Terminal:
# buildozer init  # creates spec-file
# buildozer android debug deploy run


## Installer Builders:

## Pynsist (based on NSIS)
# https://pypi.python.org/pypi/pynsist
# https://pynsist.readthedocs.io/en/latest/
# https://github.com/takluyver/pynsist/
# Download NSIS from http://nsis.sourceforge.net/Download


## Inno Setup
# http://www.jrsoftware.org/isinfo.php
# IS Tool (GUI)
# http://www.istool.org/
# https://sourceforge.net/projects/istool/


## Alternative Installer:
# Nullsoft Scriptable Install System (NSIS)
# Windows Installer XML (WiX)
# Install Shield (proprietary)
"""

# Alternatives:
# uvx
# pipx

# git clone <repository>
# git release <tag>

# -------------------------------------------------------------------------------------------

"""
### IDEs:
# https://wiki.python.org/moin/IntegratedDevelopmentEnvironments
# https://wiki.python.org/moin/PythonEditors
# https://www.pythoncentral.io/comparison-of-python-ides-development/

## IDLE

## Jupyter Notebook
# http://jupyter.org/
# https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html

## IPython
# https://ipython.org/

## Atom Editor
# https://atom.io/#ide

## PyCharm
# http://www.jetbrains.com/pycharm/

## Wing IDE
# http://wingware.com/

## Eclipse PyDev
# http://pydev.org/

## Python Tools for Visual Studio (PTVS): xlrd, xlwt
# https://marketplace.visualstudio.com/items?itemName=donjayamanne.python
# https://microsoft.github.io/PTVS/

## Netbeans
# http://wiki.netbeans.org/Python

## Komodo IDE
# http://www.activestate.com/komodo-ide

## Visual Studio Code
# https://code.visualstudio.com/
#
# Copilot
# https://code.visualstudio.com/docs/copilot/overview
#
# Continue.dev
# https://www.continue.dev/

## Mu Editor
# https://codewith.mu/

## Thonny
# https://thonny.org/

## Sublime Text
# https://www.sublimetext.com/

## Neovim
# https://neovim.io/

## Vim
# https://www.vim.org/

## Emacs
# https://www.gnu.org/software/emacs/

## Cursor IDE
# https://cursor.so/

"""

# -------------------------------------------------------------------------------------------
# imports, Libraries, Modules, Packages
# -------------------------------------------------------------------------------------------

# Python 3 and 2 compatibility
# these imports must be in the first place!
# https://docs.python.org/2.7/howto/pyporting.html
# http://python-future.org/
#
# https://docs.python.org/2/library/__future__.html
# https://docs.python.org/2/library/future_builtins.html
# https://docs.python.org/2/library/__builtin__.html
#
# https://docs.python.org/3/library/builtins.html
# https://docs.python.org/3/library/__future__.html
# from __future__ import print_function
# from __future__ import division
# from __future__ import unicode_literals
# from __future__ import absolute_import
# from __future__ import nested_scopes
# from __future__ import generators
# from __future__ import with_statement
# from __future__ import print_function

# -------------------------

import sys
import os
import os.path

# example for interacting with the Environment (Linux Terminal Bash Shell Console)
os.environ['PYTHONIOENCODING'] = 'utf-8'  # set encoding for stdout and stderr
os.getenv('PYTHONIOENCODING', 'utf-8')  # get encoding for stdout and stderr

# environment variables from .env file
from dotenv import load_dotenv, dotenv_values
#load_dotenv()                  # Load environment variables from .env file
config = dotenv_values(".env")  # Load environment variables into a dictionary

# -------------------------

import argparse
import getopt

import time
import datetime
import random
import math

# -------------------------

"""
# Logging:
# https://docs.python.org/2/howto/logging.html
# https://docs.python.org/2/library/logging.html
"""
import logging
logger = logging.getLogger("template")


"""
# Software Engineering, TDD:
# http://pythontesting.net/start-here
#
# pytest (py.test)
#
# unittest
# https://docs.python.org/2/library/unittest.html
# https://docs.python.org/3/library/unittest.html
# http://pythontesting.net/framework/unittest/unittest-introduction/
#
# nose
# http://pythontesting.net/framework/nose/nose-introduction/
#
# coverage
#
# doctest
#
# mock
#
# hypothesis
#
# tox
#
"""
import unittest


# -------------------------------------------------------------------------------------------
# HPC, Parallel Computing
# -------------------------------------------------------------------------------------------

"""
HPC (High Performance Computing)

Parallel Python
Concurrency
https://docs.python.org/3/library/concurrency.html
GIL (global interpreter lock)
https://docs.python.org/3/whatsnew/3.13.html#free-threaded-cpython

Modules:
threading
multiprocess
  subprocess
asyncio (async/await, Coroutines)
https://docs.python.org/3/library/asyncio.html

asynchronous IO (Twisted)

Cython
https://cython.org/
https://github.com/cython/cython 
https://en.wikipedia.org/wiki/Cython
cythonize

[SWIG (Wrapper, Bindings)]
https://www.swig.org/

Pypy
https://pypy.org/ 
JIT-Compiler

Numba
https://numba.pydata.org/
https://numba.readthedocs.io/en/stable/cuda/index.html

Taichi
https://www.taichi-lang.org/ 

"""

import threading
from threading import Thread

# -------------------------

from multiprocessing import Pool, Process, Queue

def timer(f):
    """ Decorator """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)  # execute wrapped function
        stop_time = time.time()
        elapsed_time = stop_time - start_time
        print(f"delta_time (dt) = {elapsed_time}")
        return result
    return wrapper

@timer
def multithreaded():
    with Pool() as pool:
        results = pool.imap()


# -------------------------

import asyncio

async def coroutine():
    await asyncio.sleep(1)
    # keyword await only inside async def

async def start_coroutine():
    task = asyncio.create_task(coroutine())
    value = await task

def main_async():
    asyncio.run(start_coroutine())


# -------------------------------------------------------------------------------------------
# Data Science, Machine Learning, Deep Learning, AI
#
# Anaconda, IPython, Jupyter Notebook, Google Colab
# -------------------------------------------------------------------------------------------

"""
Data Science
Machine Learning, Deep Learning, Datamining
Generative AI, LLM, Diffusion Models

Anaconda (conda)
https://www.anaconda.com/
https://anaconda.com/app/code-in-the-cloud
https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html
https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf

Jupyter Notebook (IPython --pylab)
https://jupyter.org/

Google Colab (Colaboratory)
https://colab.research.google.com/

# -------------------------

Libraries:
Numpy, SciPy, Pandas

Scikit-learn (sklearn)

Matplotlib

Bokeh (interactive graphics)
https://bokeh.pydata.org/en/latest/

NLTK (Natural Languages Toolkit)
http://www.nltk.org/

Keras
Theano
Tensorflow (Google)
PyTorch (Facebook)
Transformers (Hugging Face)

# -------------------------

Numba
https://numba.pydata.org/
https://numba.readthedocs.io/en/stable/cuda/index.html

Taichi
https://www.taichi-lang.org/ 

"""

import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import bokeh.plotting as bp

import numba
import taichi as ti


# -------------------------------------------------------------------------------------------
# Image Processing, Computer Vision
# -------------------------------------------------------------------------------------------

"""
Image Processing

PIL (Python Imaging Library) for Python 2
Pillow (PIL fork) for Python 3
https://pillow.readthedocs.io/en/stable/

OpenCV
https://opencv.org/get-started/

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
"""

from PIL import Image, ImageFilter

def test_pil():
    resource = os.path.join("res", "gfx", "cat.png")
    image = Image.open(resource)
    blurredImage = image.filter(ImageFilter.BLUR)
    image.show()
    blurredImage.show()

# -------------------------

import cv2

def test_cv():
    resource = os.path.join("res", "gfx", "cat.png")
    image = cv2.imread(resource)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# -------------------------

import skimage as ski
#import matplotlib.pyplot as plt

def test_skimage():
    # Load an image
    resource = os.path.join("res", "gfx", "cat.png")
    image = ski.io.imread(resource)

    # Convert the image to grayscale
    gray_image = ski.color.rgb2gray(image)

    # Detect corners using Harris corner detector
    corners = ski.feature.corner_peaks(ski.feature.corner_harris(gray_image), min_distance=5)

    # Display the original image with detected corners
    plt.imshow(image)
    plt.scatter(corners[:, 1], corners[:, 0], color='red')
    plt.show()


# -------------------------------------------------------------------------------------------
# Regular Expressions (RegEx)
# -------------------------------------------------------------------------------------------

"""
Regular Expressions (RegEx)
https://docs.python.org/3/library/re.html

Regex Patterns:
\d    # match one digit
\w    # match one alphanumeric character
\s    # match one whitespace character
.     # match any character except newline
[]    # match any character in the brackets
[^]   # match any character not in the brackets

Regex Anchors:
^     # match start of string
$     # match end of string

Regex Quantifiers:
*     # match zero or more occurrences
+     # match one or more occurrences
?     # match zero or one occurrence
{n}   # match exactly n occurrences
{n,}  # match n or more occurrences
{n,m} # match between n and m occurrences

Regex Groups:
(ab)  # match the group ab
(a|b) # match either a or b
match.group(1)       # access the matched group by index starting from 1
(?P<name>ab)         # match the group ab and name it 'name'
match.group('name')  # access the named group 'name'
"""

import re

# fileformats for Parser:
import json
import csv

def test_re():
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

    # regex = '^[A-C].*'             # match names starting with A, B or C
    regex = re.compile(r'^[A-C]')  # match names starting with A, B or C

    for name in names:
        match = re.search(regex, name)
        # match = re.match(regex, name)       # returns a match object if the string starts with the pattern
        # match = re.fullmatch(regex, name)   # returns a match object if the entire string matches the pattern
        # match = re.split(regex, name)       # returns a list of strings split by the pattern
        # match = re.sub(regex, 'X', name)    # replaces the pattern with 'X' in the string
        # matches = re.findall(regex, name)   # returns a list of all matches
        # matches = re.finditer(regex, name)  # returns an iterator yielding match objects
        if match:
            print(f"Matched: {name} at position: {match.span()} with group: {match.group()}")

    # matches = [name for name in names if regex.match(name)]


# -------------------------------------------------------------------------------------------
# Database (DB)
# CRUD (Create, Read, Update und Delete)
# ORM (Object-Relational Mapper)
# -------------------------------------------------------------------------------------------

# SQLAlchemy

# -------------------------

"""
SQlite
https://docs.python.org/3/library/sqlite3.html

Data Types:
INTEGER, REAL, TEXT, BLOB, NULL

mapped to Python types:
int, float, str, bytes, None

"""
import sqlite3

def createDatabase():
    """ Create a SQlite Database and Table
    """
    conn = sqlite3.connect('example.db')  # create a database file
    cur = conn.cursor()  # create a cursor object

    # Create table
    cur.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

    # Insert a row of data
    cur.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
    cur.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
    #cur.executemany(sql)           # transaction for multiple inserts
    #cur.executescript("""""")

    # Save (commit) the changes
    conn.commit()

    # Close db objects
    cur.close()   # close the cursor
    conn.close()  # Close the connection


def queryDatabase():
    """ Query the SQlite Database
    """
    conn = sqlite3.connect('example.db')  # connect to the database file
    cur = conn.cursor()  # create a cursor object

    # Query the database
    cur.execute("SELECT * FROM users")
    #cur.execute(query, parameters)  # use parameters to prevent SQL injection
    #cur.execute("SELECT * FROM users WHERE age > ?", (20,))

    rows = cur.fetchall()  # fetch all rows

    for row in rows:
        print(row)  # print each row

    # Close the connection
    cur.close()   # close the cursor
    conn.close()  # Close the connection


# -------------------------------------------------------------------------------------------
# Web, Network, WebScraping
# -------------------------------------------------------------------------------------------

"""
Web, Network, WebScraping


Requests
import requests

httpx

Scrapy
https://scrapy.org/
https://github.com/scrapy/scrapy

Beutiful Soup (bs4)
from bs4 import BeautifulSoup

Flask (Web Framework)

FastAPI

Tornado (Webserver)

Network:
Twisted

# -----------------------

# WebScraping (old):
import socket
import httplib
import htmllib
import urllib
import urllib2
from lxml import etree
from io import StringIO, BytesIO
from base64 import b64encode
#from html.parser import HTMLParser

import mechanize
from selenium import webdriver
"""

import webbrowser


class Scraper(object):
    """ TODO: Scraper
    Scrapy, urllib2, httplib

    """

    def __init__(self):
        pass

    def useScrapy(self):
        pass

    def useUrllib2(self):
        pass

    def useHttplib(self):
        pass

    def useMechanize(self):
        pass

    def useSelenium(self):
        pass


class Parser(object):
    """ TODO: Parser, File-Parser
    """

    def __init__(self, arg):
        self.arg = arg
        self.arg2 = None
        self.browser = 'Mozilla/5.0 (Windows NT 5.1; rv:20.0) Gecko/20100101 Firefox/20.0'

    def openTextFile(self):
        pass

    def openHTML(self):
        pass

    def openXML(self):
        pass

    def openDB(self):
        pass


class DBManager(object):
    """ TODO: DB-Connection-Manager
    """
    def __init__(self):
        pass


class ML(object):
    """ Machine Learning
    """
    def __init__(self):
        pass


class Environment(object):
    """ TODO: Interact with the Linux Terminal Bash Shell Console
    """

    def __init__(self):
        pass

    def openBrowser(self, url):
        webbrowser.open(url)

    def runProgram(self, prog):
        os.system(prog)
        #os.popen(prog)


# -------------------------------------------------------------------------------------------

"""
Security, Cybersecurity

Privacy, Anonymity, Tor / Onion-Routing

Forensics, TSK (The Sleuth Kit)

Reverse Engineering (Decompiler, Debugger), Greyhat Python

Penetration Testing (Pentesting), MSF (Metasploit Framework)
Ethical Hacking (Whitehat), Blackhat Python
https://github.com/dloss/python-pentest-tools
https://github.com/enaqx/awesome-pentest

@see PacktPub
https://github.com/PacktPublishing/Python-Penetration-Testing-Cookbook

Linux Distros:
https://distrowatch.com/search.php?category=Security#simple
Kali Linux, Parrot OS, BlackArch, Caine
https://www.kali.org/, https://parrotlinux.org/, 
Tails, Whonix, Qubes OS

Tools:
Scapy (Sniffer)

PeePDP
http://eternal-todo.com/tools/peepdf-pdf-analysis-tool

Cryptography
PyCrypto: https://www.dlitz.net/software/pycrypto/
Paramiko (SSH)
"""


# -------------------------------------------------------------------------------------------
# Game
# Creative Coding
# Physical Computing | IoT | MCU | Embedded | Robotics | AI
# -------------------------------------------------------------------------------------------

"""
Pygame (OpenGL, Canvas, MIDI, Sound)
https://www.pygame.org/docs/
https://inventwithpython.com/pygame/chapters/

Install: 'pip install pygame --user'
"""
import pygame
#from pygame.locals import *
import pygame.midi
#import pygame.mixer_music

# Pygame
def createCanvasWithPygame():

    global FPSCLOCK, DISPLAYSURF
    FPS = 30
    WINDOWWIDTH = 600
    WINDOWHEIGHT = 600
    BGCOLOR = (0, 0, 0)
    # variables set by mouse event
    x = 0
    y = 0

    # --------------------

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    # set up the window
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('PyGame')

    # --------------------

    # RESSOURCES

    # load images
    img = pygame.image.load('res/gfx/cat.png')
    #if img.get_size() != (IMAGESIZE, IMAGESIZE):
    #    img = pygame.transform.smoothscale(img, (IMAGESIZE, IMAGESIZE))

    """
    # load fonts
    BASICFONT = pygame.font.Font('freesansbold.ttf', 36)


    # load sounds
    # choose a desired audio format
    pygame.mixer.init(11025)
    # get path
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    # set absolute path to sample
    file_path = os.path.join(main_dir, 'res', 'bdrum.wav')
    # load sound file
    snd = pygame.mixer.Sound(file_path)
    #
    # using a collection
    #SOUNDS = {}
    #SOUNDS['bad swap'] = pygame.mixer.Sound('badswap.wav')
    #SOUNDS['match'] = []
    #for i in range(NUMSOUNDS):
    #    SOUNDS['match'].append(pygame.mixer.Sound('match%s.wav' % i))


    # MIDI
    pygame.midi.init()
    port = pygame.midi.get_default_output_id()
    midi_out = pygame.midi.Output(port, 0)

    # put all MIDI stuff in try - finally statement
    try:
        instrument = 0  # values 0 - 127
        midi_out.set_instrument(instrument)
        note = 60
        velocity = 120
        midi_out.note_on(note, velocity)
        pygame.time.wait(2000)
        midi_out.note_off(note, 0)
    finally:
        del midi_out
        pygame.midi.quit()
    """

    # --------------------

    # the main game loop
    while True:
        DISPLAYSURF.fill(BGCOLOR)

        # draw images
        DISPLAYSURF.blit(img, (x, y))

        """
        # draw text
        scoreSurf = BASICFONT.render('Score: ' + str(score), 1, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 100, 10)
        DISPLAYSURF.blit(scoreSurf, scoreRect)


        # play a sound
        print('Playing Sound...')
        channel = sound.play()
        #poll until finished
        while channel.get_busy(): #still playing
            print("...")
            time.wait(1000)
        print("...Finished!")
        """

        # event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    # you could display a confirmation window
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_BACKSPACE:
                    # leave function
                    return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    # move UP
                    pass
                elif event.key == pygame.K_a:
                    # move LEFT
                    pass
                elif event.key == pygame.K_d:
                    # move RIGHT
                    pass
                elif event.key == pygame.K_s:
                    # move DOWN
                    pass
                elif event.key == pygame.K_e:
                    # change tool
                    pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # this is the start of a mouse click or mouse drag
                lastMouseDownX, lastMouseDownY = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.pos == (lastMouseDownX, lastMouseDownY):
                    # This event is a mouse click, not the end of a mouse drag.
                    x, y = event.pos
                    # check for clicks on buttons
                    if pygame.Rect(74, 16, 111, 30).collidepoint(x, y):
                        # play sound
                        pass #snd.play()
                else:
                    # this is the end of a mouse drag
                    pass
            elif event.type == pygame.midi.MIDIIN:
                # @see pygame.midi.midis2events()
                pass
        pygame.display.update()
        FPSCLOCK.tick(FPS)

# -------------------------

"""
Arcade
https://arcade.academy/
"""
#import arcade

# -------------------------

"""
Physics Engines

Box2D
pybox2d
https://github.com/pybox2d/pybox2d/wiki/manual
conda install -c https://conda.anaconda.org/kne pybox2d

Chipmunks
https://chipmunk-physics.net/

Pymunk
http://www.pymunk.org/en/latest/
https://github.com/viblo/pymunk
https://pymunk.readthedocs.org/en/latest/

Cymunk
https://github.com/kivy/cymunk
http://cymunk.readthedocs.org/en/latest/

Cocos2d
http://python.cocos2d.org/doc.html

Genesis
https://genesis-embodied-ai.github.io/
Robot AI Physics Simulation
https://medium.com/data-science-in-your-pocket/genesis-physics-ai-engine-for-robotic-simulation-b67176c45a7d
import genesis as gs
"""

# -------------------------------------------------------------------------------------------

"""
Creative Coding

Audio | DSP | Music | MIDI

# Pure Data
pylibpd
# PortAudio
pyaudio
# Soundfont sf2
pyfluidsynth

pygame.mixer, pygame.mixer.music, pygame.midi, pygame.sndarray
https://www.pygame.org/docs/

# Music Notation
Mingus
Mido

# Music Library
Mopidy

# Digital Audio Workstation (DAW)
Reaper (DAW)

# Coding Music
Sonic Pi (Ruby)
https://sonic-pi.net/


# Creative Coding Frameworks
openFrameworks (C++) for Audio, Video, Image Processing, Computer Vision, Graphics, GUI
https://openframeworks.cc/

Processing (Java)
https://processing.org/

JUCE (C++)
https://juce.com/

# Plugin SDKs
Steinberg VST_SDK, Apple AU, CLAP

Will Pirkle (C++)
https://willpirkle.com/

"""

# -------------------------------------------------------------------------------------------

"""
MAKE::Physical Computing Platforms
Embedded Systems
Embedded Linux
Internet of Things (IoT)
Robotics

# ------------------------

Single Board Computer (SBC)

Raspberry Pi
import RPi.GPIO as GPIO

# WiringPi2

# picamera

# Wiimote (Nintendo Wii Game Controller)
import cwiid

# Minecraft Pi Edition
import mcpi

# ------------------------

Robotics

ROS2 (Robot Operating System)
https://www.ros.org/

Robots
https://eu.robotshop.com/
Unitree, Boston Dynamics

MicroMouse
https://globaltronic.pt/en/product/micromouse-kit/

MicroBit
https://makecode.microbit.org/#editor

Keyestudio Micro bit 4WD Mecanum Robot Car V2.0
https://www.keyestudio.com/products/keyestudio-micro-bit-4wd-mecanum-robot-car-v20-diy-smart-kit-with-microbit-board

BuildMecar-Kit (picamera Streaming)
https://www.waveshare.com/buildmecar-kit.htm
https://www.waveshare.com/wiki/BuildMecar-Kit#Introduction

# ------------------------

Microcontroller Unit (MCU)

MicroPython
https://micropython.org/

CircuitPython (Adafruit)
https://circuitpython.org/
https://learn.adafruit.com/welcome-to-circuitpython
https://learn.adafruit.com/circuitpython-essentials
https://learn.adafruit.com/cooperative-multitasking-in-circuitpython-with-asyncio
https://learn.adafruit.com/multi-tasking-the-arduino-part-3
https://learn.adafruit.com/adafruit-pygamer
https://learn.adafruit.com/monitor-picam-and-temperature-on-a-pitft-via-adafruit-dot-io
https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython

Mu Editor
https://codewith.mu/

Adafruit
http://www.adafruit.com/
https://github.com/adafruit
"""


# -------------------------------------------------------------------------------------------
# GUI - Graphical User Interface
# -------------------------------------------------------------------------------------------

"""
# Tkinter
# Python Shell:
# help(Tkinter.<Tab>)
# Core Widgets:
# Label, Button, Entry, Checkbutton, Radiobutton, Spinbox, Listbox, Text, Canvas, Bitmap, Image
# Toplevel, Frame, Menu, Menubutton, Scrollbar, OptionMenu, LabelFrame, Message, PanedWindow, Scale
# Geometry Managers:
# pack, grid, place
"""
import tkinter as tk
#from Tkinter import * # Python 2
#from tkinter import * # Python 3


def createGuiTk():
    win = tk.Tk()

    # Widgets
    label = tk.Label(win, text="Hello World!")
    # Geometry Managers: pack, grid, place
    label.pack()

    win.mainloop()


# -------------------------------------------------------------------------------------------

"""
wxPython
https://www.wxpython.org/

wxWidgets
https://wxwidgets.org/
https://wiki.wxwidgets.org/Tools

wxFormBuilder
https://github.com/wxFormBuilder/wxFormBuilder
"""

# -------------------------------------------------------------------------------------------

"""
Qt | KDE
https://www.qt.io/

Qt-Bindings
https://wiki.python.org/moin/PyQt
https://www.riverbankcomputing.com/static/Docs/PyQt5/

[Qt Designer]
https://www.riverbankcomputing.com/static/Docs/PyQt5/designer.html
https://doc.qt.io/qt-6/qtdesigner-manual.html

Qt Creator
https://www.qt.io/product/development-tools/
"""

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTextEdit, QAction, QStatusBar, QMessageBox
from PyQt5.QtGui import QIcon, QKeySequence

# PyQt4
#from PyQt4.QtGui import *
#import PyQt4.QtCore
# PySide
#from PySide.QtCore import Qt
#from PySide.QtGui import QApplication, QLabel
#from PySide.QtSql import *

# Qt
def createGuiQtSimple():
    # Application
    app = QApplication(sys.argv)

    # Widget
    w = QWidget()
    w.setWindowTitle('Simple')
    w.resize(250, 150)
    w.move(300, 300)
    w.show()

    app.exec_()
    # sys.exit()


# -----------------------------------------

# Qt
class MyQMainWindow(QMainWindow):

    def __init__(self):
        super(MyQMainWindow, self).__init__()

        # init GUI
        # Window (QMainWindow, QWidget)
        self.setWindowTitle("A Simple Text Editor")
        self.setWindowIcon(QIcon('res/img/appicon.png'))
        self.setGeometry(100, 100, 800, 600)
        self.setMinimumHeight(200)
        self.setMinimumWidth(280)

        # -----------------------------------------

        # Widgets (QLabel, ...)
        # CentralWidget
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        # DockWidgets

        # -----------------------------------------

        # Actions (trigger Functions)
        self.newAction = QAction(QIcon('res/img/new.png'), '&New', self, shortcut=QKeySequence.New, statusTip="Create a New File", triggered=self.newFile)
        self.openAction = QAction(QIcon('res/img/open.png'), 'O&pen', self, shortcut=QKeySequence.Open, statusTip="Open an existing file", triggered=self.openFile)
        self.saveAction = QAction(QIcon('res/img/save.png'), '&Save', self, shortcut=QKeySequence.Save, statusTip="Save the current file to disk", triggered=self.saveFile)
        self.exitAction = QAction(QIcon('res/img/exit.png'), 'E&xit', self, shortcut="Ctrl+Q", statusTip="Exit the Application", triggered=self.exitFile)
        self.cutAction = QAction(QIcon('res/img/cut.png'), 'C&ut', self, shortcut=QKeySequence.Cut, statusTip="Cut the current selection to clipboard", triggered=self.textEdit.cut)
        self.copyAction = QAction(QIcon('res/img/copy.png'), 'C&opy', self, shortcut=QKeySequence.Copy, statusTip="Copy the current selection to clipboard", triggered=self.textEdit.copy)
        self.pasteAction = QAction(QIcon('res/img/paste.png'), '&Paste', self, shortcut=QKeySequence.Paste, statusTip="Paste the clipboard's content in current location", triggered=self.textEdit.paste)
        self.selectAllAction = QAction(QIcon('res/img/selectAll.png'), 'Select All', self, statusTip="Select All", triggered=self.textEdit.selectAll)
        self.redoAction = QAction(QIcon('res/img/redo.png'), 'Redo', self, shortcut=QKeySequence.Redo, statusTip="Redo previous action", triggered=self.textEdit.redo)
        self.undoAction = QAction(QIcon('res/img/undo.png'), 'Undo', self, shortcut=QKeySequence.Undo, statusTip="Undo previous action", triggered=self.textEdit.undo)
        self.aboutAction = QAction(QIcon('res/img/about.png'), 'A&bout', self, statusTip="Displays info about text editor", triggered=self.aboutHelp)

        # -----------------------------------------

        # Menus (add Actions)
        self.fileMenu = self.menuBar().addMenu("&File")

        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)

        self.editMenu = self.menuBar().addMenu("&Edit")

        self.editMenu.addAction(self.undoAction)
        self.editMenu.addAction(self.redoAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.cutAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.selectAllAction)

        self.helpMenu = self.menuBar().addMenu("&Help")

        self.helpMenu.addAction(self.aboutAction)

        # -----------------------------------------

        # Toolbar
        self.mainToolBar = self.addToolBar('Main')

        self.mainToolBar.addAction(self.newAction)
        self.mainToolBar.addAction(self.openAction)
        self.mainToolBar.addAction(self.saveAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.cutAction)
        self.mainToolBar.addAction(self.copyAction)
        self.mainToolBar.addAction(self.pasteAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.undoAction)
        self.mainToolBar.addAction(self.redoAction)

        # -----------------------------------------

        # Statusbar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Ready', 10000)

        # -----------------------------------------

        self.show()

    # -----------------------------------------

    # Functions (Slots called when the Menu Actions are triggered)
    def newFile(self):
        # TODO Qt Menu Actions
        pass

    def openFile(self):
        # TODO Qt Menu Actions
        pass

    def saveFile(self):
        # TODO Qt Menu Actions
        pass

    def exitFile(self):
        # TODO Qt Menu Actions
        pass

    def aboutHelp(self):
        QMessageBox.about(self, "About Simple Text Editor", "A Simple Text Editor where you can edit and save files")


def createGuiQtTextEditor():
    # Application
    app = QApplication(sys.argv)

    # instance
    mainWindow = MyQMainWindow()

    app.exec_()
    # sys.exit()


# -------------------------------------------------------------------------------------------

"""
Kivy
https://kivy.org/
https://github.com/kivy/kivy
https://kivy.org/docs/
https://media.readthedocs.org/pdf/kivy/latest/kivy.pdf

Kivy can be run by QPython on Android Devices and Deployed using Buildozer VM from Kivy Website (create *.apk):
- put code in file name 'main.py'
- include the next line as a comment in your script for QPython:
#qpy:kivy

Kivy Sister-Projects:
https://github.com/kivy/buildozer
https://github.com/kivy/python-for-android
https://github.com/kivy/kivy-ios
https://github.com/kivy/kivy-designer
https://github.com/kivy-garden
https://kivy.org/docs/api-kivy.garden.html
https://github.com/kivy/kivent
https://github.com/chozabu/KivEntEd
https://chipmunk-physics.net/forum/viewtopic.php?t=3757
"""
from kivy.app import App
from kivy.lang import Builder
# UI Widgets
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar


# Kivy using objects to create widgets
class KivyApp(App):
    def build(self):
        return Button(text="Hello Kivy")


# Kivy using KV-language to create widget
# embedded string (or separated file *.kv)
Builder.load_string('''
<MyInterface>:
    orientation: "vertical"

    Label:
        text: "Hello Kivy"

    BoxLayout:
        orientation: 'vertical'
        TextInput:
            id: variable
            hint_text: "Enter your username"
        MyButton:
            user_input: variable.text
            text: "Attack"
            on_release: self.do_action()

    Label:

    BoxLayout:
        TextInput:
            size_hint: (0.5, 0.5)
            id: variable2
            hint_text: "Enter your password"
            password: True
        MyButton2:
            size_hint: (0.5, 0.5)
            user_input2: variable2.text
            text: "Write to SD"
            on_release: self.do_action()

    Label:
        text: "For educational purpose only, use on your own risk!"

''')


class MyInterface(BoxLayout):
    pass


class MyButton(Button):
    def progbar(self):
        pb = ProgressBar()
        popup = Popup(title='Brute Forcing ...', content=pb, size_hint=(0.7, 0.3))
        popup.open()
        # update ProgressBar in Loop
        pb.value = 25

    def do_action(self, *args):
        threading.Thread(target=self.progbar).start()
        print('log from Kivy')
        return


class MyButton2(Button):
    def do_action(self, *args):
        try:
            file = open("/mnt/extSdCard/test.txt", 'w')
            file.write(self.user_input2)
        except:
            pass
        return


class KivyApp2(App):
    def build(self):
        return MyInterface()


def createGuiKivy():
    #app = KivyApp()  # instance
    app = KivyApp2()  # instance
    app.run()


# -------------------------------------------------------------------------------------------
# TUI - Text User Interface
# CUI - Commandline User Interface
# CLI - Commandline Interface
# -------------------------------------------------------------------------------------------

"""
TUI
Text User Interface, Terminal User Interface
@see oterm, ollmcp for ollama (as examples for modern TUI)

Textual (based on Textualize Rich)
https://textual.textualize.io/

Rich
https://rich.readthedocs.io/

Typer (from FastAPI)
https://typer.tiangolo.com/

@see ASCII-Art
"""

# Textual / Textualize Rich TUI Application
from textual.app import App, ComposeResult
from textual.widgets import Static, Footer, Header, Label

class TuiApp(App):
    """ TUI Application using Textualize Rich
    """
    def compose(self) -> ComposeResult:
        """ Compose the TUI Application
        """
        yield Header()
        yield Footer()
        yield Label("Hello TUI Application using Textualize Rich!")
        # Add a Static widget with the text
        #yield Static("")
    

    def build(self):
        return tui()


def tui():
    """ Text User Interface
    """
    effectTTE("Mads, heute geht es um 21:00 Uhr in deiner Zeitzone ins Bett!\nUnd vorher Zähne putzen nicht vergessen!")

    app = TuiApp()
    app.run()  # run the TUI Application


# -----------------------------------------
# Rich
# https://rich.readthedocs.io/
# https://youtu.be/NIyljVEcJKw?si=1FuFSmqwHEJk71v7 (Tutorial)

# test Rich in the Terminal:
# python -m rich

# pretty print
# from rich import print as rprint

# rich for iPython and Jupyter Notebooks
# from rich import pretty
# pretty.install()

# from rich import inspect
# inspect(object)

# Console class and Logging
# from rich.console import Console
# console = Console()
# console.print("Hello, [bold magenta]World[/bold magenta]!", justify="center")
# from rich.traceback import install
# install(show_locals=True)
# console.log("This is a log message with [bold]bold[/bold] text and [italic]italic[/italic] text.", style="info")


# -----------------------------------------
# Typer
# (from FastAPI)
# https://typer.tiangolo.com/


# -----------------------------------------
# TerminalTextEffects (TTE)
# https://chrisbuilds.github.io/terminaltexteffects/
# https://chrisbuilds.github.io/terminaltexteffects/showroom/

from terminaltexteffects.effects.effect_blackhole import Blackhole

def effectTTE(text):
    """ Termial Text Effects"""
    effect = Blackhole(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)


# -------------------------------------------------------------------------------------------

"""
CUI
Commandline User Interface

CLI
Commandline Interface
https://en.wikipedia.org/wiki/Command-line_interface


# Terminal (VT100 Emulation):
# https://de.wikipedia.org/wiki/ANSI-Escapesequenz
# https://de.wikipedia.org/wiki/Terminalemulation
"""

"""
# Colorama
# https://pypi.python.org/pypi/colorama
#from colorama import init as coloramainit
#from colorama import Fore, Back, Style
#
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
#
# FOREGROUND:
# ESC [ 30 m      # black
# ESC [ 31 m      # red
# ESC [ 32 m      # green
# ESC [ 33 m      # yellow
# ESC [ 34 m      # blue
# ESC [ 35 m      # magenta
# ESC [ 36 m      # cyan
# ESC [ 37 m      # white
# ESC [ 39 m      # reset
#
# BACKGROUND:
# ESC [ 40 m      # black
# ...
# MULTIPLE PARAMS:
# ESC [ 36 ; 45 ; 1 m
#
# Examples:
# init()
# print('\033[31m' + 'some red text')
# print('\033[39m') # reset to default color
# print(Fore.RED + 'some red text' + Fore.RESET)
# print(Style.RESET_ALL) # back to normal
"""

"""
# Termcolor
# https://pypi.python.org/pypi/termcolor
#
# Text colors: grey, red, green, yellow, blue, magenta, cyan, white
# Text highlights: on_grey, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white
# Attributes: bold, dark, underline, blink, reverse, concealed
#
# Examples:
# print(colored('Hello, World!', 'red', attrs=['reverse', 'blink']))
# cprint('Hello, World!', 'green', 'on_red')
"""
from termcolor import colored, cprint

"""
# ASCII-Art:
# Leetspeak
# https://de.wikipedia.org/wiki/Leetspeak
# http://www.1337.me/
"""

"""
# FIGlet
# https://pypi.python.org/pypi/pyfiglet
# https://github.com/pwaller/pyfiglet
# http://www.figlet.org/
# fonts: lean, mini, banner
# favorite fonts: alligator2, poison, cosmic, chunky, eftiwater, isometric2, larry3d, letters, nipples, ntgreek, rectangles, shadow, slant, speed
"""
from pyfiglet import Figlet


def banner():
    #print "\n********************************"
    #print "*  *"
    #print "********************************"

    f = Figlet(font='cosmic')  # fonts: alligator2, poison, cosmic, chunky, eftiwater, isometric2, larry3d, letters, nipples, ntgreek, rectangles, shadow, slant, speed
    print('\033[34m')
    print(f.renderText('Totman'))
    print('\033[39m')

    # termcolor
    #cprint('[  *  ] Hello World!', 'red')
    #print('[  ' + colored('*', 'red') + '  ] Hello termcolor')  # use termcolor function colored()
    #print('[  \033[31m*\033[39m  ] Hello VT100')                # use CSI Escape Sequence directly


def usage():
    """ Print commandline usage
    Invoked if wrong number or type of arguments
    :return:
    """

    print("Usage: ")
    print("    -h: help (this message)")
    print("example: ")  # TODO usage() example


def cui():
    """ Commandline User Interface
    """

    """
    printf()-like output:
    # @see http://www.python-kurs.eu/python3_formatierte_ausgabe.php

    print("You typed", c)
    print("You typed %s" % (c))
    print("You typed {}".format(c))

    # f-srings (@since Python 3.6):
    # https://docs.python.org/3/reference/lexical_analysis.html#f-strings
    print(f"You typed {c}")
    """

    banner()

    #usage()

    # CUI
    print("Type '1' for Tk-GUI")
    print("Type '2' for Qt-GUI Editor")
    print("Type '3' for Kivy App")
    print("Type '4' for Pygame OpenGL Canvas")
    print("Type '5' for Qt-GUI Simple")
    print("Type '6' for TUI (Text / Terminal User Interface)")
    print("Type '0' to exit")

    while True:
        c = input(">> ")

        if '1' in c:
            createGuiTk()
        elif '2' in c:
            createGuiQtTextEditor()
        elif '3' in c:
            createGuiKivy()
        elif '4' in c:
            createCanvasWithPygame()
        elif '5' in c:
            createGuiQtSimple()
        elif '6' in c:
            tui()
        elif '0' in c:
            sys.exit(0)
        else:
            pass


# -------------------------------------------------------------------------------------------

def main(args):
    # -----------------------------------------
    # command line 
    cui()
    #tui()
    # -----------------------------------------
    # OpenGL
    #createCanvasWithPygame()
    # -----------------------------------------
    # GUI
    #createGuiTk()
    #createGuiQtSimple()
    #createGuiQtTextEditor()
    #createGuiKivy()
    # -----------------------------------------
    # Web
    #flask/htdocs/main.py       # ???
    # -----------------------------------------


# -------------------------------------------------------------------------------------------

# code entry point
if __name__ == "__main__":

    try:
        # parse commandline arguments
        args = sys.argv[1:]

        """
        # manually parse sys.argv[1:]
        if len(sys.argv) < 1:
            usage()
            sys.exit()

        # example
        try:
            (url, username, password) = sys.argv[1:]
        except ValueError:
            usage()

        # ---------------------------------------------------

        # optargs (C-Style)
        try:
            opts, args = getopt.getopt(sys.argv, "w:f:t:c:")
        except getopt.GetoptError:
            print("Error en arguments")
            sys.exit()
        hidecode = 000
        for opt, arg in opts:
            if opt == '-w':
                url = arg
            elif opt == '-f':
                dict = arg
            elif opt == '-t':
                threads = arg
            elif opt == '-c':
                hidecode = arg

        # ---------------------------------------------------

        # argparse
        parser = argparse.ArgumentParser(description='WebScraper url')
        parser.add_argument('--url', action="store", dest="url", required=True)
        args = parser.parse_args()

        """

        # start application
        DEBUG = 1
        # logging TODO
        timestart = time.time() #time.clock()

        main(args)

    except KeyboardInterrupt:
        print(sys.argv[0] + "interrupted by user, killing all threads!")
