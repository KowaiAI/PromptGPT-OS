#!/usr/bin/env python3
"""
System compatibility check for PromptGPT OS
Verifies all dependencies and system requirements
"""

import sys
import platform
import subprocess

def check_python_version():
    """Check Python version compatibility"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print(f"❌ Python {version.major}.{version.minor} is not supported")
        print("✅ Required: Python 3.6 or higher")
        return False
    else:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
        return True

def check_dependencies():
    """Check all required dependencies"""
    dependencies = {
        'rich': 'Terminal UI framework',
        'keyboard': 'Keyboard input handling (optional)',
        'pyperclip': 'Clipboard functionality (optional)'
    }
    
    missing = []
    available = []
    
    for dep, description in dependencies.items():
        try:
            __import__(dep)
            available.append(f"✅ {dep} - {description}")
        except ImportError:
            if dep in ['keyboard', 'pyperclip']:
                available.append(f"⚠️  {dep} - {description} (Optional - will continue without)")
            else:
                missing.append(f"❌ {dep} - {description}")
    
    for item in available:
        print(item)
    
    for item in missing:
        print(item)
    
    return len(missing) == 0

def check_terminal_support():
    """Check terminal compatibility"""
    print("\n🖥️  Terminal Compatibility:")
    print(f"✅ Platform: {platform.system()} {platform.release()}")
    
    # Check if running in a proper terminal
    if hasattr(sys.stdout, 'isatty') and sys.stdout.isatty():
        print("✅ Interactive terminal detected")
    else:
        print("⚠️  Non-interactive terminal detected")
    
    # Check terminal encoding
    encoding = sys.stdout.encoding or 'unknown'
    print(f"✅ Terminal encoding: {encoding}")
    
    return True

def check_file_permissions():
    """Check file system permissions"""
    import os
    import tempfile
    
    print("\n📁 File System Permissions:")
    
    # Check write permissions in current directory
    try:
        test_file = 'test_write_permission.tmp'
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        print("✅ Write permissions in current directory")
    except:
        print("❌ No write permissions in current directory")
        return False
    
    # Check if generated_prompts directory can be created
    try:
        os.makedirs('generated_prompts', exist_ok=True)
        print("✅ Can create generated_prompts directory")
    except:
        print("❌ Cannot create generated_prompts directory")
        return False
    
    return True

def run_full_check():
    """Run complete system compatibility check"""
    print("🔍 PromptGPT OS - System Compatibility Check")
    print("=" * 50)
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Terminal Support", check_terminal_support),
        ("File Permissions", check_file_permissions)
    ]
    
    all_passed = True
    
    for check_name, check_func in checks:
        print(f"\n{check_name}:")
        try:
            result = check_func()
            if not result:
                all_passed = False
        except Exception as e:
            print(f"❌ Error during {check_name} check: {e}")
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All checks passed! PromptGPT OS is ready to run.")
        print("\n📋 To start the application:")
        print("   python main.py")
    else:
        print("⚠️  Some issues detected. Please resolve them before running.")
        print("\n📋 To install missing dependencies:")
        print("   pip install rich keyboard pyperclip")
    
    return all_passed

if __name__ == "__main__":
    run_full_check()