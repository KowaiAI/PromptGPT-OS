#!/usr/bin/env python3
"""
PromptGPT OS Launcher
Production-ready launcher with system checks and error handling
"""

import sys
import os

def main():
    """Main launcher function with system checks"""
    
    # Add current directory to Python path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
    
    # Check Python version
    if sys.version_info < (3, 6):
        print("❌ Error: Python 3.6 or higher is required")
        print(f"   Current version: {sys.version}")
        sys.exit(1)
    
    # Try to import Rich first (required dependency)
    try:
        from rich.console import Console
        console = Console()
    except ImportError:
        print("❌ Error: 'rich' library is required but not installed")
        print("📋 Install with: pip install rich")
        sys.exit(1)
    
    # Check for data files
    required_files = [
        'data/questions.json',
        'data/templates.json',
        'config/settings.py'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        console.print("[red]❌ Missing required files:[/red]")
        for file_path in missing_files:
            console.print(f"   - {file_path}")
        console.print("\n[yellow]Please ensure all application files are present[/yellow]")
        sys.exit(1)
    
    # Create necessary directories
    directories = ['generated_prompts', 'custom_data']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    # Import and run the main application
    try:
        from main import PromptGPTOS
        
        # Clear screen and start application
        os.system('cls' if os.name == 'nt' else 'clear')
        
        app = PromptGPTOS()
        app.run()
        
    except KeyboardInterrupt:
        console.print("\n[yellow]👋 Application interrupted by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]❌ Application error: {e}[/red]")
        console.print("\n[dim]Run 'python check_system.py' for system diagnostics[/dim]")
        sys.exit(1)

if __name__ == "__main__":
    main()