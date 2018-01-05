@echo off
cls

pyinstaller ^
--clean ^
--onefile ^
--noconsole ^
--icon=res\icon.ico ^
--name="PythonApp" ^
src\app.py

REM https://de.wikipedia.org/wiki/BAT-Datei
REM
REM --upx-dir=C:\Users\A3000\Documents\TM\_dev\Python\PycharmProjects\pyinstaller\PyInstaller-3.2\upx ^
