"""
Library Management System (Python Desktop Edition)
Main application launcher.

Technologies used:
- pandas: Data manipulation & CSV flat-file persistence
- numpy: Numerical analysis and statistical metrics
- matplotlib: Visual data charts showing student interest across book categories
- tkinter: Modern graphical user interface (GUI)
- turtle: Vector graphics animated splash screen & logo
"""

import sys
from src.splash.turtle_splash import show_turtle_splash
from src.gui.main_window import MainWindow

def main():
    skip_splash = "--no-splash" in sys.argv

    # 1. Show animated Turtle Splash Screen
    if not skip_splash:
        try:
            print("Displaying Turtle Splash Screen...")
            show_turtle_splash(auto_close=True, duration_seconds=2.0)
        except Exception as e:
            print(f"Splash screen skipped: {e}")

    # 2. Launch Tkinter Desktop Application
    print("Launching Library Management System Dashboard...")
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()

