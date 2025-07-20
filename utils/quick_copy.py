"""
Quick Copy Utility for PromptGPT OS
Provides instant clipboard copying with hotkeys
"""

import threading
from utils.clipboard_manager import ClipboardManager
from rich.console import Console

console = Console()

class QuickCopy:
    """Handles quick copy operations for generated prompts"""
    
    def __init__(self):
        self.clipboard_manager = ClipboardManager()
        self.last_prompt = None
        self.last_category = None
        self.last_subcategory = None
    
    def set_current_prompt(self, prompt, category, subcategory):
        """Set the current prompt for quick copying"""
        self.last_prompt = prompt
        self.last_category = category
        self.last_subcategory = subcategory
    
    def quick_copy_prompt_only(self):
        """Copy just the prompt content"""
        if not self.last_prompt:
            console.print("[red]No prompt available to copy[/red]")
            return False
        
        return self.clipboard_manager.copy_prompt_only(self.last_prompt)
    
    def quick_copy_with_metadata(self):
        """Copy prompt with metadata"""
        if not self.last_prompt:
            console.print("[red]No prompt available to copy[/red]")
            return False
        
        return self.clipboard_manager.copy_prompt_with_metadata(
            self.last_prompt, 
            self.last_category, 
            self.last_subcategory
        )
    
    def show_copy_options(self):
        """Show available copy options"""
        if not self.clipboard_manager.available:
            console.print("[yellow]Clipboard functionality not available on this system[/yellow]")
            return
        
        options_text = """
📋 Copy Options:
1. Copy prompt only (clean text)
2. Copy with metadata (category, source info)
        """
        console.print(options_text)
    
    def copy_with_choice(self, include_metadata=True):
        """Copy with user's choice of format"""
        if include_metadata:
            return self.quick_copy_with_metadata()
        else:
            return self.quick_copy_prompt_only()