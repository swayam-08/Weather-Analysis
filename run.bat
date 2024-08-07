@echo off
REM Set the path to the Python executable if it's not in the system PATH
set PYTHON_EXE=python

REM Run data cleaning script
echo Running data cleaning script...
%PYTHON_EXE% scripts\data_cleaning.py
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%

REM Run data analysis script
echo Running data analysis script...
%PYTHON_EXE% scripts\data_analysis.py
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%

REM Run data visualization script
echo Running data visualization script...
%PYTHON_EXE% scripts\data_visualization.py
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%

echo All scripts completed successfully.