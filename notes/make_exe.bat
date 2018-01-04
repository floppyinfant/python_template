@echo off
cls

pyinstaller --onefile --windowed --icon=res\icon_python.ico --name="MyPythonApp" src\mytemplate\template.py
REM --console --version-file="" --noupx

REM References:
REM https://pyinstaller.readthedocs.io/en/stable/usage.html
REM https://de.wikipedia.org/wiki/BAT-Datei

REM echo Taste druecken zum Beenden
REM pause > nul
REM exit
