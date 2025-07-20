"""
Template Guide for PromptGPT OS
Provides comprehensive guidance on creating custom templates
"""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns

console = Console()

def show_template_guide():
    """Display comprehensive template creation guide"""
    console.clear()
    
    # Header
    header_text = Text()
    header_text.append("📚 TEMPLATE CREATION GUIDE 📚", style="bold bright_blue")
    header_panel = Panel(
        header_text,
        title="[bold bright_blue]Learn to Create Perfect Templates[/bold bright_blue]",
        border_style="bright_blue",
        padding=(1, 2)
    )
    console.print(header_panel)
    console.print()
    
    # What are templates section
    what_text = Text()
    what_text.append("What are Templates?\n\n", style="bold yellow")
    what_text.append("Templates are text patterns that turn your answers into professional AI prompts. ", style="white")
    what_text.append("They use placeholders like {answer_1} that get replaced with your actual answers.\n\n", style="white")
    what_text.append("Example:\n", style="bold cyan")
    what_text.append("Template: 'Create a {answer_1} website for {answer_2} with {answer_3} features.'\n", style="dim green")
    what_text.append("Result: 'Create a business website for restaurants with online ordering features.'", style="bright_green")
    
    what_panel = Panel(
        what_text,
        title="[bold yellow]Understanding Templates[/bold yellow]",
        border_style="yellow",
        padding=(1, 2)
    )
    
    # How to create section
    how_text = Text()
    how_text.append("How to Create Templates:\n\n", style="bold cyan")
    how_text.append("1. Write your prompt in plain English\n", style="white")
    how_text.append("2. Replace specific details with placeholders: {answer_1}, {answer_2}, etc.\n", style="white")
    how_text.append("3. The numbers match your question order (question 1 = {answer_1})\n", style="white")
    how_text.append("4. Include context and requirements for the AI\n\n", style="white")
    how_text.append("Template Structure:\n", style="bold magenta")
    how_text.append("• Introduction: What you want the AI to create\n", style="white")
    how_text.append("• Requirements: Specific details from user answers\n", style="white")
    how_text.append("• Style: How it should look/feel/work\n", style="white")
    how_text.append("• Output: What format you want back", style="white")
    
    how_panel = Panel(
        how_text,
        title="[bold cyan]Creating Templates[/bold cyan]",
        border_style="cyan",
        padding=(1, 2)
    )
    
    # Display first row
    console.print(Columns([what_panel, how_panel], equal=True))
    console.print()
    
    # Examples section
    examples_text = Text()
    examples_text.append("Template Examples:\n\n", style="bold green")
    
    examples_text.append("📱 Mobile App Template:\n", style="bold blue")
    examples_text.append("'Create a {answer_1} mobile app for {answer_2}. The app should have these main features: {answer_3}. ", style="dim white")
    examples_text.append("Target users are {answer_4}. Design style should be {answer_5}. Include {answer_6} payment methods if applicable.'\n\n", style="dim white")
    
    examples_text.append("🎨 Image Template:\n", style="bold magenta")
    examples_text.append("'Generate a {answer_1} style image featuring {answer_2}. The mood should be {answer_3} with {answer_4} colors. ", style="dim white")
    examples_text.append("Setting: {answer_5}. Include these elements: {answer_6}. Art style: {answer_7}.'\n\n", style="dim white")
    
    examples_text.append("📝 Blog Post Template:\n", style="bold yellow")
    examples_text.append("'Write a {answer_1} blog post about {answer_2} for {answer_3} audience. Tone: {answer_4}. ", style="dim white")
    examples_text.append("Include these key points: {answer_5}. Length: {answer_6} words. Add a compelling {answer_7} call-to-action.'", style="dim white")
    
    examples_panel = Panel(
        examples_text,
        title="[bold green]Real Template Examples[/bold green]",
        border_style="green",
        padding=(1, 2)
    )
    
    # Tips section
    tips_text = Text()
    tips_text.append("Pro Tips for Great Templates:\n\n", style="bold red")
    tips_text.append("✓ Be specific: Use clear, detailed prompts\n", style="green")
    tips_text.append("✓ Use context: Explain what you want the AI to understand\n", style="green")
    tips_text.append("✓ Include constraints: Set limits (word count, style, format)\n", style="green")
    tips_text.append("✓ Add examples: 'Like [example]' helps AI understand\n", style="green")
    tips_text.append("✓ Test variations: Try different phrasings\n\n", style="green")
    
    tips_text.append("Common Mistakes to Avoid:\n\n", style="bold orange3")
    tips_text.append("✗ Too vague: 'Create something good'\n", style="red")
    tips_text.append("✗ Missing placeholders: Forgetting to use {answer_X}\n", style="red")
    tips_text.append("✗ Wrong numbers: {answer_5} for question 3\n", style="red")
    tips_text.append("✗ No structure: Just throwing requirements together\n", style="red")
    tips_text.append("✗ Too complex: Trying to do everything in one prompt", style="red")
    
    tips_panel = Panel(
        tips_text,
        title="[bold red]Tips & Best Practices[/bold red]",
        border_style="red",
        padding=(1, 2)
    )
    
    # Display second row
    console.print(Columns([examples_panel, tips_panel], equal=True))
    console.print()
    
    # File format section
    format_text = Text()
    format_text.append("Template File Format:\n\n", style="bold bright_magenta")
    format_text.append("Save your templates as .txt files with this structure:\n\n", style="white")
    format_text.append("my_template.txt:\n", style="bold cyan")
    format_text.append("────────────────────────\n", style="dim white")
    format_text.append("Create a {answer_1} for {answer_2}.\n\n", style="bright_white")
    format_text.append("Requirements:\n", style="bright_white")
    format_text.append("- Style: {answer_3}\n", style="bright_white")
    format_text.append("- Features: {answer_4}\n", style="bright_white")
    format_text.append("- Target audience: {answer_5}\n\n", style="bright_white")
    format_text.append("Make it {answer_6} and ensure it {answer_7}.\n", style="bright_white")
    format_text.append("────────────────────────\n\n", style="dim white")
    format_text.append("💡 The entire file content becomes your template!", style="yellow")
    
    format_panel = Panel(
        format_text,
        title="[bold bright_magenta]File Format Guide[/bold bright_magenta]",
        border_style="bright_magenta",
        padding=(1, 2),
        width=60
    )
    
    # Advanced tips
    advanced_text = Text()
    advanced_text.append("Advanced Techniques:\n\n", style="bold bright_cyan")
    advanced_text.append("🔥 Conditional Text:\n", style="bold yellow")
    advanced_text.append("'Include payment features if this is an e-commerce {answer_1}.'\n\n", style="white")
    
    advanced_text.append("🎯 Specific Instructions:\n", style="bold yellow")
    advanced_text.append("'Generate exactly 5 {answer_1} options in bullet format.'\n\n", style="white")
    
    advanced_text.append("🚀 Multi-step Prompts:\n", style="bold yellow")
    advanced_text.append("'First, analyze {answer_1}. Then create {answer_2} based on that analysis.'\n\n", style="white")
    
    advanced_text.append("🎨 Style References:\n", style="bold yellow")
    advanced_text.append("'In the style of {answer_1}, create {answer_2} that feels like {answer_3}.'\n\n", style="white")
    
    advanced_text.append("📊 Output Formatting:\n", style="bold yellow")
    advanced_text.append("'Provide results as: Title, Description, 3 key features for {answer_1}.'", style="white")
    
    advanced_panel = Panel(
        advanced_text,
        title="[bold bright_cyan]Advanced Template Techniques[/bold bright_cyan]",
        border_style="bright_cyan",
        padding=(1, 2),
        width=60
    )
    
    # Display third row
    console.print(Columns([format_panel, advanced_panel], equal=True))
    console.print()
    
    # Footer with navigation
    footer_text = Text()
    footer_text.append("Ready to create your own templates? Use the Settings menu to add custom categories and upload your template files!", style="bold bright_green")
    
    footer_panel = Panel(
        footer_text,
        title="[bold bright_green]🚀 Get Started Now![/bold bright_green]",
        border_style="bright_green",
        padding=(1, 2)
    )
    
    console.print(footer_panel)
    console.print()
    
    # Navigation
    choice = console.input("[bold cyan]Press Enter to return to main menu: [/bold cyan]")
    return "main_menu"