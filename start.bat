@echo off
setlocal

REM Set the name of your virtual environment folder
set VENV_DIR=.venv

REM Check if the virtual environment exists
if not exist %VENV_DIR% (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
)

REM Check if the virtual environment is already activated
if "%VIRTUAL_ENV%"=="" (
    echo Activating virtual environment...
    call %VENV_DIR%\Scripts\activate.bat
) else (
    echo Virtual environment already activated.
)

REM Always check and install missing requirements
@REM pip install --upgrade pip
pip install -r requirements.txt

REM Run the FastAPI project
uvicorn app.main:app --reload 