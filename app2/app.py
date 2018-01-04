#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Alternative Shebangs:
# #!/usr/bin/env python3
# don't use:
# #!/usr/bin/python
# #!/usr/local/bin/python
# #!/bin/python

"""
# Python 3 and 2 compatibility (these imports must be in the first place):
# https://docs.python.org/2.7/howto/pyporting.html
# http://python-future.org/
#
# https://docs.python.org/2/library/__future__.html
# https://docs.python.org/2/library/future_builtins.html
# https://docs.python.org/2/library/__builtin__.html
#
# https://docs.python.org/3/library/builtins.html
# https://docs.python.org/3/library/__future__.html
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import nested_scopes
from __future__ import generators
from __future__ import with_statement
"""
from __future__ import print_function

"""
Author: Thorsten Mauthe, t.mauthe@gmx.de
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
__version__ = 0.01
__description__ = ''

# -------------------------------------------------------------------------------------------

"""
### Python Distributions:
#
## Anaconda
# https://www.anaconda.com/what-is-anaconda/
## Enthought
# https://www.enthought.com/product/enthought-python-distribution/
## ActivePython
# https://www.activestate.com/activepython
## Python.org
# https://www.python.org/

# -------------------------------------------------------------------------------------------

### Virtual Environments:
# https://conda.io/docs/commands.html#conda-vs-pip-vs-virtualenv-commands

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

# -------------------------------------------------------------------------------------------

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
#
#
## pip, PyPI (Python Package Index)
# https://pip.pypa.io/en/stable/
# pip search $SEARCH_TERM
# pip list
# # create requirements file
# pip freeze
#
# pip install <package>
# pip install --upgrade $PACKAGE_NAME
# pip uninstall $PACKAGE_NAME
#
#
## setuptools
## easy_install
## distutils

# -------------------------------------------------------------------------------------------

### IDEs:
# https://wiki.python.org/moin/IntegratedDevelopmentEnvironments
# https://www.pythoncentral.io/comparison-of-python-ides-development/

## IDLE
## IPython | Jupyter Notebook
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
## Atom Editor


### PyInstaller:
# http://www.pyinstaller.org/, https://pyinstaller.readthedocs.io/en/stable/, https://github.com/pyinstaller/pyinstaller
# uses:
# (pefile)
# (PyWin32: http://sourceforge.net/projects/pywin32/files/)
# UDX
# PyCrypto: https://www.dlitz.net/software/pycrypto/

# Installation:
# pip install pyinstaller
# on error: pip install future --upgrade

# Usage: https://pyinstaller.readthedocs.io/en/stable/usage.html
# pyinstaller --onefile --windowed --icon=res/icon.ICO /path/to/yourscript.py


### py2exe:
# http://www.py2exe.org/
# http://www.py2exe.org/index.cgi/Tutorial
#
# create a setup.py file
from distutils.core import setup
import py2exe
setup(console=['hello.py'])
# run the file in DOS Command Window
python setup.py py2exe


### Installer Builders
## NSIS
# http://nsis.sourceforge.net/Main_Page
## Inno Setup
# http://www.jrsoftware.org/isinfo.php

"""

# -------------------------------------------------------------------------------------------

# pip install -r requirements.txt
# create file with: 'conda list --export' or 'pip freeze'

# -------------------------

import sys
import os
import os.path
import time
import datetime

import argparse
import getopt

# -------------------------

"""
# Software Engineering, TDD:
# http://pythontesting.net/start-here
# pytest
# unittest
# http://pythontesting.net/framework/unittest/unittest-introduction/
# nose
# http://pythontesting.net/framework/nose/nose-introduction/
"""
#import unittest

"""
# Logging:
# https://docs.python.org/2/howto/logging.html
# https://docs.python.org/2/library/logging.html
"""
import logging

# -------------------------

"""
# Terminal (VT100 Emulation):
# https://de.wikipedia.org/wiki/ANSI-Escapesequenz
# https://de.wikipedia.org/wiki/Terminalemulation

# --------

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

# --------

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
# FIGlet
# https://pypi.python.org/pypi/pyfiglet
# https://github.com/pwaller/pyfiglet
# http://www.figlet.org/
# fonts: lean, mini, banner
# favorite fonts: alligator2, poison, cosmic, chunky, eftiwater, isometric2, larry3d, letters, nipples, ntgreek, rectangles, shadow, slant, speed

# --------

# ASCII-Art:
# Leetspeak
# https://de.wikipedia.org/wiki/Leetspeak
# http://www.1337.me/
"""
from pyfiglet import Figlet

# -------------------------

# WebScraping:
import socket
import httplib
import htmllib
import urllib
import urllib2
import requests
from lxml import etree
from io import StringIO, BytesIO
from base64 import b64encode
from bs4 import BeautifulSoup
#from html.parser import HTMLParser

import webbrowser
import mechanize
from selenium import webdriver

# Scrapy
# https://scrapy.org/
# https://github.com/scrapy/scrapy

# -------------------------

# Parser | Fileformats:
import re
import json
import csv

# -------------------------

# Webdesign:
# Flask
# Django

# DB | CRUD:
# SQlite
# MySQL
# SQLAlchemy

# -------------------------

# GUI:

# Tkinter
from Tkinter import *  # Python 2
#from tkinter import * # Python 3
# Core Widgets:
# Label, Button, Entry, Checkbutton, Radiobutton, Spinbox, Listbox, Text, Canvas, Bitmap, Image
# Toplevel, Frame, Menu, Menubutton, Scrollbar, OptionMenu, LabelFrame, Message, PanedWindow, Scale
# Geometry Managers:
# pack, grid, place

# Kivy
# https://kivy.org/
#from kivy.app import App
#from kivy.uix.button import Button

# PyQt4
from PyQt4.QtGui import *
#import PyQt4.QtCore
# PySide
#from PySide.QtCore import Qt
#from PySide.QtGui import QApplication, QLabel
#from PySide.QtSql import *

# -------------------------

# Game | Creative Coding | Physical Computing | IoT:

# Pygame (OpenGL, Canvas, MIDI, Sound)
# https://www.pygame.org/docs/
# https://inventwithpython.com/pygame/chapters/
# pip install pygame --user
import pygame

# pybox2d (Physics)
# https://github.com/pybox2d/pybox2d/wiki/manual
# conda install -c https://conda.anaconda.org/kne pybox2d

# pylibpd (Pure Data), pyaudio (PortAudio)

# pyfluidsynth (Soundfont Synthesizer, sf2)

# cwiid (Wiimote)
# RPi.GPIO (Raspberry Pi)
# WiringPi

# -------------------------

# Image Processing:

# PIL
#import PIL

# OpenCV
#import cv2

# -------------------------

# Pentesting:
# https://github.com/dloss/python-pentest-tools

# Scapy

# PeePDP
# http://eternal-todo.com/tools/peepdf-pdf-analysis-tool

# Cryptography
# PyCrypto: https://www.dlitz.net/software/pycrypto/

# -------------------------

# HPC (High Performance Computing):

# Parallel Python: threading, processes, asynchronous IO (Twisted), asyncio (Python 3)
from threading import Thread

# Cython
# Numba
# SWIG (Wrapper, Bindings)

# -------------------------

# Data Science, Maschine Learning, Deep Learning, Datamining:

# Anaconda (conda)
# IPython/ Jupyter Notebook (IPython --pylab)

# Numpy, SciPy, Pandas

# Scikit-learn (sklearn), Theano, Tensorflow

# Matplotlib

# Bokeh (interactive graphics)
# https://bokeh.pydata.org/en/latest/

# NLTK (Natural Languages Toolkit)
# http://www.nltk.org/

# -------------------------------------------------------------------------------------------

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

def createGuiTk():
    root = Tk()

    # Widgets
    label = Label(root, text = "Hello World!")
    # Geometry Managers: pack, grid, place
    label.pack()

    root.mainloop()

# -----------------------------------------

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initGUI()


    def initGUI(self):
        # Window (QMainWindow, QWidget)
        self.setWindowTitle("A Simple Text Editor")
        self.setWindowIcon(QIcon('appicon.png'))
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
        self.newAction = QAction( QIcon('img/new.png'), '&New', self, shortcut = QKeySequence.New, statusTip = "Create a New File", triggered = self.newFile)
        self.openAction = QAction( QIcon('img/open.png'), 'O&pen', self, shortcut = QKeySequence.Open, statusTip = "Open an existing file", triggered = self.openFile)
        self.saveAction = QAction( QIcon('img/save.png'), '&Save', self, shortcut = QKeySequence.Save, statusTip = "Save the current file to disk", triggered = self.saveFile)
        self.exitAction = QAction( QIcon('img/exit.png'), 'E&xit', self, shortcut = "Ctrl+Q", statusTip = "Exit the Application", triggered = self.exitFile)
        self.cutAction = QAction( QIcon('img/cut.png'), 'C&ut', self, shortcut = QKeySequence.Cut, statusTip = "Cut the current selection to clipboard", triggered = self.textEdit.cut)
        self.copyAction = QAction( QIcon('img/copy.png'), 'C&opy', self, shortcut = QKeySequence.Copy, statusTip = "Copy the current selection to clipboard", triggered = self.textEdit.copy)
        self.pasteAction = QAction( QIcon('img/paste.png'), '&Paste', self, shortcut = QKeySequence.Paste, statusTip = "Paste the clipboard's content in current location", triggered = self.textEdit.paste)
        self.selectAllAction = QAction( QIcon('img/selectAll.png'), 'Select All', self, statusTip = "Select All", triggered = self.textEdit.selectAll)
        self.redoAction = QAction( QIcon('img/redo.png'),'Redo', self, shortcut = QKeySequence.Redo, statusTip = "Redo previous action", triggered = self.textEdit.redo)
        self.undoAction = QAction( QIcon('img/undo.png'),'Undo', self, shortcut = QKeySequence.Undo, statusTip = "Undo previous action", triggered = self.textEdit.undo)
        self.aboutAction = QAction( QIcon('img/about.png'), 'A&bout', self, statusTip = "Displays info about text editor", triggered = self.aboutHelp)

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
        pass

    def openFile(self):
        pass

    def saveFile(self):
        pass

    def exitFile(self):
        pass

    def aboutHelp(self):
        QMessageBox.about(self, "About Simple Text Editor", "A Simple Text Editor where you can edit and save files")


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
    sys.exit()


def createGuiQtTextEditor():
    # Application
    app = QApplication(sys.argv)

    # class s.o.
    mainWindow = MainWindow()

    app.exec_()
    sys.exit()

# -----------------------------------------

def createCanvasWithPygame():
    """
    global FPSCLOCK, DISPLAYSURF

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    # set up the window
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('PyGame')


    # load images
    img = pygame.image.load('cat.png')
    #if img.get_size() != (IMAGESIZE, IMAGESIZE):
    #    img = pygame.transform.smoothscale(img, (IMAGESIZE, IMAGESIZE))


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


    # the main game loop
    while True:
        DISPLAYSURF.fill(BGCOLOR)

        # draw images
        x = 0
        y = 0
        DISPLAYSURF.blit(img, (x, y))


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


        # event handling loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    # you could display a confirmation window
                    pygame.quit()
                    sys.exit()
                elif event.key == K_BACKSPACE:
                    # leave function
                    return
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    # move UP
                elif event.key == K_a:
                    # move LEFT
                elif event.key == K_d:
                    # move RIGHT
                elif event.key == K_s:
                    # move DOWN
                elif event.key == K_e:
                    # change tool
            elif event.type == MOUSEBUTTONUP:
                if event.pos == (lastMouseDownX, lastMouseDownY):
                    # This event is a mouse click, not the end of a mouse drag.
                    x, y = event.pos
                    # check for clicks on buttons
                    if pygame.Rect(74, 16, 111, 30).collidepoint(x, y):
                        # play sound
                        snd.play()
                else:
                    # this is the end of a mouse drag

            elif event.type == MOUSEBUTTONDOWN:
                # this is the start of a mouse click or mouse drag
                lastMouseDownX, lastMouseDownY = event.pos
            elif event.type == pygame.midi.MIDIIN:
                # @see pygame.midi.midis2events()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

    """

# -------------------------------------------------------------------------------------------

def banner():
    #print "\n********************************"
    #print "*  *" # TODO banner()
    #print "********************************"

    f = Figlet(font='cosmic')  # fonts: alligator2, poison, cosmic, chunky, eftiwater, isometric2, larry3d, letters, nipples, ntgreek, rectangles, shadow, slant, speed
    print('\033[34m')
    print(f.renderText('Totman'))
    print('\033[39m')

    # termcolor
    cprint('[  *  ] Hello World!', 'red')
    print('[  ' + colored('*', 'red') + '  ] Hello termcolor')  # use termcolor function colored()
    print('[  \033[31m*\033[39m  ] Hello VT100')                # use CSI Escape Sequence directly


def usage():
    print("Usage: ")
    print("    -h: help (this message)")
    print("example: ")  # TODO usage() example


def cui():
    """ Commandline User Interface
    """

    banner()

    c = raw_input(">> ")

    # @see http://www.python-kurs.eu/python3_formatierte_ausgabe.php
    print("You typed", c)
    print("You typed %s" % (c))
    print("You typed {}".format(c))


def main(args):
    #createGuiTk()
    #createGuiQtSimple()
    #createGuiQtTextEditor()
    cui()

# -------------------------------------------------------------------------------------------

# code entry point
if __name__ == "__main__":

    # parse sys.argv
    try:

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
        """

        """
        # argparse
        parser = argparse.ArgumentParser(description='WebScraper url')
        parser.add_argument('--url', action="store", dest="url", required=True)
        args = parser.parse_args()
        """

        """
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
        """

        # commandline arguments
        args = sys.argv[1:]

        # start application
        DEBUG = 1
        timestart = time.time() #time.clock()

        main(args)

    except KeyboardInterrupt:
        print(sys.argv[0] + "interrupted by user, killing all threads!")

