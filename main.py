#!/usr/bin/env python3
"""
PromptGPT OS - AI Content Prompt Generator
A colorful command-line application for generating AI content prompts
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

from utils.navigation import NavigationHandler
from utils.prompt_generator import PromptGenerator
from utils.file_handler import FileHandler
from ui.display import DisplayManager
from config.settings import COLORS, CATEGORIES, ASCII_HEADER

console = Console()
nav_handler = NavigationHandler()
prompt_gen = PromptGenerator()
file_handler = FileHandler()
display_manager = DisplayManager()

class PromptGPTOS:
    def __init__(self):
        self.current_page = "main_menu"
        self.user_answers = {}
        self.current_category = None
        self.current_subcategory = None
        self.question_index = 0
        self.hotkey_enabled = True
        
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
        menu_text.append("(Shift+S or type 'start')", style="dim white")
        menu_text.append("\n\n")
        
        menu_text.append("📖 ", style="bold blue")
        menu_text.append("README", style="bold cyan")
        menu_text.append(" - Learn how to use PromptGPT OS ", style="green")
        menu_text.append("(Shift+R or type 'readme')", style="dim white")
        menu_text.append("\n\n")
        
        menu_text.append("🚪 ", style="bold red")
        menu_text.append("QUIT", style="bold orange1")
        menu_text.append(" - Exit the application ", style="yellow")
        menu_text.append("(Shift+Q or type 'quit')", style="dim white")
        
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
            choices=["start", "readme", "quit", "s", "r", "q"],
            default="start"
        ).lower()
        
        if choice in ["start", "s"]:
            self.current_page = "category_selection"
        elif choice in ["readme", "r"]:
            self.current_page = "readme"
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
            choices=["1", "2", "3", "4", "5", "code", "image", "music", "text", "video", "home", "quit"]
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
                self.current_page = "questionnaire"
            except (ValueError, IndexError, StopIteration):
                console.print("[red]Invalid choice. Please try again.[/red]")
                time.sleep(1)
    
    def show_questionnaire(self):
        """Display questionnaire for selected category/subcategory"""
        questions = prompt_gen.get_questions(self.current_category, self.current_subcategory)
        
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
        
        question_panel = Panel(
            question_text,
            title="[bold green]🤔 QUESTIONNAIRE 🤔[/bold green]",
            border_style="bright_green",
            padding=(1, 2)
        )
        
        console.print(question_panel)
        console.print("\n")
        
        # Navigation info
        nav_text = Text()
        nav_text.append("Navigation: ", style="dim white")
        nav_text.append("'back' ", style="bold yellow")
        nav_text.append("| ", style="dim white")
        nav_text.append("'restart' ", style="bold blue")
        nav_text.append("| ", style="dim white")
        nav_text.append("'home' ", style="bold green")
        nav_text.append("| ", style="dim white")
        nav_text.append("'quit'", style="bold red")
        
        console.print(nav_text)
        console.print()
        
        answer = Prompt.ask("[bold cyan]Your answer[/bold cyan]", default="").strip()
        
        if answer.lower() == "quit":
            self.quit_app()
        elif answer.lower() == "home":
            self.current_page = "main_menu"
        elif answer.lower() == "restart":
            self.user_answers = {}
            self.question_index = 0
        elif answer.lower() == "back":
            if self.question_index > 0:
                self.question_index -= 1
                # Remove the previous answer
                if len(self.user_answers) > self.question_index:
                    del self.user_answers[self.question_index]
            else:
                self.current_page = "subcategory_selection"
        else:
            # Store answer and move to next question
            self.user_answers[self.question_index] = answer
            self.question_index += 1
    
    def show_prompt_result(self):
        """Display the generated prompt result"""
        console.clear()
        display_manager.show_header()
        
        # Generate the prompt
        generated_prompt = prompt_gen.generate_prompt(
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
            choices=["save", "restart", "home", "quit"],
            default="home"
        ).lower()
        
        if choice == "save":
            filename = file_handler.save_prompt(generated_prompt, self.current_category, self.current_subcategory)
            console.print(f"[bold green]✅ Prompt saved to: {filename}[/bold green]")
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
    
    def quit_app(self):
        """Exit the application gracefully"""
        console.clear()
        goodbye_text = Text()
        goodbye_text.append("👋 ", style="bold yellow")
        goodbye_text.append("Thank you for using PromptGPT OS!", style="bold magenta")
        goodbye_text.append("\n🚀 Happy AI content creation! 🚀", style="bold cyan")
        
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
