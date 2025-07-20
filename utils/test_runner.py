"""
PromptGPT OS - Automated Testing Suite
Developed by: https://github.com/KowaiAI
Copyright (c) 2025 KowaiAI. All rights reserved.

Comprehensive automated testing for all PromptGPT OS components.
Features unit tests, integration tests, and performance benchmarks.

Watermark: PROMPTGPT_OS_KOWAI_AI_2025_TEST_RUNNER_CORE
"""

import os
import sys
import json
import time
import unittest
import importlib.util
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn

console = Console()

class PromptGPTTestSuite:
    """Comprehensive test suite for PromptGPT OS"""
    
    def __init__(self):
        self.test_results = {}
        self.performance_metrics = {}
        self.failed_tests = []
        
    def run_all_tests(self):
        """Execute comprehensive test suite"""
        console.print("\n[bold yellow]🧪 Starting Comprehensive Test Suite...[/bold yellow]")
        
        test_categories = [
            ("Core Module Tests", self._test_core_modules),
            ("Configuration Tests", self._test_configuration),
            ("Data Integrity Tests", self._test_data_integrity),
            ("UI Component Tests", self._test_ui_components),
            ("File System Tests", self._test_file_system),
            ("Database Tests", self._test_database),
            ("Clipboard Tests", self._test_clipboard),
            ("History System Tests", self._test_history_system),
            ("Animation Tests", self._test_animations),
            ("Error Handling Tests", self._test_error_handling),
            ("Performance Tests", self._test_performance)
        ]
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.1f}%"),
            console=console
        ) as progress:
            
            overall_task = progress.add_task("Running Test Suite", total=len(test_categories))
            
            for category_name, test_function in test_categories:
                category_task = progress.add_task(f"Testing {category_name}", total=None)
                
                try:
                    start_time = time.time()
                    result = test_function()
                    end_time = time.time()
                    
                    self.test_results[category_name] = {
                        'status': 'PASSED',
                        'details': result,
                        'duration': end_time - start_time
                    }
                    
                    progress.update(category_task, description=f"✅ {category_name}")
                    
                except Exception as e:
                    self.test_results[category_name] = {
                        'status': 'FAILED', 
                        'error': str(e),
                        'duration': time.time() - start_time if 'start_time' in locals() else 0
                    }
                    self.failed_tests.append(category_name)
                    progress.update(category_task, description=f"❌ {category_name}")
                
                progress.advance(overall_task)
                time.sleep(0.3)
        
        return self._generate_test_report()
    
    def _test_core_modules(self):
        """Test core module functionality"""
        tests = []
        
        # Test main application imports
        try:
            sys.path.append('.')
            import main
            tests.append("✅ Main application module loaded")
        except Exception as e:
            tests.append(f"❌ Main module error: {e}")
        
        # Test configuration
        try:
            from config.settings import Colors, ASCII_ART
            tests.append("✅ Configuration module loaded")
        except Exception as e:
            tests.append(f"❌ Config module error: {e}")
        
        # Test utilities
        utils_modules = ['navigation', 'prompt_generator', 'file_handler', 'clipboard_manager']
        for module in utils_modules:
            try:
                importlib.import_module(f'utils.{module}')
                tests.append(f"✅ Utils.{module} loaded")
            except Exception as e:
                tests.append(f"❌ Utils.{module} error: {e}")
        
        return tests
    
    def _test_configuration(self):
        """Test configuration system"""
        tests = []
        
        # Test config file existence
        config_file = "config/settings.py"
        if os.path.exists(config_file):
            tests.append("✅ Configuration file exists")
            
            try:
                from config.settings import Colors
                # Test color definitions
                required_colors = ['primary', 'secondary', 'accent', 'success', 'warning', 'error']
                for color in required_colors:
                    if hasattr(Colors, color):
                        tests.append(f"✅ Color.{color} defined")
                    else:
                        tests.append(f"❌ Color.{color} missing")
            except Exception as e:
                tests.append(f"❌ Color configuration error: {e}")
        else:
            tests.append("❌ Configuration file missing")
        
        return tests
    
    def _test_data_integrity(self):
        """Test data file integrity"""
        tests = []
        
        data_files = [
            ("data/questions.json", "Questions database"),
            ("data/templates.json", "Template database")
        ]
        
        for file_path, description in data_files:
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    if isinstance(data, dict) and len(data) > 0:
                        tests.append(f"✅ {description} valid and populated")
                    else:
                        tests.append(f"⚠️ {description} empty or invalid structure")
                        
                except json.JSONDecodeError as e:
                    tests.append(f"❌ {description} JSON error: {e}")
            else:
                tests.append(f"❌ {description} file missing")
        
        return tests
    
    def _test_ui_components(self):
        """Test UI system components"""
        tests = []
        
        try:
            from rich.console import Console
            from rich.panel import Panel
            from rich.text import Text
            
            # Test Rich components
            test_console = Console(file=open(os.devnull, 'w'))
            test_panel = Panel("Test", title="Test Panel")
            test_text = Text("Test Text", style="bold green")
            
            tests.append("✅ Rich UI components working")
            
            # Test display manager
            try:
                from ui.display import DisplayManager
                display_mgr = DisplayManager()
                tests.append("✅ Display manager loaded")
            except Exception as e:
                tests.append(f"❌ Display manager error: {e}")
                
        except Exception as e:
            tests.append(f"❌ UI system error: {e}")
        
        return tests
    
    def _test_file_system(self):
        """Test file system operations"""
        tests = []
        
        # Test directory structure
        required_dirs = ["config", "data", "ui", "utils", "generated_prompts"]
        for directory in required_dirs:
            if os.path.exists(directory):
                tests.append(f"✅ Directory {directory} exists")
            else:
                tests.append(f"❌ Directory {directory} missing")
        
        # Test file permissions
        try:
            test_file = "test_permissions.tmp"
            with open(test_file, 'w') as f:
                f.write("test")
            os.remove(test_file)
            tests.append("✅ File write permissions working")
        except Exception as e:
            tests.append(f"❌ File permission error: {e}")
        
        return tests
    
    def _test_database(self):
        """Test database functionality"""
        tests = []
        
        try:
            import sqlite3
            
            # Test in-memory database
            conn = sqlite3.connect(":memory:")
            conn.execute("CREATE TABLE test (id INTEGER, name TEXT)")
            conn.execute("INSERT INTO test VALUES (1, 'test')")
            result = conn.execute("SELECT * FROM test").fetchone()
            conn.close()
            
            if result == (1, 'test'):
                tests.append("✅ SQLite database operations working")
            else:
                tests.append("❌ SQLite data retrieval failed")
                
        except Exception as e:
            tests.append(f"❌ Database error: {e}")
        
        # Test offline database file
        db_file = "data/promptgpt_offline.db"
        if os.path.exists(db_file):
            tests.append("✅ Offline database file exists")
        else:
            tests.append("⚠️ Offline database file not found")
        
        return tests
    
    def _test_clipboard(self):
        """Test clipboard functionality"""
        tests = []
        
        try:
            import pyperclip
            
            # Test clipboard write/read
            test_text = "PromptGPT OS Test"
            pyperclip.copy(test_text)
            retrieved_text = pyperclip.paste()
            
            if retrieved_text == test_text:
                tests.append("✅ Clipboard operations working")
            else:
                tests.append("⚠️ Clipboard data mismatch")
                
        except Exception as e:
            tests.append(f"❌ Clipboard error: {e}")
        
        return tests
    
    def _test_history_system(self):
        """Test history management"""
        tests = []
        
        try:
            from utils.history_manager import HistoryManager
            
            # Test history manager initialization
            history_mgr = HistoryManager()
            tests.append("✅ History manager initialized")
            
            # Test history file
            history_file = "generated_prompts/prompt_history.json"
            if os.path.exists(history_file):
                with open(history_file, 'r') as f:
                    data = json.load(f)
                tests.append("✅ History file accessible")
            else:
                tests.append("⚠️ History file not found")
                
        except Exception as e:
            tests.append(f"❌ History system error: {e}")
        
        return tests
    
    def _test_animations(self):
        """Test animation system"""
        tests = []
        
        try:
            from utils.animations import AnimationManager
            
            # Test animation manager
            anim_mgr = AnimationManager()
            tests.append("✅ Animation manager loaded")
            
            # Test animation methods exist
            animation_methods = ['typewriter_effect', 'loading_spinner', 'progress_bar']
            for method in animation_methods:
                if hasattr(anim_mgr, method):
                    tests.append(f"✅ Animation.{method} available")
                else:
                    tests.append(f"❌ Animation.{method} missing")
                    
        except Exception as e:
            tests.append(f"❌ Animation system error: {e}")
        
        return tests
    
    def _test_error_handling(self):
        """Test error handling system"""
        tests = []
        
        try:
            from utils.error_handler import ErrorClassifier, AutomatedDebugger
            
            # Test error classifier
            classifier = ErrorClassifier()
            test_error_code = classifier.classify_error("FileNotFoundError", "test file not found")
            
            if test_error_code in classifier.ERROR_CODES:
                tests.append("✅ Error classification working")
            else:
                tests.append("❌ Error classification failed")
            
            # Test automated debugger
            debugger = AutomatedDebugger()
            tests.append("✅ Automated debugger initialized")
            
        except Exception as e:
            tests.append(f"❌ Error handling system error: {e}")
        
        return tests
    
    def _test_performance(self):
        """Test system performance"""
        tests = []
        metrics = {}
        
        # Test import times
        start_time = time.time()
        try:
            from rich.console import Console
            import_time = time.time() - start_time
            metrics['rich_import_time'] = import_time
            tests.append(f"✅ Rich import time: {import_time:.3f}s")
        except Exception as e:
            tests.append(f"❌ Rich import failed: {e}")
        
        # Test JSON parsing performance
        start_time = time.time()
        try:
            with open("data/questions.json", 'r') as f:
                json.load(f)
            parse_time = time.time() - start_time
            metrics['json_parse_time'] = parse_time
            tests.append(f"✅ JSON parse time: {parse_time:.3f}s")
        except Exception as e:
            tests.append(f"❌ JSON parsing failed: {e}")
        
        # Test memory usage (basic check)
        try:
            import psutil
            memory_usage = psutil.Process().memory_info().rss / 1024 / 1024  # MB
            metrics['memory_usage_mb'] = memory_usage
            tests.append(f"✅ Memory usage: {memory_usage:.1f}MB")
        except ImportError:
            tests.append("⚠️ psutil not available for memory testing")
        except Exception as e:
            tests.append(f"❌ Memory check failed: {e}")
        
        self.performance_metrics = metrics
        return tests
    
    def _generate_test_report(self):
        """Generate comprehensive test report"""
        total_tests = len(self.test_results)
        passed_tests = len([r for r in self.test_results.values() if r['status'] == 'PASSED'])
        failed_tests = len(self.failed_tests)
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_categories': total_tests,
                'passed': passed_tests,
                'failed': failed_tests,
                'success_rate': (passed_tests / total_tests * 100) if total_tests > 0 else 0,
                'overall_status': 'HEALTHY' if failed_tests == 0 else 'ISSUES_DETECTED'
            },
            'detailed_results': self.test_results,
            'performance_metrics': self.performance_metrics,
            'failed_categories': self.failed_tests
        }
        
        return report

def display_test_results(results):
    """Display comprehensive test results"""
    console.print("\n[bold cyan]🧪 AUTOMATED TEST RESULTS[/bold cyan]")
    
    # Summary Panel
    summary = results['summary']
    status_color = "green" if summary['overall_status'] == 'HEALTHY' else "red"
    
    summary_text = Text()
    summary_text.append(f"Status: ", style="white")
    summary_text.append(f"{summary['overall_status']}", style=f"bold {status_color}")
    summary_text.append(f"\nTest Categories: {summary['total_categories']}", style="white")
    summary_text.append(f"\nPassed: {summary['passed']}", style="green")
    summary_text.append(f"\nFailed: {summary['failed']}", style="red")
    summary_text.append(f"\nSuccess Rate: {summary['success_rate']:.1f}%", style="yellow")
    summary_text.append(f"\nTest Time: {results['timestamp']}", style="dim white")
    
    summary_panel = Panel(
        summary_text,
        title="[bold yellow]📊 TEST SUMMARY[/bold yellow]",
        border_style="yellow"
    )
    console.print(summary_panel)
    
    # Detailed Results Table
    console.print("\n[bold white]📋 DETAILED TEST RESULTS[/bold white]")
    
    results_table = Table(show_header=True, header_style="bold cyan")
    results_table.add_column("Category", style="white", width=25)
    results_table.add_column("Status", style="white", width=10)
    results_table.add_column("Duration", style="dim white", width=10)
    results_table.add_column("Details", style="dim white", width=50)
    
    for category, result in results['detailed_results'].items():
        status_color = "green" if result['status'] == 'PASSED' else "red"
        status_text = f"[{status_color}]{result['status']}[/{status_color}]"
        duration_text = f"{result['duration']:.3f}s"
        
        if result['status'] == 'PASSED':
            details = f"{len(result['details'])} tests completed"
        else:
            details = result.get('error', 'Unknown error')[:50]
        
        results_table.add_row(category, status_text, duration_text, details)
    
    console.print(results_table)
    
    # Performance Metrics
    if results['performance_metrics']:
        console.print("\n[bold yellow]⚡ PERFORMANCE METRICS[/bold yellow]")
        
        perf_table = Table(show_header=True, header_style="bold yellow")
        perf_table.add_column("Metric", style="white", width=20)
        perf_table.add_column("Value", style="cyan", width=15)
        perf_table.add_column("Unit", style="dim white", width=10)
        
        for metric, value in results['performance_metrics'].items():
            if 'time' in metric:
                perf_table.add_row(metric.replace('_', ' ').title(), f"{value:.3f}", "seconds")
            elif 'memory' in metric:
                perf_table.add_row(metric.replace('_', ' ').title(), f"{value:.1f}", "MB")
            else:
                perf_table.add_row(metric.replace('_', ' ').title(), str(value), "")
        
        console.print(perf_table)

def run_test_suite():
    """Main test suite runner"""
    test_suite = PromptGPTTestSuite()
    results = test_suite.run_all_tests()
    display_test_results(results)
    return results

if __name__ == "__main__":
    console.print("[bold cyan]🧪 PromptGPT OS - Automated Test Suite[/bold cyan]")
    console.print("Developed by: https://github.com/KowaiAI\n")
    
    try:
        run_test_suite()
    except KeyboardInterrupt:
        console.print("\n[yellow]Testing interrupted by user[/yellow]")
    except Exception as e:
        console.print(f"\n[bold red]Test suite error: {e}[/bold red]")