#!/usr/bin/env python3
"""
Startup script for Airline Data Analytics Dashboard
This script provides a convenient way to run the application
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = [
        'flask',
        'pandas',
        'requests',
        'plotly',
        'beautifulsoup4',
        'python-dotenv'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        
        response = input("\n📦 Install missing packages? (y/n): ")
        if response.lower() in ['y', 'yes']:
            print("\n🔧 Installing packages...")
            subprocess.run([sys.executable, '-m', 'pip', 'install'] + missing_packages)
        else:
            print("❌ Cannot run application without required packages")
            sys.exit(1)

def create_env_file():
    """Create .env file if it doesn't exist"""
    env_file = Path('.env')
    if not env_file.exists():
        print("📝 Creating .env file...")
        with open(env_file, 'w') as f:
            f.write("# Airline Data Analytics Dashboard Configuration\n")
            f.write("# Get your free API key at: https://aviationstack.com/\n")
            f.write("AVIATIONSTACK_API_KEY=demo_key\n")
            f.write("OPENAI_API_KEY=\n")
            f.write("FLASK_ENV=development\n")
            f.write("SECRET_KEY=your-secret-key-here\n")
        print("✅ .env file created with default values")

def run_application():
    """Run the Flask application"""
    print("🚀 Starting Airline Data Analytics Dashboard...")
    print("📊 Dashboard will be available at: http://localhost:5000")
    print("🔄 The application uses mock data by default")
    print("🔑 Add your Aviationstack API key to .env file for real data")
    print("⏹️  Press Ctrl+C to stop the application")
    
    try:
        # Import and run the Flask app
        from app import app
        
        # Wait a moment then open browser
        import threading
        def open_browser():
            time.sleep(2)
            webbrowser.open('http://localhost:5000')
        
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        # Run the app
        app.run(debug=True, host='0.0.0.0', port=5000)
        
    except KeyboardInterrupt:
        print("\n🛑 Application stopped")
    except Exception as e:
        print(f"\n❌ Error running application: {str(e)}")
        sys.exit(1)

def main():
    """Main function"""
    print("=" * 50)
    print("🛩️  AIRLINE DATA ANALYTICS DASHBOARD")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path('app.py').exists():
        print("❌ app.py not found. Please run this script from the project directory.")
        sys.exit(1)
    
    # Check dependencies
    print("🔍 Checking dependencies...")
    check_dependencies()
    
    # Create .env file if needed
    create_env_file()
    
    # Run the application
    run_application()

if __name__ == "__main__":
    main() 