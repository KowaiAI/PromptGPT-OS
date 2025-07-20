"""
# PromptGPT OS - Navigation Management System
# Developed by: https://github.com/KowaiAI
# Copyright (c) 2025 KowaiAI. All rights reserved.
# 
# This file contains proprietary navigation and user interface code.
# Unauthorized copying, modification, or distribution is prohibited.
# 
# Watermark: PROMPTGPT_OS_KOWAI_AI_2025_NAV_CORE
"""

from rich.console import Console
from rich.prompt import Prompt
import re

console = Console()

class NavigationHandler:
    """Handles navigation and user input validation"""
    
    def __init__(self):
        self.navigation_commands = {
            'back': 'Go to previous page',
            'home': 'Return to main menu', 
            'restart': 'Restart current questionnaire',
            'quit': 'Exit application',
            'next': 'Go to next question',
            'skip': 'Skip this question',
            'save': 'Save current prompt',
            'help': 'Show navigation help'
        }
    
    def validate_choice(self, choice, valid_choices):
        """Validate user choice against valid options"""
        if not choice:
            return False
        
        choice = choice.lower().strip()
        return choice in [opt.lower() for opt in valid_choices]
    
    def parse_navigation_command(self, user_input):
        """Parse user input for navigation commands"""
        if not user_input:
            return None
        
        user_input = user_input.lower().strip()
        
        if user_input in self.navigation_commands:
            return user_input
        
        # Handle shortcuts
        shortcuts = {
            'b': 'back',
            'h': 'home',
            'r': 'restart', 
            'q': 'quit',
            'n': 'next',
            's': 'save',
            'sk': 'skip',
            '?': 'help'
        }
        
        return shortcuts.get(user_input, None)
    
    def sanitize_input(self, user_input):
        """Sanitize user input for safety"""
        if not user_input:
            return ""
        
        # Remove potentially harmful characters
        sanitized = re.sub(r'[<>"\']', '', str(user_input))
        # Limit length
        return sanitized[:1000].strip()
    
    def get_user_choice(self, prompt_text, valid_choices=None, allow_empty=False, show_skip=False):
        """Get validated user choice with navigation support"""
        # Add skip option if enabled
        if show_skip:
            prompt_text += " | Type 'skip' to skip this question"
        
        while True:
            try:
                user_input = Prompt.ask(prompt_text, default="" if allow_empty else None)
                
                if not user_input and allow_empty:
                    return ""
                
                # Check for navigation commands first
                nav_command = self.parse_navigation_command(user_input)
                if nav_command:
                    if nav_command == 'help':
                        self.show_navigation_help()
                        continue
                    return nav_command
                
                # Validate against valid choices if provided
                if valid_choices and not self.validate_choice(user_input, valid_choices):
                    console.print(f"[red]Invalid choice. Please select from: {', '.join(valid_choices)}[/red]")
                    continue
                
                return self.sanitize_input(user_input)
                
            except KeyboardInterrupt:
                return "quit"
            except Exception as e:
                console.print(f"[red]Input error: {str(e)}[/red]")
                continue
    
    def show_navigation_help(self):
        """Display available navigation commands"""
        help_text = "\n[bold cyan]Available Navigation Commands:[/bold cyan]\n"
        for cmd, desc in self.navigation_commands.items():
            help_text += f"  [yellow]{cmd}[/yellow] - {desc}\n"
        
        console.print(help_text)
    
    def confirm_action(self, message, default=False):
        """Get user confirmation for actions"""
        try:
            from rich.prompt import Confirm
            return Confirm.ask(message, default=default)
        except KeyboardInterrupt:
            return False
        except Exception:
            return default
