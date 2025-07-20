# PromptGPT OS - Installation Guide

## Quick Start

### Method 1: Using requirements.txt (Recommended)
```bash
pip install -r requirements.txt
python main.py
```

### Method 2: Automated Installation Script (Linux/macOS)
```bash
chmod +x install.sh
./install.sh
```

### Method 3: Production Launcher
```bash
python run_promptgpt.py
```

## System Requirements

- Python 3.6 or higher
- pip (Python package installer)
- Terminal/Command Prompt access

## Dependencies

The `requirements.txt` file includes:

### Required Dependencies
- `rich>=13.0.0` - Terminal UI framework (Required)

### Optional Dependencies  
- `keyboard>=0.13.5` - Keyboard input handling (Optional - graceful fallback)
- `pyperclip>=1.8.0` - Clipboard functionality (Optional - graceful fallback)

## Installation Methods

### Windows
```cmd
pip install -r requirements.txt
python main.py
```

### Linux/macOS
```bash
pip3 install -r requirements.txt
python3 main.py
```

### Manual Dependency Installation
If `requirements.txt` installation fails:
```bash
pip install rich
pip install keyboard pyperclip  # Optional
python main.py
```

## Verification

Run system check to verify installation:
```bash
python check_system.py
```

## Troubleshooting

### Missing Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Permission Issues (Linux/macOS)
```bash
pip3 install --user -r requirements.txt
python3 main.py
```

### Virtual Environment (Recommended for Development)
```bash
python -m venv promptgpt_env
source promptgpt_env/bin/activate  # Linux/macOS
# promptgpt_env\Scripts\activate  # Windows
pip install -r requirements.txt
python main.py
```

## Post-Installation

After successful installation, you can start the application with any of these commands:

- `python main.py` - Direct execution
- `python run_promptgpt.py` - Production launcher with system checks
- `./install.sh && python main.py` - Full installation and launch (Linux/macOS)

The application will start immediately without requiring authentication and display the main menu for creating AI content prompts.