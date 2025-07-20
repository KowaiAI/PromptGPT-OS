"""
# PromptGPT OS - Prompt Generation Engine
# Developed by: https://github.com/KowaiAI
# Copyright (c) 2025 KowaiAI. All rights reserved.
# 
# This file contains proprietary prompt generation and template processing code.
# Unauthorized copying, modification, or distribution is prohibited.
# 
# Watermark: PROMPTGPT_OS_KOWAI_AI_2025_PROMPT_CORE
"""

import json
import os
from datetime import datetime
from rich.console import Console

console = Console()

class PromptGenerator:
    """Generates AI prompts based on user responses"""
    
    def __init__(self):
        self.questions_data = self.load_questions()
        self.templates_data = self.load_templates()
        self.settings_manager = None  # Will be initialized when needed
    
    def load_questions(self):
        """Load questions from JSON file"""
        try:
            with open('data/questions.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            console.print("[red]Warning: questions.json not found. Using fallback questions.[/red]")
            return self.get_fallback_questions()
        except json.JSONDecodeError:
            console.print("[red]Error: Invalid JSON in questions.json. Using fallback questions.[/red]")
            return self.get_fallback_questions()
    
    def load_templates(self):
        """Load prompt templates from JSON file"""
        try:
            with open('data/templates.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            console.print("[red]Warning: templates.json not found. Using fallback templates.[/red]")
            return self.get_fallback_templates()
        except json.JSONDecodeError:
            console.print("[red]Error: Invalid JSON in templates.json. Using fallback templates.[/red]")
            return self.get_fallback_templates()
    
    def get_questions(self, category, subcategory, is_custom=False):
        """Get questions for specific category and subcategory"""
        if is_custom:
            # Load custom questions
            if self.settings_manager is None:
                from utils.settings_manager import SettingsManager
                self.settings_manager = SettingsManager()
            
            custom_questions = self.settings_manager.get_custom_questions(category, subcategory)
            if custom_questions:
                return custom_questions
            console.print(f"[red]No custom questions found for {category}/{subcategory}[/red]")
            return self.get_generic_questions()
        
        try:
            return self.questions_data[category][subcategory]
        except KeyError:
            console.print(f"[red]No questions found for {category}/{subcategory}[/red]")
            return self.get_generic_questions()
    
    def generate_prompt(self, category, subcategory, user_answers, is_custom=False):
        """Generate final prompt based on user answers"""
        if is_custom:
            # Load custom template
            if self.settings_manager is None:
                from utils.settings_manager import SettingsManager
                self.settings_manager = SettingsManager()
            
            template = self.settings_manager.get_custom_template(category, subcategory)
            if not template:
                template = self.get_generic_template()
        else:
            try:
                template = self.templates_data[category][subcategory]
            except KeyError:
                template = self.get_generic_template()
        
        # Convert answers dict to list for easier processing
        answers_list = []
        questions = self.get_questions(category, subcategory, is_custom)
        
        for i in range(len(questions)):
            answer = user_answers.get(i, "Not specified")
            answers_list.append(answer)
        
        # Replace placeholders in template with answers
        prompt = template
        
        # Basic template variable replacement
        replacements = {
            '{category}': category.title(),
            '{subcategory}': subcategory.title(),
            '{timestamp}': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            '{answers_summary}': self.create_answers_summary(questions, answers_list)
        }
        
        for placeholder, value in replacements.items():
            prompt = prompt.replace(placeholder, str(value))
        
        # Advanced answer integration
        prompt = self.integrate_specific_answers(prompt, questions, answers_list)
        
        return prompt
    
    def create_answers_summary(self, questions, answers):
        """Create a formatted summary of all answers"""
        summary = ""
        for i, (question, answer) in enumerate(zip(questions, answers)):
            if answer and answer.strip() and answer != "Not specified":
                summary += f"\n• {question}: {answer}"
        
        return summary.strip()
    
    def integrate_specific_answers(self, prompt, questions, answers):
        """Integrate specific answers into prompt using intelligent matching"""
        # Look for key concepts in questions and integrate relevant answers
        integrations = []
        
        for i, (question, answer) in enumerate(zip(questions, answers)):
            if not answer or answer.strip() == "" or answer == "Not specified":
                continue
            
            question_lower = question.lower()
            
            # Categorize answers based on question content
            if any(word in question_lower for word in ['style', 'aesthetic', 'look', 'appearance']):
                integrations.append(f"Style requirements: {answer}")
            elif any(word in question_lower for word in ['audience', 'target', 'user', 'viewer']):
                integrations.append(f"Target audience: {answer}")
            elif any(word in question_lower for word in ['purpose', 'goal', 'objective', 'aim']):
                integrations.append(f"Purpose: {answer}")
            elif any(word in question_lower for word in ['feature', 'functionality', 'function']):
                integrations.append(f"Features: {answer}")
            elif any(word in question_lower for word in ['technology', 'tech', 'platform', 'framework']):
                integrations.append(f"Technology: {answer}")
            elif any(word in question_lower for word in ['color', 'colour', 'palette']):
                integrations.append(f"Color scheme: {answer}")
            elif any(word in question_lower for word in ['size', 'length', 'duration', 'dimension']):
                integrations.append(f"Size specifications: {answer}")
            elif any(word in question_lower for word in ['tone', 'mood', 'feeling', 'emotion']):
                integrations.append(f"Tone/Mood: {answer}")
        
        # Add integration section to prompt
        if integrations:
            integration_text = "\n\nSpecific Requirements:\n" + "\n".join([f"- {item}" for item in integrations])
            prompt += integration_text
        
        return prompt
    
    def get_fallback_questions(self):
        """Provide fallback questions if JSON file is not available"""
        return {
            "code": {
                "web_app": [
                    "What is the primary purpose of your web application?",
                    "Who is your target audience?",
                    "What main features should the application have?",
                    "What technology stack do you prefer?",
                    "Do you need user authentication?",
                    "What is the expected user interface style?",
                    "Do you need a database? What type?",
                    "What are the performance requirements?",
                    "Do you need responsive design for mobile devices?",
                    "What are the security considerations?"
                ]
            },
            "image": {
                "fantasy": [
                    "What is the main subject of the image?",
                    "What style of fantasy art do you prefer?",
                    "What is the setting or environment?",
                    "What mood or atmosphere should the image convey?",
                    "What colors should be prominent?",
                    "What level of detail do you want?",
                    "Should there be any characters? Describe them.",
                    "What lighting conditions do you want?",
                    "What size/resolution do you need?",
                    "Any specific artistic influences or references?"
                ]
            }
        }
    
    def get_fallback_templates(self):
        """Provide fallback templates if JSON file is not available"""
        return {
            "code": {
                "web_app": """Create a {subcategory} with the following specifications:

{answers_summary}

Please ensure the code is:
- Well-documented and clean
- Following best practices for {category}
- Scalable and maintainable
- Secure and optimized

Generated on: {timestamp}"""
            },
            "image": {
                "fantasy": """Generate a {subcategory} image with these characteristics:

{answers_summary}

Style: Professional digital art
Quality: High resolution, detailed
Format: Suitable for digital use

Generated on: {timestamp}"""
            }
        }
    
    def get_generic_questions(self):
        """Generic questions when specific ones aren't available"""
        return [
            "What is the main purpose or goal of your content?",
            "Who is your target audience?",
            "What style or tone do you prefer?",
            "What are the key requirements or specifications?",
            "Are there any constraints or limitations?",
            "What is the intended use or application?",
            "Do you have any specific preferences for the output?",
            "What makes this content unique or special?",
            "Are there any examples or references you'd like to follow?",
            "What success criteria should the AI consider?"
        ]
    
    def get_generic_template(self):
        """Generic template when specific ones aren't available"""
        return """Create {category} content of type {subcategory} with the following specifications:

{answers_summary}

Please ensure the output is:
- High quality and professional
- Tailored to the specified requirements
- Creative and engaging
- Technically sound

Generated on: {timestamp}"""
