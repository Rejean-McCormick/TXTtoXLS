@echo off
REM Enhanced Git Setup Script
REM This script initializes a Git repository, commits a file, and sets up a remote repository.

REM Step 1: Check for Git Installation
git --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Git is not installed. Please install Git from https://git-scm.com and try again.
    pause
    exit /b
)

REM Step 2: Check for a Python File in the Current Directory
set "pyfile="
for %%f in (*.py) do (
    set "pyfile=%%~nf"
    goto :found
)

REM If no Python file is found, exit
if "%pyfile%"=="" (
    echo No Python (.py) file found in the current directory. Please ensure there is a .py file and try again.
    pause
    exit /b
)

:found
echo Detected Python file: %pyfile%.py

REM Step 3: Initialize Git Repository
echo Initializing Git repository...
git init

REM Step 4: Add All Files to the Repository
echo Adding files to the repository...
git add .

REM Step 5: Commit Changes
echo Committing changes...
git commit -m "Initial commit" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Failed to commit. Make sure there are changes to commit.
    pause
    exit /b
)

REM Step 6: Configure Remote Repository
set "repository_url=https://github.com/your-username/%pyfile%"
echo Setting remote origin to: %repository_url%
git remote add origin %repository_url%

REM Step 7: Push Changes to Remote Repository
echo Pushing changes to remote repository...
git branch -M main
git push -u origin main

REM Final Step: Success Message
if %ERRORLEVEL% EQU 0 (
    echo Git repository setup completed successfully.
    echo Remote repository URL: %repository_url%
) else (
    echo Failed to push changes. Please check your remote repository setup.
)
pause
