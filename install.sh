#!/bin/bash
# PromptGPT OS Installation Script

echo "🚀 Installing PromptGPT OS..."
echo ""

# Check Python version
python_version=$(python3 --version 2>&1)
if [[ $? -eq 0 ]]; then
    echo "✓ Python found: $python_version"
else
    echo "❌ Python 3 not found. Please install Python 3.6+ first."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r project_requirements.txt

if [[ $? -eq 0 ]]; then
    echo "✓ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Create output directory
mkdir -p generated_prompts

echo ""
echo "🎉 Installation complete!"
echo ""
echo "To run PromptGPT OS:"
echo "  python3 main.py"
echo ""
echo "For help, see README.md"
