#!/usr/bin/env python3
"""
# PromptGPT OS - Advanced Animation System
# Developed by: https://github.com/KowaiAI
# Copyright (c) 2025 KowaiAI. All rights reserved.
# 
# This file contains proprietary animation and visual effects code.
# Unauthorized copying, modification, or distribution is prohibited.
# 
# Watermark: PROMPTGPT_OS_KOWAI_AI_2025_ANIMATION_CORE
"""

import time
import threading
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn
from rich.text import Text
from rich.panel import Panel
from rich.align import Align
import random

console = Console()

class AnimationManager:
    """Advanced animation system with progress tracking and visual effects"""
    
    def __init__(self):
        self.console = console
        self.animation_enabled = True
        self.current_progress = None
        
    def typewriter_effect(self, text, delay=0.03, style="white"):
        """Animated typewriter effect for text display"""
        if not self.animation_enabled:
            console.print(text, style=style)
            return
            
        for char in text:
            console.print(char, style=style, end="")
            time.sleep(delay)
        console.print()
    
    def loading_spinner(self, message, duration=2.0):
        """Animated loading spinner with message"""
        if not self.animation_enabled:
            console.print(f"[cyan]{message}[/cyan]")
            time.sleep(0.5)
            return
            
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task(message, total=None)
            time.sleep(duration)
    
    def progress_bar(self, items, description="Processing"):
        """Animated progress bar for processing items"""
        if not self.animation_enabled:
            console.print(f"[cyan]{description} {len(items)} items...[/cyan]")
            return items
            
        with Progress(
            TextColumn("[bold blue]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeRemainingColumn(),
            console=console
        ) as progress:
            task = progress.add_task(description, total=len(items))
            
            processed_items = []
            for item in items:
                time.sleep(0.1)  # Simulate processing
                processed_items.append(item)
                progress.update(task, advance=1)
            
            return processed_items
    
    def slide_in_panel(self, content, title, border_style="cyan", delay=0.1):
        """Animated panel that slides in character by character"""
        if not self.animation_enabled:
            panel = Panel(content, title=title, border_style=border_style)
            console.print(panel)
            return
            
        # Create the panel
        panel = Panel(content, title=title, border_style=border_style)
        
        # Simulate slide-in effect
        for i in range(3):
            console.print("  " * (3-i), end="")
            time.sleep(delay)
        
        console.print(panel)
    
    def fade_in_text(self, text, steps=5, delay=0.2):
        """Text that fades in gradually"""
        if not self.animation_enabled:
            console.print(text)
            return
            
        for i in range(steps + 1):
            alpha = i / steps
            if alpha < 0.3:
                style = "dim white"
            elif alpha < 0.6:
                style = "white"
            else:
                style = "bold white"
            
            console.clear()
            console.print(text, style=style)
            time.sleep(delay)
    
    def pulse_text(self, text, pulses=3, delay=0.5):
        """Text that pulses with changing brightness"""
        if not self.animation_enabled:
            console.print(text)
            return
            
        styles = ["dim cyan", "cyan", "bold cyan", "bright_cyan"]
        
        for _ in range(pulses):
            for style in styles + styles[::-1]:
                console.clear()
                console.print(text, style=style)
                time.sleep(delay / len(styles))
    
    def rainbow_text(self, text, delay=0.1):
        """Animated rainbow text effect"""
        if not self.animation_enabled:
            console.print(text)
            return
            
        colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
        
        for i in range(len(colors)):
            colored_text = Text()
            for j, char in enumerate(text):
                color_index = (i + j) % len(colors)
                colored_text.append(char, style=colors[color_index])
            
            console.clear()
            console.print(colored_text)
            time.sleep(delay)
    
    def matrix_effect(self, lines=10, duration=3.0):
        """Matrix-style falling text effect"""
        if not self.animation_enabled:
            return
            
        chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        
        end_time = time.time() + duration
        while time.time() < end_time:
            console.clear()
            for _ in range(lines):
                line = "".join(random.choice(chars) for _ in range(80))
                console.print(line, style="green")
            time.sleep(0.1)
    
    def celebration_animation(self):
        """Success celebration animation"""
        if not self.animation_enabled:
            console.print("[bold green]✅ Success![/bold green]")
            return
            
        # Animated celebration
        celebration_text = "🎉 SUCCESS! 🎉"
        
        # Pulse effect
        for _ in range(3):
            console.print(celebration_text, style="bold green")
            time.sleep(0.3)
            console.print(" " * len(celebration_text))
            time.sleep(0.2)
        
        # Final display
        console.print(celebration_text, style="bold green")

class ProgressTracker:
    """Advanced progress tracking system with analytics"""
    
    def __init__(self):
        self.session_stats = {
            'categories_visited': set(),
            'subcategories_visited': set(),
            'questions_answered': 0,
            'prompts_generated': 0,
            'templates_used': set(),
            'session_start': time.time(),
            'custom_categories_created': 0,
            'clipboard_copies': 0,
            'files_saved': 0
        }
        
    def track_category_visit(self, category):
        """Track category selection"""
        self.session_stats['categories_visited'].add(category)
    
    def track_subcategory_visit(self, subcategory):
        """Track subcategory selection"""
        self.session_stats['subcategories_visited'].add(subcategory)
    
    def track_question_answered(self):
        """Track question answered"""
        self.session_stats['questions_answered'] += 1
    
    def track_prompt_generated(self, template_used=None):
        """Track prompt generation"""
        self.session_stats['prompts_generated'] += 1
        if template_used:
            self.session_stats['templates_used'].add(template_used)
    
    def track_custom_category_created(self):
        """Track custom category creation"""
        self.session_stats['custom_categories_created'] += 1
    
    def track_clipboard_copy(self):
        """Track clipboard usage"""
        self.session_stats['clipboard_copies'] += 1
    
    def track_file_saved(self):
        """Track file saves"""
        self.session_stats['files_saved'] += 1
    
    def get_session_summary(self):
        """Get comprehensive session summary"""
        session_duration = time.time() - self.session_stats['session_start']
        
        return {
            'duration_minutes': round(session_duration / 60, 2),
            'categories_explored': len(self.session_stats['categories_visited']),
            'subcategories_explored': len(self.session_stats['subcategories_visited']),
            'questions_answered': self.session_stats['questions_answered'],
            'prompts_generated': self.session_stats['prompts_generated'],
            'unique_templates_used': len(self.session_stats['templates_used']),
            'productivity_score': self._calculate_productivity_score(),
            'custom_categories_created': self.session_stats['custom_categories_created'],
            'clipboard_copies': self.session_stats['clipboard_copies'],
            'files_saved': self.session_stats['files_saved']
        }
    
    def _calculate_productivity_score(self):
        """Calculate productivity score based on activity"""
        score = 0
        score += self.session_stats['prompts_generated'] * 10
        score += self.session_stats['questions_answered'] * 2
        score += len(self.session_stats['categories_visited']) * 5
        score += self.session_stats['custom_categories_created'] * 15
        score += self.session_stats['clipboard_copies'] * 3
        score += self.session_stats['files_saved'] * 5
        
        return min(score, 100)  # Cap at 100
    
    def display_progress_dashboard(self):
        """Display animated progress dashboard"""
        stats = self.get_session_summary()
        
        dashboard_text = f"""
📊 Session Statistics

⏱️  Session Duration: {stats['duration_minutes']} minutes
🎯 Prompts Generated: {stats['prompts_generated']}
❓ Questions Answered: {stats['questions_answered']}
📂 Categories Explored: {stats['categories_explored']}
🔧 Custom Categories: {stats['custom_categories_created']}
📋 Clipboard Copies: {stats['clipboard_copies']}
💾 Files Saved: {stats['files_saved']}

🏆 Productivity Score: {stats['productivity_score']}/100
        """
        
        panel = Panel(
            dashboard_text,
            title="[bold cyan]📈 PROGRESS DASHBOARD 📈[/bold cyan]",
            border_style="cyan",
            padding=(1, 2)
        )
        
        console.print(panel)

# Global instances
animation_manager = AnimationManager()
progress_tracker = ProgressTracker()