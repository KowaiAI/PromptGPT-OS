"""
# PromptGPT OS - Display Management System
# Developed by: https://github.com/KowaiAI
# Copyright (c) 2025 KowaiAI. All rights reserved.
# 
# This file contains proprietary user interface and display code.
# Unauthorized copying, modification, or distribution is prohibited.
# 
# Watermark: PROMPTGPT_OS_KOWAI_AI_2025_UI_CORE
"""

import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.layout import Layout
from rich.live import Live
from typing import Optional, List, Dict, Any

from config.settings import ASCII_HEADER, COLORS, APP_NAME, APP_VERSION

console = Console()

class DisplayManager:
    """Manages all display operations for the terminal interface"""
    
    def __init__(self):
        self.console = console
        self.current_theme = "default"
        self.animation_enabled = True
        
    def show_header(self):
        """Display the main application header with ASCII art"""
        header_text = Text()
        
        # Add the ASCII art header in pink
        for line in ASCII_HEADER.split('\n'):
            header_text.append(line + '\n', style='bright_magenta')
        
        # Add version information
        version_text = Text()
        version_text.append(f"Version {APP_VERSION}", style="dim cyan")
        version_text.append(" | ", style="dim white")
        version_text.append("Made with ❤️ for AI creators", style="dim cyan")
        
        header_panel = Panel(
            Align.center(header_text),
            border_style="bright_magenta",
            padding=(0, 2)
        )
        
        version_panel = Panel(
            Align.center(version_text),
            border_style="dim magenta",
            padding=(0, 2)
        )
        
        self.console.print(header_panel)
        self.console.print(version_panel)
        self.console.print()
    
    def show_loading(self, message: str = "Loading...", duration: float = 2.0):
        """Display an animated loading screen"""
        if not self.animation_enabled:
            self.console.print(f"[cyan]{message}[/cyan]")
            return
            
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console,
            transient=True,
        ) as progress:
            task = progress.add_task(f"[cyan]{message}[/cyan]", total=100)
            
            for i in range(100):
                time.sleep(duration / 100)
                progress.update(task, advance=1)
    
    def show_success_message(self, message: str, details: Optional[str] = None):
        """Display a success message with optional details"""
        success_text = Text()
        success_text.append("✅ ", style="bright_green")
        success_text.append(message, style="bright_green")
        
        if details:
            success_text.append(f"\n💡 {details}", style="dim green")
        
        success_panel = Panel(
            success_text,
            title="[bold green]Success[/bold green]",
            border_style="bright_green",
            padding=(1, 2)
        )
        
        self.console.print(success_panel)
        self.console.print()
    
    def show_error_message(self, message: str, details: Optional[str] = None):
        """Display an error message with optional details"""
        error_text = Text()
        error_text.append("❌ ", style="bright_red")
        error_text.append(message, style="bright_red")
        
        if details:
            error_text.append(f"\n🔍 {details}", style="dim red")
        
        error_panel = Panel(
            error_text,
            title="[bold red]Error[/bold red]",
            border_style="bright_red",
            padding=(1, 2)
        )
        
        self.console.print(error_panel)
        self.console.print()
    
    def show_warning_message(self, message: str, details: Optional[str] = None):
        """Display a warning message with optional details"""
        warning_text = Text()
        warning_text.append("⚠️ ", style="orange1")
        warning_text.append(message, style="orange1")
        
        if details:
            warning_text.append(f"\n💭 {details}", style="dim yellow")
        
        warning_panel = Panel(
            warning_text,
            title="[bold orange1]Warning[/bold orange1]",
            border_style="orange1",
            padding=(1, 2)
        )
        
        self.console.print(warning_panel)
        self.console.print()
    
    def show_info_message(self, message: str, details: Optional[str] = None):
        """Display an informational message with optional details"""
        info_text = Text()
        info_text.append("ℹ️ ", style="bright_blue")
        info_text.append(message, style="bright_blue")
        
        if details:
            info_text.append(f"\n📋 {details}", style="dim blue")
        
        info_panel = Panel(
            info_text,
            title="[bold blue]Information[/bold blue]",
            border_style="bright_blue",
            padding=(1, 2)
        )
        
        self.console.print(info_panel)
        self.console.print()
    
    def show_table(self, title: str, headers: List[str], rows: List[List[str]], 
                   table_style: str = "bright_cyan"):
        """Display a formatted table"""
        table = Table(title=title, title_style=f"bold {table_style}")
        
        # Add columns
        for header in headers:
            table.add_column(header, style="white", no_wrap=True)
        
        # Add rows
        for row in rows:
            table.add_row(*row)
        
        self.console.print(table)
        self.console.print()
    
    def show_progress_bar(self, total: int, description: str = "Progress"):
        """Show a progress bar context manager"""
        return Progress(
            TextColumn("[progress.description]{task.description}"),
            SpinnerColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=self.console
        )
    
    def create_layout(self, sections: Dict[str, Any]) -> Layout:
        """Create a rich layout with multiple sections"""
        layout = Layout()
        
        if len(sections) == 2:
            layout.split_column(
                Layout(sections.get('top', ''), name="top"),
                Layout(sections.get('bottom', ''), name="bottom")
            )
        elif len(sections) == 3:
            layout.split_column(
                Layout(sections.get('header', ''), name="header", size=3),
                Layout(sections.get('body', ''), name="body"),
                Layout(sections.get('footer', ''), name="footer", size=3)
            )
        
        return layout
    
    def show_animated_text(self, text: str, style: str = "white", delay: float = 0.05):
        """Display text with typing animation"""
        if not self.animation_enabled:
            self.console.print(text, style=style)
            return
            
        animated_text = Text()
        for char in text:
            animated_text.append(char, style=style)
            with Live(animated_text, refresh_per_second=20, console=self.console) as live:
                time.sleep(delay)
    
    def show_category_grid(self, categories: Dict[str, Any]):
        """Display categories in a grid layout"""
        grid = Table.grid(padding=1)
        grid.add_column(style="cyan", no_wrap=True)
        grid.add_column(style="magenta", no_wrap=True)
        
        # Convert categories to grid rows
        category_items = list(categories.items())
        for i in range(0, len(category_items), 2):
            row = []
            for j in range(2):
                if i + j < len(category_items):
                    key, cat = category_items[i + j]
                    icon = cat.get('icon', '🔸')
                    name = cat.get('name', key)
                    desc = cat.get('description', '')
                    
                    cell_content = f"{icon} {name}\n{desc[:30]}..."
                    row.append(cell_content)
                else:
                    row.append("")
            
            grid.add_row(*row)
        
        category_panel = Panel(
            grid,
            title="[bold purple]Content Categories[/bold purple]",
            border_style="bright_purple",
            padding=(1, 2)
        )
        
        self.console.print(category_panel)
    
    def show_help_panel(self, help_content: str, title: str = "Help"):
        """Display a help panel with formatted content"""
        help_text = Text()
        
        for line in help_content.split('\n'):
            if line.startswith('•'):
                help_text.append(line + '\n', style="cyan")
            elif line.startswith('#'):
                help_text.append(line + '\n', style="bold magenta")
            else:
                help_text.append(line + '\n', style="white")
        
        help_panel = Panel(
            help_text,
            title=f"[bold yellow]{title}[/bold yellow]",
            border_style="bright_yellow",
            padding=(1, 2)
        )
        
        self.console.print(help_panel)
        self.console.print()
    
    def show_statistics(self, stats: Dict[str, Any]):
        """Display application statistics"""
        stats_table = Table(title="PromptGPT OS Statistics", title_style="bold magenta")
        stats_table.add_column("Metric", style="cyan", no_wrap=True)
        stats_table.add_column("Value", style="green", justify="right")
        
        for metric, value in stats.items():
            stats_table.add_row(metric, str(value))
        
        self.console.print(stats_table)
        self.console.print()
    
    def show_banner(self, message: str, style: str = "bright_yellow"):
        """Display a prominent banner message"""
        banner_text = Text()
        banner_text.append(f"🎉 {message} 🎉", style=style)
        
        banner_panel = Panel(
            Align.center(banner_text),
            border_style=style,
            padding=(1, 4)
        )
        
        self.console.print(banner_panel)
        self.console.print()
    
    def clear_screen(self):
        """Clear the terminal screen"""
        self.console.clear()
    
    def show_separator(self, style: str = "dim white"):
        """Display a visual separator line"""
        separator = "─" * 80
        self.console.print(separator, style=style)
    
    def show_footer(self, message: str = "Thank you for using PromptGPT OS!"):
        """Display application footer"""
        footer_text = Text()
        footer_text.append(message, style="dim cyan")
        
        footer_panel = Panel(
            Align.center(footer_text),
            border_style="dim cyan",
            padding=(1, 2)
        )
        
        self.console.print(footer_panel)
    
    def toggle_animation(self):
        """Toggle animation on/off"""
        self.animation_enabled = not self.animation_enabled
        status = "enabled" if self.animation_enabled else "disabled"
        self.show_info_message(f"Animations {status}")
    
    def set_theme(self, theme_name: str):
        """Set the display theme"""
        # This would integrate with theme settings from config
        self.current_theme = theme_name
        self.show_info_message(f"Theme changed to: {theme_name}")
    
    def show_prompt_preview(self, prompt: str, max_length: int = 500):
        """Show a preview of the generated prompt"""
        if len(prompt) > max_length:
            preview = prompt[:max_length] + "..."
        else:
            preview = prompt
        
        preview_text = Text()
        preview_text.append(preview, style="white")
        
        preview_panel = Panel(
            preview_text,
            title="[bold green]📋 Prompt Preview[/bold green]",
            border_style="bright_green",
            padding=(1, 2)
        )
        
        self.console.print(preview_panel)
        self.console.print()
