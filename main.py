#!/usr/bin/env python3
"""
# PromptGPT OS - Advanced AI Content Prompt Generator
# Developed by: https://github.com/KowaiAI
# Copyright (c) 2025 KowaiAI. All rights reserved.
# 
# This is the main application file for PromptGPT OS.
# Unauthorized copying, modification, or distribution is prohibited.
# 
# Watermark: PROMPTGPT_OS_KOWAI_AI_2025_MAIN_CORE
"""

import sys
import json
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.align import Align
import keyboard
import threading
import time
import pyperclip

from utils.navigation import NavigationHandler
from utils.prompt_generator import PromptGenerator
from utils.file_handler import FileHandler
from utils.settings_manager import SettingsManager
from utils.template_guide import show_template_guide
from utils.clipboard_manager import ClipboardManager
from utils.animations import AnimationManager, ProgressTracker
from utils.history_manager import HistoryManager
from ui.display import DisplayManager
from config.settings import COLORS, CATEGORIES, ASCII_HEADER

console = Console()
nav_handler = NavigationHandler()
prompt_gen = PromptGenerator()
file_handler = FileHandler()
settings_manager = SettingsManager()
display_manager = DisplayManager()
clipboard_manager = ClipboardManager()
animation_manager = AnimationManager()
progress_tracker = ProgressTracker()
history_manager = HistoryManager()

class PromptGPTOS:
    def __init__(self):
        self.current_page = "main_menu"
        self.user_answers = {}
        self.current_category = None
        self.current_subcategory = None
        self.question_index = 0
        self.hotkey_enabled = True
        self.custom_categories = {}
        self.is_custom_category = False
        
    def setup_hotkeys(self):
        """Setup global hotkeys for navigation"""
        try:
            # Disable keyboard hotkeys in terminal environment to prevent input blocking
            # keyboard.add_hotkey('shift+s', lambda: self.handle_hotkey('start'))
            # keyboard.add_hotkey('shift+r', lambda: self.handle_hotkey('readme'))
            # keyboard.add_hotkey('shift+q', lambda: self.handle_hotkey('quit'))
            # keyboard.add_hotkey('shift+h', lambda: self.handle_hotkey('home'))
            # keyboard.add_hotkey('shift+b', lambda: self.handle_hotkey('back'))
            # keyboard.add_hotkey('shift+n', lambda: self.handle_hotkey('next'))
            self.hotkey_enabled = False
        except:
            # If keyboard hotkeys fail, continue without them
            self.hotkey_enabled = False
    
    def handle_hotkey(self, action):
        """Handle hotkey presses"""
        if action == 'quit':
            self.quit_app()
        # Other hotkey actions can be handled here
    
    def run(self):
        """Main application loop"""
        console.clear()
        self.setup_hotkeys()
        
        while True:
            try:
                if self.current_page == "main_menu":
                    self.show_main_menu()
                elif self.current_page == "readme":
                    self.show_readme()
                elif self.current_page == "category_selection":
                    self.show_category_selection()
                elif self.current_page == "subcategory_selection":
                    self.show_subcategory_selection()
                elif self.current_page == "questionnaire":
                    self.show_questionnaire()
                elif self.current_page == "prompt_result":
                    self.show_prompt_result()
                elif self.current_page == "template_guide":
                    self.show_template_guide()
                elif self.current_page == "settings":
                    self.show_settings()
                elif self.current_page == "history":
                    self.show_history()
                elif self.current_page == "stats":
                    self.show_stats()
                elif self.current_page == "custom_category_selection":
                    self.show_custom_category_selection()
                elif self.current_page == "custom_subcategory_selection":
                    self.show_custom_subcategory_selection()
                else:
                    self.current_page = "main_menu"
            except KeyboardInterrupt:
                self.quit_app()
            except Exception as e:
                console.print(f"[red]Error: {str(e)}[/red]")
                self.current_page = "main_menu"
    
    def show_main_menu(self):
        """Display the main menu splash screen"""
        console.clear()
        display_manager.show_header()
        
        # Create colorful menu
        menu_text = Text()
        menu_text.append("🚀 ", style="bold yellow")
        menu_text.append("START", style="bold magenta")
        menu_text.append(" - Begin creating prompts ", style="cyan")
        menu_text.append("(type 'start')", style="dim white")
        menu_text.append("\n\n")
        
        menu_text.append("📖 ", style="bold blue")
        menu_text.append("README", style="bold cyan")
        menu_text.append(" - Learn how to use PromptGPT OS ", style="green")
        menu_text.append("(type 'readme')", style="dim white")
        menu_text.append("\n\n")
        
        menu_text.append("📚 ", style="bold blue")
        menu_text.append("HISTORY", style="bold blue")
        menu_text.append(" - View your past 10 generated prompts ", style="green")
        menu_text.append("(type 'history')", style="dim white")
        menu_text.append("\n\n")
        
        menu_text.append("📚 ", style="bold magenta")
        menu_text.append("TEMPLATE GUIDE", style="bold purple")
        menu_text.append(" - Learn how to create custom templates ", style="bright_blue")
        menu_text.append("(type 'guide')", style="dim white")
        menu_text.append("\n\n")
        
        menu_text.append("⚙️ ", style="bold yellow")
        menu_text.append("SETTINGS", style="bold orange1")
        menu_text.append(" - Manage custom categories and templates ", style="bright_green")
        menu_text.append("(type 'settings')", style="dim white")
        menu_text.append("\n\n")
        
        menu_text.append("📊 ", style="bold green")
        menu_text.append("STATS", style="bold green")
        menu_text.append(" - View session statistics and progress ", style="cyan")
        menu_text.append("(type 'stats')", style="dim white")
        menu_text.append("\n\n")
        
        menu_text.append("🚪 ", style="bold red")
        menu_text.append("QUIT", style="bold red")
        menu_text.append(" - Exit the application ", style="yellow")
        menu_text.append("(type 'quit')", style="dim white")
        menu_text.append("\n\n")
        
        menu_text.append("🔧 ", style="bold yellow")
        menu_text.append("DEBUG", style="bold yellow") 
        menu_text.append(" - Run automated debugging ", style="cyan")
        menu_text.append("(type 'debug')", style="dim white")
        menu_text.append("\n")
        
        menu_text.append("🔍 ", style="bold blue")
        menu_text.append("ANALYZE", style="bold blue")
        menu_text.append(" - Analyze codebase for errors ", style="cyan") 
        menu_text.append("(type 'analyze')", style="dim white")
        menu_text.append("\n")
        
        menu_text.append("🧪 ", style="bold green")
        menu_text.append("TEST", style="bold green")
        menu_text.append(" - Run automated test suite ", style="cyan")
        menu_text.append("(type 'test')", style="dim white")
        
        menu_panel = Panel(
            Align.center(menu_text),
            title="[bold purple]✨ MAIN MENU ✨[/bold purple]",
            border_style="bright_magenta",
            padding=(2, 4)
        )
        
        console.print(menu_panel)
        console.print("\n")
        
        choice = Prompt.ask(
            "[bold cyan]Enter your choice[/bold cyan]",
            choices=["start", "history", "readme", "guide", "settings", "stats", "debug", "analyze", "test", "quit", "s", "h", "r", "g", "set", "st", "d", "a", "t", "q"],
            default="start"
        ).lower()
        
        if choice in ["start", "s"]:
            progress_tracker.track_category_visit("menu_start")
            self.current_page = "category_selection"
        elif choice in ["history", "h"]:
            self.current_page = "history"
        elif choice in ["readme", "r"]:
            self.current_page = "readme"
        elif choice in ["guide", "g"]:
            self.current_page = "template_guide"
        elif choice in ["settings", "set"]:
            self.current_page = "settings"
        elif choice in ["stats", "st"]:
            self.current_page = "stats"
        elif choice in ["debug", "d"]:
            self.run_debug_system()
        elif choice in ["analyze", "a"]:
            self.run_analysis_system()
        elif choice in ["test", "t"]:
            self.run_test_suite()
        elif choice in ["quit", "q"]:
            self.quit_app()
    
    def show_readme(self):
        """Display the readme page"""
        console.clear()
        display_manager.show_header()
        
        readme_content = Text()
        readme_content.append("🎯 ", style="bold yellow")
        readme_content.append("PURPOSE\n", style="bold magenta")
        readme_content.append("PromptGPT OS helps you create detailed, effective prompts for AI content generation.\n\n", style="white")
        
        readme_content.append("🔄 ", style="bold blue")
        readme_content.append("HOW IT WORKS\n", style="bold cyan")
        readme_content.append("1. Select a content category (Code, Image, Music, Text, Video)\n", style="green")
        readme_content.append("2. Choose a specific subcategory\n", style="green")
        readme_content.append("3. Answer comprehensive questions about your desired content\n", style="green")
        readme_content.append("4. Get a professionally crafted AI prompt\n", style="green")
        readme_content.append("5. Save or copy your prompt for use with AI tools\n\n", style="green")
        
        readme_content.append("💡 ", style="bold orange1")
        readme_content.append("BEST PRACTICES FOR MAXIMUM PROMPT QUALITY\n", style="bold yellow")
        readme_content.append("• NEVER use yes/no answers - Always be detailed and comprehensive\n", style="bright_red")
        readme_content.append("• The more detail you provide, the better your prompt will be\n", style="bright_green")
        readme_content.append("• Elaborate on every aspect of your requirements\n", style="white")
        readme_content.append("• Include specific examples to clarify your needs\n", style="white")
        readme_content.append("• Provide context about your target audience\n", style="white")
        readme_content.append("• Mention style preferences and constraints\n", style="white")
        readme_content.append("• Specify technical requirements when relevant\n", style="white")
        readme_content.append("• Reference examples or inspirations you admire\n", style="white")
        readme_content.append("• Review the generated prompt before using it\n\n", style="white")
        
        readme_content.append("⌨️ ", style="bold purple")
        readme_content.append("NAVIGATION\n", style="bold magenta")
        readme_content.append("• Use hotkeys (Shift+Letter) for quick navigation\n", style="cyan")
        readme_content.append("• Type menu options directly\n", style="cyan")
        readme_content.append("• Use 'back', 'home', 'quit' commands anytime\n", style="cyan")
        
        readme_panel = Panel(
            readme_content,
            title="[bold green]📚 README & USER GUIDE 📚[/bold green]",
            border_style="bright_green",
            padding=(1, 2)
        )
        
        console.print(readme_panel)
        console.print("\n")
        
        choice = Prompt.ask(
            "[bold cyan]Press Enter to return to main menu, or type 'quit' to exit[/bold cyan]",
            default="home"
        ).lower()
        
        if choice == "quit":
            self.quit_app()
        else:
            self.current_page = "main_menu"
    
    def show_category_selection(self):
        """Display category selection menu"""
        console.clear()
        display_manager.show_header()
        
        categories_text = Text()
        categories_text.append("🎨 Select the type of content you want to create:\n\n", style="bold white")
        
        for i, (key, category) in enumerate(CATEGORIES.items(), 1):
            icon = category['icon']
            name = category['name']
            desc = category['description']
            
            categories_text.append(f"{icon} ", style="bold yellow")
            categories_text.append(f"{i}. {name.upper()}", style=f"bold {category['color']}")
            categories_text.append(f" - {desc}\n", style="white")
        
        # Add custom categories option
        categories_text.append("\n🔧 ", style="bold magenta")
        categories_text.append("6. CUSTOM", style="bold magenta")
        categories_text.append(" - Your custom categories and templates\n", style="white")
        
        categories_text.append("\n🏠 HOME | 🚪 QUIT", style="dim cyan")
        
        categories_panel = Panel(
            categories_text,
            title="[bold purple]🎯 CONTENT CATEGORIES 🎯[/bold purple]",
            border_style="bright_purple",
            padding=(1, 2)
        )
        
        console.print(categories_panel)
        console.print("\n")
        
        choice = Prompt.ask(
            "[bold cyan]Enter category number or name[/bold cyan]",
            choices=["1", "2", "3", "4", "5", "6", "code", "image", "music", "text", "video", "custom", "home", "quit"]
        ).lower()
        
        if choice == "quit":
            self.quit_app()
        elif choice == "home":
            self.current_page = "main_menu"
        else:
            # Map choice to category
            category_map = {
                "1": "code", "code": "code",
                "2": "image", "image": "image", 
                "3": "music", "music": "music",
                "4": "text", "text": "text",
                "5": "video", "video": "video"
            }
            
            if choice in ["6", "custom"]:
                self.current_page = "custom_category_selection"
            else:
                self.current_category = category_map.get(choice)
                if self.current_category:
                    self.current_page = "subcategory_selection"
    
    def show_subcategory_selection(self):
        """Display subcategory selection for chosen category"""
        console.clear()
        display_manager.show_header()
        
        category_info = CATEGORIES[self.current_category]
        subcategories = category_info['subcategories']
        
        subcategory_text = Text()
        subcategory_text.append(f"{category_info['icon']} ", style="bold yellow")
        subcategory_text.append(f"Select {category_info['name']} type:\n\n", style=f"bold {category_info['color']}")
        
        for i, subcat in enumerate(subcategories, 1):
            subcategory_text.append(f"  {i}. ", style="bold white")
            subcategory_text.append(f"{subcat.upper()}", style=f"bold {category_info['color']}")
            subcategory_text.append(f"\n", style="white")
        
        subcategory_text.append("\n🔙 BACK | 🏠 HOME | 🚪 QUIT", style="dim cyan")
        
        subcategory_panel = Panel(
            subcategory_text,
            title=f"[bold {category_info['color']}]{category_info['icon']} {category_info['name'].upper()} SUBCATEGORIES {category_info['icon']}[/bold {category_info['color']}]",
            border_style=category_info['color'],
            padding=(1, 2)
        )
        
        console.print(subcategory_panel)
        console.print("\n")
        
        valid_choices = [str(i) for i in range(1, len(subcategories) + 1)]
        valid_choices.extend([sub.lower() for sub in subcategories])
        valid_choices.extend(["back", "home", "quit"])
        
        choice = Prompt.ask(
            "[bold cyan]Enter subcategory number or name[/bold cyan]",
            choices=valid_choices
        ).lower()
        
        if choice == "quit":
            self.quit_app()
        elif choice == "home":
            self.current_page = "main_menu"
        elif choice == "back":
            self.current_page = "category_selection"
        else:
            # Map choice to subcategory
            try:
                if choice.isdigit():
                    subcat_index = int(choice) - 1
                    self.current_subcategory = subcategories[subcat_index]
                else:
                    self.current_subcategory = next(sub for sub in subcategories if sub.lower() == choice)
                
                self.user_answers = {}
                self.question_index = 0
                self.is_custom_category = False
                self.current_page = "questionnaire"
            except (ValueError, IndexError, StopIteration):
                console.print("[red]Invalid choice. Please try again.[/red]")
                time.sleep(1)
    
    def show_questionnaire(self):
        """Display questionnaire for selected category/subcategory"""
        questions = prompt_gen.get_questions(self.current_category, self.current_subcategory, self.is_custom_category)
        
        if self.question_index >= len(questions):
            self.current_page = "prompt_result"
            return
        
        console.clear()
        display_manager.show_header()
        
        current_question = questions[self.question_index]
        progress = f"Question {self.question_index + 1} of {len(questions)}"
        
        question_text = Text()
        question_text.append(f"📝 {progress}\n\n", style="bold cyan")
        question_text.append(f"Category: ", style="white")
        question_text.append(f"{self.current_category.title()}", style="bold magenta")
        question_text.append(f" → ", style="white")
        question_text.append(f"{self.current_subcategory.title()}", style="bold cyan")
        question_text.append(f"\n\n", style="white")
        question_text.append(f"❓ {current_question}\n", style="bold white")
        question_text.append(f"\n💡 Tip: The more details you provide, the better your prompt will be!\n", style="dim yellow")
        question_text.append(f"Navigation: next | skip | back | home | quit | ? (help)\n", style="dim cyan")
        
        question_panel = Panel(
            question_text,
            title="[bold green]🤔 QUESTIONNAIRE 🤔[/bold green]",
            border_style="bright_green",
            padding=(1, 2)
        )
        
        console.print(question_panel)
        console.print("\n")
        
        # Use enhanced navigation with skip support
        answer = nav_handler.get_user_choice(
            "[bold cyan]Your answer[/bold cyan]", 
            allow_empty=True, 
            show_skip=True
        )
        
        # Handle navigation commands
        if answer == "quit":
            self.quit_app()
        elif answer == "home":
            self.current_page = "main_menu"
        elif answer == "restart":
            self.user_answers = {}
            self.question_index = 0
        elif answer == "back":
            if self.question_index > 0:
                self.question_index -= 1
                # Remove the previous answer
                if self.question_index in self.user_answers:
                    del self.user_answers[self.question_index]
            else:
                self.current_page = "subcategory_selection"
        elif answer == "next":
            # Move to next question without saving answer
            self.question_index += 1
        elif answer == "skip":
            # Skip this question and move to next
            console.print("[yellow]Question skipped.[/yellow]")
            time.sleep(0.5)
            self.question_index += 1
        else:
            # Store answer and move to next question
            if answer.strip():  # Only store non-empty answers
                self.user_answers[self.question_index] = answer
                progress_tracker.track_question_answered()
            self.question_index += 1
    
    def show_prompt_result(self):
        """Display the generated prompt result"""
        console.clear()
        display_manager.show_header()
        
        # Generate the prompt
        generated_prompt = prompt_gen.generate_prompt(
            self.current_category, 
            self.current_subcategory, 
            self.user_answers,
            self.is_custom_category
        )
        
        # Track prompt generation and add to history
        progress_tracker.track_prompt_generated(f"{self.current_category}_{self.current_subcategory}")
        history_manager.add_to_history(
            generated_prompt,
            self.current_category,
            self.current_subcategory,
            self.user_answers
        )
        
        result_text = Text()
        result_text.append("🎉 Your AI prompt has been generated!\n\n", style="bold green")
        result_text.append("Category: ", style="white")
        result_text.append(f"{self.current_category.title()}", style="bold magenta")
        result_text.append(" → ", style="white")
        result_text.append(f"{self.current_subcategory.title()}", style="bold cyan")
        result_text.append("\n\n", style="white")
        
        # Show clipboard status
        clipboard_status = clipboard_manager.get_status()
        if clipboard_status['available']:
            result_text.append("📋 Clipboard ready - Choose COPY to copy to clipboard\n", style="dim green")
        else:
            result_text.append("⚠️  Clipboard not available on this system\n", style="dim yellow")
        
        # Display the generated prompt
        prompt_panel = Panel(
            generated_prompt,
            title="[bold yellow]✨ GENERATED AI PROMPT ✨[/bold yellow]",
            border_style="bright_yellow",
            padding=(1, 2)
        )
        
        result_panel = Panel(
            result_text,
            title="[bold green]🎯 PROMPT GENERATION COMPLETE 🎯[/bold green]",
            border_style="bright_green",
            padding=(1, 2)
        )
        
        console.print(result_panel)
        console.print()
        console.print(prompt_panel)
        console.print()
        
        # Navigation options
        nav_text = Text()
        nav_text.append("📋 ", style="bold magenta")
        nav_text.append("COPY", style="bold magenta")
        nav_text.append(" | ", style="dim white")
        nav_text.append("💾 ", style="bold blue")
        nav_text.append("SAVE", style="bold blue")
        nav_text.append(" | ", style="dim white")
        nav_text.append("🔄 ", style="bold yellow")
        nav_text.append("RESTART", style="bold yellow")
        nav_text.append(" | ", style="dim white")
        nav_text.append("🏠 ", style="bold green")
        nav_text.append("HOME", style="bold green")
        nav_text.append(" | ", style="dim white")
        nav_text.append("🚪 ", style="bold red")
        nav_text.append("QUIT", style="bold red")
        
        console.print(nav_text)
        console.print()
        
        choice = Prompt.ask(
            "[bold cyan]What would you like to do?[/bold cyan]",
            choices=["copy", "save", "restart", "home", "quit"],
            default="copy"
        ).lower()
        
        if choice == "copy":
            # Copy to clipboard with metadata
            success = clipboard_manager.copy_prompt_with_metadata(
                generated_prompt, 
                self.current_category, 
                self.current_subcategory
            )
            if success:
                progress_tracker.track_clipboard_copy()
                time.sleep(2)
            
            # Ask what to do next
            next_choice = Prompt.ask(
                "[bold cyan]What would you like to do next?[/bold cyan]",
                choices=["save", "restart", "home", "quit"],
                default="home"
            ).lower()
            
            if next_choice == "save":
                filename = file_handler.save_prompt(generated_prompt, self.current_category, self.current_subcategory)
                console.print(f"[bold green]✅ Prompt saved to: {filename}[/bold green]")
                progress_tracker.track_file_saved()
                time.sleep(2)
                self.current_page = "main_menu"
            elif next_choice == "restart":
                self.user_answers = {}
                self.question_index = 0
                self.current_page = "questionnaire"
            elif next_choice == "home":
                self.current_page = "main_menu"
            elif next_choice == "quit":
                self.quit_app()
                
        elif choice == "save":
            filename = file_handler.save_prompt(generated_prompt, self.current_category, self.current_subcategory)
            console.print(f"[bold green]✅ Prompt saved to: {filename}[/bold green]")
            progress_tracker.track_file_saved()
            time.sleep(2)
            self.current_page = "main_menu"
        elif choice == "restart":
            self.user_answers = {}
            self.question_index = 0
            self.current_page = "questionnaire"
        elif choice == "home":
            self.current_page = "main_menu"
        elif choice == "quit":
            self.quit_app()
    
    def show_template_guide(self):
        """Display the template creation guide"""
        result = show_template_guide()
        self.current_page = "main_menu"
    
    def show_settings(self):
        """Display settings menu for custom categories and templates"""
        console.clear()
        display_manager.show_header()
        
        settings_text = Text()
        settings_text.append("⚙️ Settings & Customization\n\n", style="bold yellow")
        
        settings_text.append("1. ", style="bold cyan")
        settings_text.append("ADD CUSTOM CATEGORY", style="bold white")
        settings_text.append(" - Create a new content category\n", style="cyan")
        
        settings_text.append("2. ", style="bold cyan")
        settings_text.append("UPLOAD QUESTIONS", style="bold white")
        settings_text.append(" - Upload a text file with custom questions (50 max)\n", style="cyan")
        
        settings_text.append("3. ", style="bold cyan")
        settings_text.append("UPLOAD TEMPLATE", style="bold white")
        settings_text.append(" - Upload a custom template file\n", style="cyan")
        
        settings_text.append("4. ", style="bold cyan")
        settings_text.append("MANAGE CUSTOM CONTENT", style="bold white")
        settings_text.append(" - View and delete custom categories\n", style="cyan")
        
        settings_text.append("\n🏠 HOME | 🚪 QUIT", style="dim cyan")
        
        settings_panel = Panel(
            settings_text,
            title="[bold yellow]⚙️ SETTINGS & CUSTOMIZATION ⚙️[/bold yellow]",
            border_style="yellow",
            padding=(1, 2)
        )
        
        console.print(settings_panel)
        console.print()
        
        choice = Prompt.ask(
            "[bold cyan]Select option[/bold cyan]",
            choices=["1", "2", "3", "4", "add", "upload", "template", "manage", "home", "quit"],
            default="1"
        ).lower()
        
        if choice == "quit":
            self.quit_app()
        elif choice == "home":
            self.current_page = "main_menu"
        elif choice in ["1", "add"]:
            self.add_custom_category()
        elif choice in ["2", "upload"]:
            self.upload_custom_questions()
        elif choice in ["3", "template"]:
            self.upload_custom_template()
        elif choice in ["4", "manage"]:
            self.manage_custom_content()
    
    def add_custom_category(self):
        """Add a new custom category"""
        console.clear()
        display_manager.show_header()
        
        console.print(Panel(
            "[bold cyan]Create Custom Category[/bold cyan]\n\nAdd a new content category with custom subcategories",
            title="[bold yellow]Add Custom Category[/bold yellow]",
            border_style="yellow"
        ))
        
        category_name = Prompt.ask("[bold green]Category name[/bold green]")
        if not category_name:
            console.print("[red]Category name cannot be empty![/red]")
            console.input("\n[bold cyan]Press Enter to continue...[/bold cyan]")
            self.current_page = "settings"
            return
        
        description = Prompt.ask("[bold green]Description[/bold green]", default=f"Custom {category_name} content")
        
        # Get subcategories
        subcategories = {}
        console.print("\n[bold cyan]Add subcategories (press Enter with empty name to finish):[/bold cyan]")
        
        while True:
            sub_name = Prompt.ask("[bold green]Subcategory name[/bold green]", default="")
            if not sub_name:
                break
            sub_desc = Prompt.ask(f"[bold green]Description for {sub_name}[/bold green]", default="")
            subcategories[sub_name.lower().replace(" ", "_")] = {
                'name': sub_name,
                'description': sub_desc
            }
        
        if not subcategories:
            console.print("[red]At least one subcategory is required![/red]")
            console.input("\n[bold cyan]Press Enter to continue...[/bold cyan]")
            self.current_page = "settings"
            return
        
        # Save the category
        if settings_manager.add_custom_category(category_name.lower().replace(" ", "_"), subcategories, description):
            console.print(f"[green]✓ Custom category '{category_name}' created successfully![/green]")
        else:
            console.print("[red]✗ Failed to create custom category![/red]")
        
        console.input("\n[bold cyan]Press Enter to continue...[/bold cyan]")
        self.current_page = "settings"
    
    def upload_custom_questions(self):
        """Upload custom questions from file"""
        console.clear()
        display_manager.show_header()
        
        console.print(Panel(
            "[bold cyan]Upload Custom Questions[/bold cyan]\n\nUpload a text file with questions (max 50 per file)\nEach line should be one question",
            title="[bold yellow]Upload Questions[/bold yellow]",
            border_style="yellow"
        ))
        
        file_path = Prompt.ask("[bold green]File path[/bold green]")
        if not file_path:
            console.input("\n[bold cyan]Press Enter to continue...[/bold cyan]")
            self.current_page = "settings"
            return
        
        category = Prompt.ask("[bold green]Category name[/bold green]")
        subcategory = Prompt.ask("[bold green]Subcategory name[/bold green]")
        
        if settings_manager.upload_questions_from_file(file_path, category, subcategory):
            console.print("[green]✓ Questions uploaded successfully![/green]")
        else:
            console.print("[red]✗ Failed to upload questions![/red]")
        
        console.input("\n[bold cyan]Press Enter to continue...[/bold cyan]")
        self.current_page = "settings"
    
    def upload_custom_template(self):
        """Upload custom template from file"""
        console.clear()
        display_manager.show_header()
        
        console.print(Panel(
            "[bold cyan]Upload Custom Template[/bold cyan]\n\nUpload a text file containing your template\nUse {answer_1}, {answer_2}, etc. for placeholders",
            title="[bold yellow]Upload Template[/bold yellow]",
            border_style="yellow"
        ))
        
        file_path = Prompt.ask("[bold green]Template file path[/bold green]")
        if not file_path:
            console.input("\n[bold cyan]Press Enter to continue...[/bold cyan]")
            self.current_page = "settings"
            return
        
        category = Prompt.ask("[bold green]Category name[/bold green]")
        subcategory = Prompt.ask("[bold green]Subcategory name[/bold green]")
        
        if settings_manager.upload_template_from_file(file_path, category, subcategory):
            console.print("[green]✓ Template uploaded successfully![/green]")
        else:
            console.print("[red]✗ Failed to upload template![/red]")
        
        console.input("\n[bold cyan]Press Enter to continue...[/bold cyan]")
        self.current_page = "settings"
    
    def manage_custom_content(self):
        """Manage existing custom content"""
        console.clear()
        display_manager.show_header()
        
        custom_categories = settings_manager.list_custom_categories()
        
        if not custom_categories:
            console.print(Panel(
                "[yellow]No custom categories found.[/yellow]\n\nUse the other settings options to create custom content.",
                title="[bold yellow]Custom Content[/bold yellow]",
                border_style="yellow"
            ))
            console.input("\n[bold cyan]Press Enter to continue...[/bold cyan]")
            self.current_page = "settings"
            return
        
        manage_text = Text()
        manage_text.append("Custom Categories:\n\n", style="bold cyan")
        
        for i, category in enumerate(custom_categories, 1):
            manage_text.append(f"{i}. {category}\n", style="white")
        
        manage_text.append(f"\n{len(custom_categories) + 1}. DELETE CATEGORY\n", style="bold red")
        manage_text.append(f"{len(custom_categories) + 2}. BACK TO SETTINGS", style="bold yellow")
        
        manage_panel = Panel(
            manage_text,
            title="[bold yellow]Manage Custom Content[/bold yellow]",
            border_style="yellow"
        )
        
        console.print(manage_panel)
        
        choices = [str(i) for i in range(1, len(custom_categories) + 3)] + ["delete", "back"]
        choice = Prompt.ask("[bold cyan]Select option[/bold cyan]", choices=choices).lower()
        
        if choice == "back" or choice == str(len(custom_categories) + 2):
            self.current_page = "settings"
        elif choice == "delete" or choice == str(len(custom_categories) + 1):
            self.delete_custom_category(custom_categories)
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(custom_categories):
                    console.print(f"\n[bold green]Selected: {custom_categories[idx]}[/bold green]")
                    console.input("[bold cyan]Press Enter to continue...[/bold cyan]")
            except ValueError:
                pass
            self.current_page = "settings"
    
    def delete_custom_category(self, categories):
        """Delete a custom category"""
        if not categories:
            return
        
        console.print("\n[bold red]⚠️  DELETE CUSTOM CATEGORY ⚠️[/bold red]")
        
        for i, category in enumerate(categories, 1):
            console.print(f"[white]{i}. {category}[/white]")
        
        choice = Prompt.ask(
            "[bold red]Which category to delete? (number or 'cancel')[/bold red]",
            choices=[str(i) for i in range(1, len(categories) + 1)] + ["cancel"]
        )
        
        if choice != "cancel":
            try:
                idx = int(choice) - 1
                category_to_delete = categories[idx]
                
                confirm = Confirm.ask(f"[bold red]Delete '{category_to_delete}' and all its data?[/bold red]")
                if confirm:
                    if settings_manager.delete_custom_category(category_to_delete):
                        console.print(f"[green]✓ Deleted '{category_to_delete}' successfully![/green]")
                    else:
                        console.print("[red]✗ Failed to delete category![/red]")
            except ValueError:
                console.print("[red]Invalid selection![/red]")
        
        console.input("\n[bold cyan]Press Enter to continue...[/bold cyan]")
        self.current_page = "settings"
    
    def show_custom_category_selection(self):
        """Display custom categories for selection"""
        console.clear()
        display_manager.show_header()
        
        custom_categories = settings_manager.load_custom_categories()
        
        if not custom_categories:
            console.print(Panel(
                "[yellow]No custom categories available.[/yellow]\n\nUse Settings to create custom categories.",
                title="[bold yellow]Custom Categories[/bold yellow]",
                border_style="yellow"
            ))
            console.input("\n[bold cyan]Press Enter to continue...[/bold cyan]")
            self.current_page = "category_selection"
            return
        
        categories_text = Text()
        categories_text.append("🔧 Select your custom content category:\n\n", style="bold white")
        
        for i, (key, category) in enumerate(custom_categories.items(), 1):
            icon = category.get('icon', '🔧')
            name = category.get('name', key.title())
            desc = category.get('description', 'Custom category')
            
            categories_text.append(f"{icon} ", style="bold yellow")
            categories_text.append(f"{i}. {name.upper()}", style="bold magenta")
            categories_text.append(f" - {desc}\n", style="white")
        
        categories_text.append("\n🏠 HOME | 🔙 BACK | 🚪 QUIT", style="dim cyan")
        
        categories_panel = Panel(
            categories_text,
            title="[bold magenta]🔧 CUSTOM CATEGORIES 🔧[/bold magenta]",
            border_style="bright_magenta",
            padding=(1, 2)
        )
        
        console.print(categories_panel)
        console.print()
        
        choices = [str(i) for i in range(1, len(custom_categories) + 1)] + ["home", "back", "quit"]
        choice = Prompt.ask("[bold cyan]Enter category number[/bold cyan]", choices=choices).lower()
        
        if choice == "quit":
            self.quit_app()
        elif choice == "home":
            self.current_page = "main_menu"
        elif choice == "back":
            self.current_page = "category_selection"
        else:
            try:
                idx = int(choice) - 1
                category_keys = list(custom_categories.keys())
                if 0 <= idx < len(category_keys):
                    self.current_category = category_keys[idx]
                    self.current_page = "custom_subcategory_selection"
            except ValueError:
                pass
    
    def show_custom_subcategory_selection(self):
        """Display subcategories for custom category"""
        console.clear()
        display_manager.show_header()
        
        custom_categories = settings_manager.load_custom_categories()
        if self.current_category not in custom_categories:
            self.current_page = "custom_category_selection"
            return
        
        category_data = custom_categories[self.current_category]
        subcategories = category_data.get('subcategories', {})
        
        if not subcategories:
            console.print(Panel(
                "[yellow]No subcategories found for this custom category.[/yellow]",
                title="[bold yellow]Custom Subcategories[/bold yellow]",
                border_style="yellow"
            ))
            console.input("\n[bold cyan]Press Enter to continue...[/bold cyan]")
            self.current_page = "custom_category_selection"
            return
        
        subcats_text = Text()
        subcats_text.append(f"🔧 Select subcategory for {category_data.get('name', self.current_category)}:\n\n", style="bold white")
        
        for i, (key, subcat) in enumerate(subcategories.items(), 1):
            name = subcat.get('name', key.title())
            desc = subcat.get('description', '')
            
            subcats_text.append(f"🔸 ", style="bold cyan")
            subcats_text.append(f"{i}. {name.upper()}", style="bold magenta")
            if desc:
                subcats_text.append(f" - {desc}", style="white")
            subcats_text.append("\n", style="white")
        
        subcats_text.append("\n🏠 HOME | 🔙 BACK | 🚪 QUIT", style="dim cyan")
        
        subcats_panel = Panel(
            subcats_text,
            title=f"[bold magenta]🔧 {category_data.get('name', self.current_category).upper()} SUBCATEGORIES 🔧[/bold magenta]",
            border_style="bright_magenta",
            padding=(1, 2)
        )
        
        console.print(subcats_panel)
        console.print()
        
        choices = [str(i) for i in range(1, len(subcategories) + 1)] + ["home", "back", "quit"]
        choice = Prompt.ask("[bold cyan]Enter subcategory number[/bold cyan]", choices=choices).lower()
        
        if choice == "quit":
            self.quit_app()
        elif choice == "home":
            self.current_page = "main_menu"
        elif choice == "back":
            self.current_page = "custom_category_selection"
        else:
            try:
                idx = int(choice) - 1
                subcat_keys = list(subcategories.keys())
                if 0 <= idx < len(subcat_keys):
                    self.current_subcategory = subcat_keys[idx]
                    self.user_answers = {}
                    self.question_index = 0
                    self.is_custom_category = True
                    self.current_page = "questionnaire"
                    progress_tracker.track_subcategory_visit(f"{self.current_category}_{self.current_subcategory}")
            except ValueError:
                pass
    
    def show_history(self):
        """Display history page"""
        result = history_manager.display_history_page()
        if result == "main_menu":
            self.current_page = "main_menu"
    
    def show_stats(self):
        """Display session statistics and progress dashboard"""
        console.clear()
        progress_tracker.display_progress_dashboard()
        
        input("\nPress Enter to return to main menu...")
        self.current_page = "main_menu"

    def run_debug_system(self):
        """Run automated debugging system"""
        console.clear()
        display_manager.show_header()
        
        console.print("[bold yellow]🔧 AUTOMATED DEBUG SYSTEM[/bold yellow]")
        console.print("Developed by: https://github.com/KowaiAI\n")
        
        try:
            from utils.error_handler import debug_command
            debug_command()
        except Exception as e:
            console.print(f"[bold red]Debug system error: {e}[/bold red]")
        
        console.print("\n[cyan]Press Enter to return to main menu...[/cyan]")
        input()
        self.current_page = "main_menu"
    
    def run_analysis_system(self):
        """Run codebase analysis system"""
        console.clear()
        display_manager.show_header()
        
        console.print("[bold yellow]🔍 CODEBASE ANALYSIS SYSTEM[/bold yellow]")
        console.print("Developed by: https://github.com/KowaiAI\n")
        
        try:
            from utils.error_handler import analyze_command
            analyze_command()
        except Exception as e:
            console.print(f"[bold red]Analysis system error: {e}[/bold red]")
        
        console.print("\n[cyan]Press Enter to return to main menu...[/cyan]")
        input()
        self.current_page = "main_menu"
    
    def run_test_suite(self):
        """Run automated test suite"""
        console.clear()
        display_manager.show_header()
        
        console.print("[bold yellow]🧪 AUTOMATED TEST SUITE[/bold yellow]")
        console.print("Developed by: https://github.com/KowaiAI\n")
        
        try:
            from utils.test_runner import run_test_suite
            run_test_suite()
        except Exception as e:
            console.print(f"[bold red]Test suite error: {e}[/bold red]")
        
        console.print("\n[cyan]Press Enter to return to main menu...[/cyan]")
        input()
        self.current_page = "main_menu"

    def quit_app(self):
        """Exit the application gracefully with session summary"""
        console.clear()
        
        # Show final session summary with animation
        animation_manager.typewriter_effect(
            "Generating final session report...", 
            delay=0.05,
            style="cyan"
        )
        
        progress_tracker.display_progress_dashboard()
        
        goodbye_text = Text()
        goodbye_text.append("👋 ", style="bold yellow")
        goodbye_text.append("Thank you for using PromptGPT OS!", style="bold magenta")
        goodbye_text.append("\n🚀 Happy AI content creation! 🚀", style="bold cyan")
        goodbye_text.append("\n[dim cyan]Developed by: https://github.com/KowaiAI[/dim cyan]", style="dim cyan")
        
        goodbye_panel = Panel(
            Align.center(goodbye_text),
            title="[bold green]✨ GOODBYE ✨[/bold green]",
            border_style="bright_green",
            padding=(2, 4)
        )
        
        console.print(goodbye_panel)
        console.print()
        sys.exit(0)

def main():
    """Entry point for the application"""
    try:
        app = PromptGPTOS()
        app.run()
    except KeyboardInterrupt:
        console.print("\n[bold red]Application interrupted by user.[/bold red]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]Fatal error: {str(e)}[/bold red]")
        sys.exit(1)

if __name__ == "__main__":
    main()
