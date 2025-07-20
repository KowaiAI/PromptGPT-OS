#!/usr/bin/env python3
"""
# PromptGPT OS - History Management System
# Developed by: https://github.com/KowaiAI
# Copyright (c) 2025 KowaiAI. All rights reserved.
# 
# This file contains proprietary history tracking and management code.
# Unauthorized copying, modification, or distribution is prohibited.
# 
# Watermark: PROMPTGPT_OS_KOWAI_AI_2025_HISTORY_CORE
"""

import json
import os
import time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.prompt import Prompt

console = Console()

class HistoryManager:
    """Manages prompt generation history with advanced tracking"""
    
    def __init__(self):
        self.history_file = "generated_prompts/prompt_history.json"
        self.max_history = 50  # Keep last 50 prompts
        self.ensure_history_file()
    
    def ensure_history_file(self):
        """Ensure history file and directory exist"""
        os.makedirs("generated_prompts", exist_ok=True)
        if not os.path.exists(self.history_file):
            self._save_history([])
    
    def _load_history(self):
        """Load prompt history from file"""
        try:
            with open(self.history_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _save_history(self, history):
        """Save prompt history to file"""
        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            console.print(f"[red]Error saving history: {e}[/red]")
    
    def add_to_history(self, prompt_content, category, subcategory, user_answers=None):
        """Add a new prompt to history"""
        history = self._load_history()
        
        # Create history entry
        entry = {
            'id': len(history) + 1,
            'content': prompt_content,
            'category': category,
            'subcategory': subcategory,
            'user_answers': user_answers or {},
            'created_at': datetime.now().isoformat(),
            'word_count': len(prompt_content.split()),
            'char_count': len(prompt_content)
        }
        
        # Add to beginning of list (most recent first)
        history.insert(0, entry)
        
        # Keep only the most recent entries
        if len(history) > self.max_history:
            history = history[:self.max_history]
        
        self._save_history(history)
        return entry['id']
    
    def get_recent_history(self, limit=10):
        """Get recent prompt history"""
        history = self._load_history()
        return history[:limit]
    
    def get_history_by_category(self, category, limit=10):
        """Get history filtered by category"""
        history = self._load_history()
        filtered = [entry for entry in history if entry['category'] == category]
        return filtered[:limit]
    
    def search_history(self, search_term, limit=10):
        """Search history by content or category"""
        history = self._load_history()
        search_term = search_term.lower()
        
        results = []
        for entry in history:
            if (search_term in entry['content'].lower() or 
                search_term in entry['category'].lower() or 
                search_term in entry['subcategory'].lower()):
                results.append(entry)
                if len(results) >= limit:
                    break
        
        return results
    
    def get_prompt_by_id(self, prompt_id):
        """Get specific prompt by ID"""
        history = self._load_history()
        for entry in history:
            if entry['id'] == prompt_id:
                return entry
        return None
    
    def delete_from_history(self, prompt_id):
        """Delete specific prompt from history"""
        history = self._load_history()
        history = [entry for entry in history if entry['id'] != prompt_id]
        self._save_history(history)
        return True
    
    def clear_history(self):
        """Clear all history"""
        self._save_history([])
        return True
    
    def get_history_stats(self):
        """Get comprehensive history statistics"""
        history = self._load_history()
        
        if not history:
            return {
                'total_prompts': 0,
                'categories_used': [],
                'avg_word_count': 0,
                'most_used_category': None,
                'recent_activity': []
            }
        
        # Calculate statistics
        categories = [entry['category'] for entry in history]
        category_counts = {}
        for cat in categories:
            category_counts[cat] = category_counts.get(cat, 0) + 1
        
        most_used = max(category_counts.items(), key=lambda x: x[1]) if category_counts else None
        avg_words = sum(entry['word_count'] for entry in history) / len(history)
        
        return {
            'total_prompts': len(history),
            'categories_used': list(set(categories)),
            'avg_word_count': round(avg_words, 1),
            'most_used_category': most_used[0] if most_used else None,
            'most_used_count': most_used[1] if most_used else 0,
            'recent_activity': history[:5]
        }
    
    def display_history_page(self):
        """Display interactive history page"""
        console.clear()
        
        # Header
        header_text = Text()
        header_text.append("📚 PROMPT HISTORY 📚", style="bold cyan")
        
        header_panel = Panel(
            header_text,
            border_style="cyan",
            padding=(1, 2)
        )
        console.print(header_panel)
        console.print()
        
        # Get recent history
        recent_history = self.get_recent_history(10)
        
        if not recent_history:
            console.print("[yellow]No prompt history found. Generate some prompts to see them here![/yellow]")
            console.print()
            input("Press Enter to return to main menu...")
            return
        
        # Display history table
        table = Table(title="Recent Prompts (Last 10)")
        table.add_column("ID", style="cyan", width=4)
        table.add_column("Category", style="magenta", width=12)
        table.add_column("Subcategory", style="blue", width=15)
        table.add_column("Preview", style="white", width=40)
        table.add_column("Created", style="green", width=12)
        table.add_column("Words", style="yellow", width=6)
        
        for entry in recent_history:
            # Format date
            created_date = datetime.fromisoformat(entry['created_at'])
            date_str = created_date.strftime("%m/%d %H:%M")
            
            # Create preview
            preview = entry['content'][:37] + "..." if len(entry['content']) > 40 else entry['content']
            
            table.add_row(
                str(entry['id']),
                entry['category'].title(),
                entry['subcategory'].title(),
                preview,
                date_str,
                str(entry['word_count'])
            )
        
        console.print(table)
        console.print()
        
        # Display statistics
        stats = self.get_history_stats()
        stats_text = f"""
📊 Statistics:
• Total Prompts: {stats['total_prompts']}
• Average Words: {stats['avg_word_count']}
• Most Used: {stats['most_used_category']} ({stats['most_used_count']} times)
• Categories: {len(stats['categories_used'])}
        """
        
        stats_panel = Panel(
            stats_text,
            title="[bold green]📈 HISTORY STATS[/bold green]",
            border_style="green",
            padding=(1, 2)
        )
        console.print(stats_panel)
        console.print()
        
        # Navigation options
        nav_text = Text()
        nav_text.append("🔍 ", style="bold blue")
        nav_text.append("VIEW", style="bold blue")
        nav_text.append(" | ", style="dim white")
        nav_text.append("📋 ", style="bold magenta")
        nav_text.append("COPY", style="bold magenta")
        nav_text.append(" | ", style="dim white")
        nav_text.append("🔎 ", style="bold yellow")
        nav_text.append("SEARCH", style="bold yellow")
        nav_text.append(" | ", style="dim white")
        nav_text.append("🗑️  ", style="bold red")
        nav_text.append("CLEAR", style="bold red")
        nav_text.append(" | ", style="dim white")
        nav_text.append("🏠 ", style="bold green")
        nav_text.append("HOME", style="bold green")
        
        console.print(nav_text)
        console.print()
        
        return self._handle_history_navigation(recent_history)
    
    def _handle_history_navigation(self, recent_history):
        """Handle history page navigation"""
        while True:
            choice = Prompt.ask(
                "[bold cyan]Choose action[/bold cyan]",
                choices=["view", "copy", "search", "clear", "home", "v", "c", "s", "cl", "h"],
                default="home"
            ).lower()
            
            if choice in ["home", "h"]:
                return "main_menu"
            
            elif choice in ["view", "v"]:
                return self._view_prompt_detail(recent_history)
            
            elif choice in ["copy", "c"]:
                return self._copy_from_history(recent_history)
            
            elif choice in ["search", "s"]:
                return self._search_history_interactive()
            
            elif choice in ["clear", "cl"]:
                if Prompt.ask("Clear all history? [y/N]", default="n").lower() == "y":
                    self.clear_history()
                    console.print("[green]✅ History cleared![/green]")
                    time.sleep(1)
                    return "main_menu"
    
    def _view_prompt_detail(self, recent_history):
        """View detailed prompt information"""
        try:
            prompt_id = int(Prompt.ask("Enter prompt ID to view"))
            entry = self.get_prompt_by_id(prompt_id)
            
            if not entry:
                console.print("[red]Prompt not found![/red]")
                time.sleep(1)
                return None
            
            # Display detailed view
            console.clear()
            
            detail_text = f"""
ID: {entry['id']}
Category: {entry['category'].title()} → {entry['subcategory'].title()}
Created: {datetime.fromisoformat(entry['created_at']).strftime('%Y-%m-%d %H:%M:%S')}
Word Count: {entry['word_count']} words
Character Count: {entry['char_count']} characters

CONTENT:
{entry['content']}
            """
            
            detail_panel = Panel(
                detail_text,
                title=f"[bold yellow]📝 PROMPT #{entry['id']} DETAILS[/bold yellow]",
                border_style="yellow",
                padding=(1, 2)
            )
            
            console.print(detail_panel)
            console.print()
            
            input("Press Enter to return to history...")
            return None
            
        except ValueError:
            console.print("[red]Invalid ID. Please enter a number.[/red]")
            time.sleep(1)
            return None
    
    def _copy_from_history(self, recent_history):
        """Copy prompt from history to clipboard"""
        try:
            from utils.clipboard_manager import ClipboardManager
            clipboard = ClipboardManager()
            
            prompt_id = int(Prompt.ask("Enter prompt ID to copy"))
            entry = self.get_prompt_by_id(prompt_id)
            
            if not entry:
                console.print("[red]Prompt not found![/red]")
                time.sleep(1)
                return None
            
            # Copy to clipboard
            success = clipboard.copy_prompt_only(entry['content'])
            if success:
                console.print(f"[green]✅ Prompt #{prompt_id} copied to clipboard![/green]")
            
            time.sleep(2)
            return None
            
        except ValueError:
            console.print("[red]Invalid ID. Please enter a number.[/red]")
            time.sleep(1)
            return None
        except ImportError:
            console.print("[red]Clipboard functionality not available![/red]")
            time.sleep(1)
            return None
    
    def _search_history_interactive(self):
        """Interactive history search"""
        search_term = Prompt.ask("Enter search term")
        results = self.search_history(search_term, 10)
        
        if not results:
            console.print(f"[yellow]No prompts found containing '{search_term}'[/yellow]")
            time.sleep(2)
            return None
        
        console.clear()
        console.print(f"[bold cyan]Search Results for '{search_term}':[/bold cyan]")
        console.print()
        
        # Display search results
        for i, entry in enumerate(results, 1):
            preview = entry['content'][:60] + "..." if len(entry['content']) > 60 else entry['content']
            console.print(f"[cyan]{entry['id']}.[/cyan] [{entry['category']}] {preview}")
        
        console.print()
        input("Press Enter to return to history...")
        return None