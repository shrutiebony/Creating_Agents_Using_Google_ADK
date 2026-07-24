"""
Quick launcher for the Data Science Agent UI
Run this file to start the Streamlit web interface
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required dependencies are installed"""
    required = ['streamlit', 'google-adk', 'litellm']
    missing = []
    
    for package in required:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing.append(package)
    
    if missing:
        print("❌ Missing dependencies:")
        for pkg in missing:
            print(f"   - {pkg}")
        print("\nInstall them with:")
        print("   pip install -r requirements.txt")
        return False
    
    return True


def main():
    """Launch the Streamlit UI"""
    print("="*60)
    print("🤖 Data Science Agent UI Launcher")
    print("="*60)
    print("\nChecking dependencies...")
    
    if not check_dependencies():
        sys.exit(1)
    
    print("✅ Dependencies OK\n")
    print("Starting Streamlit...")
    print("="*60)
    print("\n📱 UI will open in your browser automatically")
    print("💡 Use Ctrl+C to stop the server\n")
    
    # Get the directory of this file
    app_dir = os.path.dirname(os.path.abspath(__file__))
    app_file = os.path.join(app_dir, 'app.py')
    
    # Run streamlit
    subprocess.run([
        sys.executable, 
        '-m', 'streamlit', 'run', 
        app_file,
        '--server.port=8501',
        '--server.headless=false',
        '--browser.gatherUsageStats=false'
    ])


if __name__ == "__main__":
    main()

