"""
# PromptGPT OS - Configuration Management System
# Developed by: https://github.com/KowaiAI
# Copyright (c) 2025 KowaiAI. All rights reserved.
# 
# This file contains proprietary configuration and styling code.
# Unauthorized copying, modification, or distribution is prohibited.
# 
# Watermark: PROMPTGPT_OS_KOWAI_AI_2025_CONFIG_CORE
"""

# Color scheme for the application
COLORS = {
    'primary': 'bright_magenta',
    'secondary': 'bright_cyan', 
    'accent': 'bright_yellow',
    'success': 'bright_green',
    'warning': 'orange1',
    'error': 'bright_red',
    'info': 'bright_blue',
    'text': 'white',
    'muted': 'dim white'
}

# ASCII Header Art - Compact Version
ASCII_HEADER = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║    ██████╗ ██████╗  ██████╗ ███╗   ███╗██████╗ ████████╗     ║
║    ██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝     ║
║    ██████╔╝██████╔╝██║   ██║██╔████╔██║██████╔╝   ██║        ║
║    ██╔═══╝ ██╔══██╗██║   ██║██║╚██╔╝██║██╔═══╝    ██║        ║
║    ██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║        ██║        ║
║    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝        ║
║                                                               ║
║         ██████╗ ██████╗ ████████╗    ██████╗ ███████╗        ║
║        ██╔════╝ ██╔══██╗╚══██╔══╝   ██╔═══██╗██╔════╝        ║
║        ██║  ███╗██████╔╝   ██║      ██║   ██║███████╗        ║
║        ██║   ██║██╔═══╝    ██║      ██║   ██║╚════██║        ║
║        ╚██████╔╝██║        ██║      ╚██████╔╝███████║        ║
║         ╚═════╝ ╚═╝        ╚═╝       ╚═════╝ ╚══════╝        ║
║                                                               ║
║              ✨ AI Content Prompt Generator ✨                ║
║                Create Perfect Prompts Every Time              ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""

# Category definitions with metadata
CATEGORIES = {
    'code': {
        'name': 'Code',
        'description': 'Generate prompts for programming and development tasks',
        'icon': '💻',
        'color': 'bright_green',
        'subcategories': [
            'web_app',
            'mobile_app', 
            'script',
            'backend',
            'debug',
            'code_analysis'
        ]
    },
    'image': {
        'name': 'Image',
        'description': 'Create prompts for visual and graphic content',
        'icon': '🎨',
        'color': 'bright_magenta',
        'subcategories': [
            'fantasy',
            'social_media',
            'meme',
            'business',
            'marketing',
            'infographic',
            'character'
        ]
    },
    'music': {
        'name': 'Music',
        'description': 'Design prompts for audio and musical compositions',
        'icon': '🎵',
        'color': 'bright_cyan',
        'subcategories': [
            'edm',
            'hip_hop',
            'country',
            'rnb_soul',
            'experimental',
            'vocal',
            'commercial',
            'voice_over'
        ]
    },
    'text': {
        'name': 'Text',
        'description': 'Build prompts for written content and copywriting',
        'icon': '📝',
        'color': 'bright_yellow',
        'subcategories': [
            'business',
            'blog',
            'social_media',
            'academic',
            'fiction',
            'nonfiction',
            'marketing'
        ]
    },
    'video': {
        'name': 'Video',
        'description': 'Develop prompts for video content and cinematography',
        'icon': '🎬',
        'color': 'bright_blue',
        'subcategories': [
            'documentary',
            'commercial',
            'tutorial',
            'entertainment',
            'explainer',
            'social_media'
        ]
    }
}

# Application constants
APP_NAME = "PromptGPT OS"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "AI Content Prompt Generator - Create Perfect Prompts Every Time"

# File paths
OUTPUT_DIR = "generated_prompts"
QUESTIONS_FILE = "data/questions.json"
TEMPLATES_FILE = "data/templates.json"

# Default settings
DEFAULT_PROMPT_LENGTH = "comprehensive"
DEFAULT_STYLE = "professional"
DEFAULT_AUDIENCE = "general"

# Hotkey mappings
HOTKEYS = {
    'start': 'shift+s',
    'readme': 'shift+r',
    'quit': 'shift+q',
    'home': 'shift+h',
    'back': 'shift+b',
    'next': 'shift+n',
    'save': 'shift+ctrl+s'
}

# Navigation commands
NAV_COMMANDS = [
    'start', 'readme', 'quit', 'home', 'back', 'next', 'restart', 'save'
]

# Platform-specific settings
PLATFORMS = {
    'terminal_width': 120,
    'max_line_length': 100,
    'animation_speed': 0.05,
    'typing_speed': 0.02
}

# Question categories metadata
QUESTION_CATEGORIES = {
    'purpose': 'Understanding the goal and objective',
    'audience': 'Identifying target users and demographics',
    'style': 'Defining aesthetic and presentation preferences',
    'technical': 'Specifying technical requirements and constraints',
    'content': 'Describing the actual content and messaging',
    'functionality': 'Outlining features and interactive elements',
    'constraints': 'Noting limitations and boundaries',
    'context': 'Providing background and situational information'
}

# Theme configurations
THEMES = {
    'default': {
        'primary': 'bright_magenta',
        'secondary': 'bright_cyan',
        'accent': 'bright_yellow',
        'background': 'black'
    },
    'cyberpunk': {
        'primary': 'bright_green',
        'secondary': 'magenta',
        'accent': 'cyan',
        'background': 'black'
    },
    'ocean': {
        'primary': 'bright_blue',
        'secondary': 'cyan',
        'accent': 'white',
        'background': 'blue'
    }
}

# Error messages
ERROR_MESSAGES = {
    'file_not_found': "Required file not found: {filename}",
    'invalid_input': "Invalid input provided. Please try again.",
    'json_parse_error': "Error parsing JSON file: {filename}",
    'save_error': "Error saving file: {error}",
    'permission_error': "Permission denied when accessing: {filename}",
    'unexpected_error': "An unexpected error occurred: {error}"
}

# Success messages
SUCCESS_MESSAGES = {
    'prompt_generated': "✅ Prompt generated successfully!",
    'file_saved': "💾 File saved to: {filename}",
    'session_restored': "🔄 Session restored successfully",
    'export_complete': "📤 Export completed: {filename}"
}

# Help text
HELP_TEXT = {
    'navigation': """
Available Navigation Commands:
• start/s - Begin creating prompts
• readme/r - View user guide and tips
• home/h - Return to main menu
• back/b - Go to previous page
• next/n - Continue to next question
• restart - Start questionnaire over
• quit/q - Exit application
• save - Save current prompt
""",
    'hotkeys': """
Keyboard Shortcuts:
• Shift+S - Start
• Shift+R - Readme
• Shift+Q - Quit
• Shift+H - Home
• Shift+B - Back
• Shift+N - Next
• Shift+Ctrl+S - Save
""",
    'tips': """
Tips for Better Prompts:
• Be specific and detailed in your answers
• Include context about your target audience
• Mention style preferences and constraints
• Specify technical requirements when relevant
• Provide examples or references when possible
• Consider the end use case for your content
"""
}

# Validation patterns
VALIDATION_PATTERNS = {
    'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    'url': r'^https?://(?:[-\w.])+(?:\:[0-9]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:\#(?:[\w.])*)?)?$',
    'filename': r'^[a-zA-Z0-9_\-\. ]+$'
}

# File extensions
SUPPORTED_FORMATS = {
    'text': ['.txt', '.md', '.rtf'],
    'document': ['.doc', '.docx', '.pdf'],
    'data': ['.json', '.csv', '.xml'],
    'archive': ['.zip', '.tar.gz']
}

# Analytics events
ANALYTICS_EVENTS = {
    'app_start': 'application_started',
    'category_selected': 'category_selected',
    'subcategory_selected': 'subcategory_selected',
    'questionnaire_completed': 'questionnaire_completed',
    'prompt_generated': 'prompt_generated',
    'prompt_saved': 'prompt_saved',
    'app_exit': 'application_exited'
}
