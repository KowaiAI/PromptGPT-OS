"""
# PromptGPT OS - Settings Management System
# Developed by: https://github.com/KowaiAI
# Copyright (c) 2025 KowaiAI. All rights reserved.
# 
# This file contains proprietary settings and customization code.
# Unauthorized copying, modification, or distribution is prohibited.
# 
# Watermark: PROMPTGPT_OS_KOWAI_AI_2025_SETTINGS_CORE
"""

import json
import os
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text

console = Console()

class SettingsManager:
    """Manages custom categories, questions, and templates"""
    
    def __init__(self):
        self.custom_data_dir = Path("custom_data")
        self.custom_categories_file = self.custom_data_dir / "custom_categories.json"
        self.custom_questions_file = self.custom_data_dir / "custom_questions.json"
        self.custom_templates_file = self.custom_data_dir / "custom_templates.json"
        
        # Create custom data directory if it doesn't exist
        self.custom_data_dir.mkdir(exist_ok=True)
        
        # Initialize custom files if they don't exist
        self._initialize_custom_files()
    
    def _initialize_custom_files(self):
        """Initialize custom data files with empty structures"""
        if not self.custom_categories_file.exists():
            with open(self.custom_categories_file, 'w') as f:
                json.dump({}, f, indent=2)
        
        if not self.custom_questions_file.exists():
            with open(self.custom_questions_file, 'w') as f:
                json.dump({}, f, indent=2)
        
        if not self.custom_templates_file.exists():
            with open(self.custom_templates_file, 'w') as f:
                json.dump({}, f, indent=2)
    
    def load_custom_categories(self):
        """Load custom categories from file"""
        try:
            with open(self.custom_categories_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            console.print(f"[red]Error loading custom categories: {e}[/red]")
            return {}
    
    def load_custom_questions(self):
        """Load custom questions from file"""
        try:
            with open(self.custom_questions_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            console.print(f"[red]Error loading custom questions: {e}[/red]")
            return {}
    
    def load_custom_templates(self):
        """Load custom templates from file"""
        try:
            with open(self.custom_templates_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            console.print(f"[red]Error loading custom templates: {e}[/red]")
            return {}
    
    def save_custom_categories(self, categories):
        """Save custom categories to file"""
        try:
            with open(self.custom_categories_file, 'w') as f:
                json.dump(categories, f, indent=2)
            return True
        except Exception as e:
            console.print(f"[red]Error saving custom categories: {e}[/red]")
            return False
    
    def save_custom_questions(self, questions):
        """Save custom questions to file"""
        try:
            with open(self.custom_questions_file, 'w') as f:
                json.dump(questions, f, indent=2)
            return True
        except Exception as e:
            console.print(f"[red]Error saving custom questions: {e}[/red]")
            return False
    
    def save_custom_templates(self, templates):
        """Save custom templates to file"""
        try:
            with open(self.custom_templates_file, 'w') as f:
                json.dump(templates, f, indent=2)
            return True
        except Exception as e:
            console.print(f"[red]Error saving custom templates: {e}[/red]")
            return False
    
    def add_custom_category(self, category_name, subcategories, description="Custom category"):
        """Add a new custom category with subcategories"""
        categories = self.load_custom_categories()
        
        # Create category structure
        categories[category_name] = {
            'name': category_name.title(),
            'description': description,
            'icon': '🔧',
            'color': 'bright_magenta',
            'subcategories': subcategories
        }
        
        return self.save_custom_categories(categories)
    
    def upload_questions_from_file(self, file_path, category, subcategory):
        """Upload questions from a text file (max 50 questions)"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Process lines and filter out empty ones
            questions = []
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):  # Skip empty lines and comments
                    questions.append(line)
            
            # Limit to 50 questions
            if len(questions) > 50:
                console.print(f"[yellow]Warning: File contains {len(questions)} questions. Only first 50 will be used.[/yellow]")
                questions = questions[:50]
            
            if not questions:
                console.print("[red]No valid questions found in file.[/red]")
                return False
            
            # Load existing custom questions
            custom_questions = self.load_custom_questions()
            
            # Add category if it doesn't exist
            if category not in custom_questions:
                custom_questions[category] = {}
            
            # Add questions to subcategory
            custom_questions[category][subcategory] = questions
            
            # Save updated questions
            if self.save_custom_questions(custom_questions):
                console.print(f"[green]Successfully uploaded {len(questions)} questions for {category} > {subcategory}[/green]")
                return True
            
        except Exception as e:
            console.print(f"[red]Error uploading questions: {e}[/red]")
            return False
    
    def upload_template_from_file(self, file_path, category, subcategory):
        """Upload template from a text file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                template_content = f.read().strip()
            
            if not template_content:
                console.print("[red]Template file is empty.[/red]")
                return False
            
            # Load existing custom templates
            custom_templates = self.load_custom_templates()
            
            # Add category if it doesn't exist
            if category not in custom_templates:
                custom_templates[category] = {}
            
            # Add template to subcategory
            custom_templates[category][subcategory] = template_content
            
            # Save updated templates
            if self.save_custom_templates(custom_templates):
                console.print(f"[green]Successfully uploaded template for {category} > {subcategory}[/green]")
                return True
            
        except Exception as e:
            console.print(f"[red]Error uploading template: {e}[/red]")
            return False
    
    def list_custom_categories(self):
        """List all custom categories"""
        categories = self.load_custom_categories()
        if not categories:
            console.print("[yellow]No custom categories found.[/yellow]")
            return []
        
        return list(categories.keys())
    
    def delete_custom_category(self, category_name):
        """Delete a custom category and its associated data"""
        try:
            # Remove from categories
            categories = self.load_custom_categories()
            if category_name in categories:
                del categories[category_name]
                self.save_custom_categories(categories)
            
            # Remove from questions
            questions = self.load_custom_questions()
            if category_name in questions:
                del questions[category_name]
                self.save_custom_questions(questions)
            
            # Remove from templates
            templates = self.load_custom_templates()
            if category_name in templates:
                del templates[category_name]
                self.save_custom_templates(templates)
            
            console.print(f"[green]Successfully deleted custom category: {category_name}[/green]")
            return True
            
        except Exception as e:
            console.print(f"[red]Error deleting custom category: {e}[/red]")
            return False
    
    def get_custom_questions(self, category, subcategory):
        """Get questions for a custom category/subcategory"""
        questions = self.load_custom_questions()
        return questions.get(category, {}).get(subcategory, [])
    
    def get_custom_template(self, category, subcategory):
        """Get template for a custom category/subcategory"""
        templates = self.load_custom_templates()
        return templates.get(category, {}).get(subcategory, "")