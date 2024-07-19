# Code Review System

## Overview
This project is a code review system that leverages the Gemini-Pro API to automatically review and provide feedback on code submissions from public GitHub repositories. The system identifies potential issues, suggests improvements, and ensures code quality and consistency.

## Features   sim
- Integrate with Gemini-Pro API for code analysis.
- Supports multiple programming languages (Python, JavaScript, Java).
- Provides detailed review reports highlighting:
  - Line-by-line comments.
  - Overall summary of code quality.
  - issues with severity levels (Low, Medium, High), and overall
  - Suggestions for improvement.

## step1  create environment in the folder of project make sure anaconda install your system 
   - set directory  of folder in anaconda propmpt terminal command use
   - conda create -n env_name python=3.10.14 -y
   - conda activate env_name
   - pip install -r requirements.txt 
   if not work requirements file  after install requirements.txt 
   ## you have to install below library
   - pip install Flask 
   - pip install python-dotenv
   - pip install langchain_google_genai
## run  command terminal
   - python app.py 

you get a url  http://127.0.0.1:9000 in terminal after    command  run python app.py command.










