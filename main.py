#!/usr/bin/env python3
# ============================================================
# main.py — Entry point for EduBot AI Chatbot
#
# Run this file to start the application:
#   python main.py
#
# Make sure you've installed dependencies first:
#   pip install -r requirements.txt
# ============================================================

import sys
import os

# Ensure project root is in Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def check_dependencies():
    """
    Check that critical libraries are available before launching.
    Provides helpful error messages for missing packages.
    """
    missing = []

    try:
        import tkinter
    except ImportError:
        missing.append("tkinter (usually built-in with Python; try: sudo apt install python3-tk)")

    try:
        import nltk
    except ImportError:
        missing.append("nltk  →  pip install nltk")

    if missing:
        print("=" * 55)
        print("  ⚠️  Missing Required Libraries")
        print("=" * 55)
        for pkg in missing:
            print(f"  • {pkg}")
        print("\n  Run:  pip install -r requirements.txt")
        print("=" * 55)
        sys.exit(1)


def main():
    """
    Application entry point.
    1. Check dependencies
    2. Launch the GUI
    """
    print("=" * 55)
    print("   🤖  EduBot — AI Chatbot")
    print("   Built with Python | NLTK | Tkinter | SQLite")
    print("=" * 55)

    check_dependencies()

    print("[INFO] Initializing NLP engine...")
    print("[INFO] Setting up database...")
    print("[INFO] Launching GUI...\n")

    from gui.chat_window import run_app
    run_app()


if __name__ == "__main__":
    main()
