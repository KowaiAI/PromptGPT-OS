@echo off
echo 🚀 Installing PromptGPT OS...
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found. Please install Python 3.6+ first.
    pause
    exit /b 1
)

echo ✓ Python found
echo 📦 Installing dependencies...

pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

REM Create output directory
if not exist "generated_prompts" mkdir generated_prompts

echo.
echo 🎉 Installation complete!
echo.
echo To run PromptGPT OS:
echo   python main.py
echo.
echo For help, see README.md
pause
