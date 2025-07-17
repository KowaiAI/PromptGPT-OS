# PromptGPT OS - AI Content Prompt Generator

A colorful command-line application that generates AI content prompts through interactive questionnaires across multiple categories.

## 🎯 Purpose

PromptGPT OS helps you create detailed, effective prompts for AI content generation across various categories including Code, Images, Music, Text, and Video.

## 🔄 How It Works

1. Select a content category (Code, Image, Music, Text, Video, or Custom)
2. Choose a specific subcategory
3. Answer comprehensive questions about your desired content
4. Get a professionally crafted AI prompt
5. Save or copy your prompt for use with AI tools

**✅ Works Completely Offline** - No internet connection required!

## 📋 Features

- **1,781+ comprehensive questions** across 34+ subcategories
- **Professional prompt templates** for each content type
- **Rich colorful terminal interface** with ASCII art and animations
- **Interactive navigation** with keyboard shortcuts
- **File saving functionality** for generated prompts
- **📋 Copy to Clipboard** - One-click copy with instant clipboard access
- **📚 History Management** - Track your past 10 generated prompts
- **📊 Progress Tracking** - Real-time session statistics and analytics
- **Custom categories & templates** - Create your own content types
- **Settings & template guide** - Full customization support
- **🗄️ Offline Database** - PostgreSQL support for enterprise deployment
- **🎨 Advanced Animations** - Enhanced visual effects and user experience
- **Cross-platform support** (Windows, macOS, Linux)
- **100% Offline Operation** - No internet connection needed
- **🔒 Code Protection** - Watermarked codebase for intellectual property protection

## 🚀 Installation & Setup

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Step-by-Step Installation

1. **Download Project Files**
   - Download the `COMPLETE_PROJECT_FILES.txt`
   - Extract all files according to the directory structure below

2. **Create Directory Structure**
   ```
   promptgpt_os/
   ├── main.py
   ├── pyproject.toml
   ├── project_requirements.txt
   ├── README.md
   ├── config/
   │   └── settings.py
   ├── data/
   │   ├── questions.json
   │   └── templates.json
   ├── ui/
   │   └── display.py
   ├── utils/
   │   ├── navigation.py
   │   ├── prompt_generator.py
   │   └── file_handler.py
   └── generated_prompts/    (will be auto-created)
   ```

3. **Install Dependencies**
   ```bash
   # Option 1: Using pip directly
   pip install rich keyboard
   
   # Option 2: Using requirements file
   pip install -r project_requirements.txt
   ```

4. **Run the Application**
   ```bash
   cd promptgpt_os
   python main.py
   ```

### Troubleshooting Installation
- Ensure Python 3.6+ is installed: `python --version`
- If pip is not found, install it first
- For permission issues on macOS/Linux, try: `pip install --user rich keyboard`
- On Windows, you may need to run as administrator

## 📁 Project Structure

```
promptgpt_os/
├── main.py                    # Main application file
├── pyproject.toml            # Dependencies configuration
├── README.md                 # This file
├── config/
│   └── settings.py          # Settings, colors, ASCII art
├── data/
│   ├── questions.json       # All questions database
│   └── templates.json       # Prompt templates
├── ui/
│   └── display.py          # Display manager
├── utils/
│   ├── navigation.py       # Navigation handler
│   ├── prompt_generator.py # Prompt generation logic
│   └── file_handler.py     # File operations
└── generated_prompts/       # Output directory (auto-created)
```

## 💡 Best Practices for Maximum Prompt Quality

### 🎯 Answer Strategy
- **NEVER use yes/no answers** - Always provide detailed, comprehensive responses
- **The more detail you provide, the better your prompt will be**
- **Elaborate on every aspect** of your requirements and preferences
- **Include examples** when possible to clarify your needs

### 📝 Detailed Answering Guidelines

**Instead of:** "Yes, I need user authentication"
**Use:** "I need a robust user authentication system with email/password login, social media OAuth (Google, Facebook), password reset functionality, email verification, session management, and role-based access control for admin, moderator, and regular user roles."

**Instead of:** "Modern design"
**Use:** "I want a clean, minimalist design following Material Design principles with a blue and white color scheme, sans-serif typography (like Inter or Roboto), subtle shadows, rounded corners, and smooth animations. The design should feel professional yet approachable, similar to modern SaaS applications like Slack or Notion."

### 🔍 Comprehensive Response Framework

1. **Context & Purpose**
   - Explain the broader context of your project
   - Define your target audience demographics and technical skill level
   - Describe the problem you're solving

2. **Specific Requirements**
   - List all functional requirements in detail
   - Specify technical constraints and preferences
   - Include performance and scalability needs

3. **Style & Preferences**
   - Describe visual style, tone, or aesthetic preferences
   - Mention any brand guidelines or existing standards
   - Reference examples or inspirations

4. **Technical Details**
   - Specify frameworks, languages, or tools you prefer
   - Include integration requirements with other systems
   - Mention hosting, deployment, or platform constraints

5. **Success Criteria**
   - Define what success looks like for your project
   - Include measurable goals or outcomes
   - Specify any compliance or accessibility requirements

### ✅ Quality Checklist for Each Answer

Before submitting each response, ask yourself:
- [ ] Did I provide specific examples?
- [ ] Did I explain the "why" behind my requirements?
- [ ] Did I include enough detail for someone unfamiliar with my project?
- [ ] Did I mention my target audience and their needs?
- [ ] Did I specify any constraints or limitations?
- [ ] Could I add more context or background information?

### 🚀 Pro Tips for Better Prompts

- **Reference Examples**: Mention specific websites, apps, or designs you admire
- **Include User Stories**: Describe how users will interact with your content
- **Specify Edge Cases**: Mention special situations or requirements
- **Provide Context**: Explain why certain features or styles are important
- **Think Long-term**: Consider future needs and scalability
- **Be Honest About Constraints**: Mention budget, timeline, or technical limitations

## ⌨️ Navigation

- Use hotkeys (Shift+Letter) for quick navigation
- Type menu options directly
- Use 'back', 'home', 'quit' commands anytime

## 📚 Categories Available

### 🖥️ CODE
- Web Applications
- Mobile Apps
- Scripts
- Backend Systems
- Debugging
- Code Analysis

### 🎨 IMAGE
- Fantasy Art
- Social Media Graphics
- Memes
- Business Graphics
- Marketing Materials
- Infographics
- Character Design

### 🎵 MUSIC
- EDM
- Hip-Hop
- Country
- Pop
- Rock
- Classical
- Jazz
- Folk

### 📝 TEXT
- Blog Posts
- Marketing Copy
- Creative Writing
- Technical Documentation
- Social Media Content
- Email Marketing

### 🎬 VIDEO
- Promotional Videos
- Educational Content
- Entertainment
- Social Media Videos
- Documentaries
- Tutorials

## 🔧 Usage Tips

1. **Start the application**: `python main.py`
2. **Navigate**: Use the main menu to select options
3. **Answer questions**: Be thorough and specific
4. **Review prompts**: Check generated content before use
5. **Save prompts**: Files are automatically saved to `generated_prompts/`

## 🤝 Support

The application includes a built-in README accessible from the main menu that provides detailed usage instructions and navigation help.

## 📝 License

This project is designed for AI content creators and prompt engineers to generate high-quality prompts efficiently.

---

**Version 1.0.0** | Made with ❤️ for AI creators