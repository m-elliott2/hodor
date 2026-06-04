"""
A script to prevent the computer from locking by simulating keyboard activity.

This script, inspired by Hodor from Game of Thrones, "holds the door" by
repeatedly pressing the Shift key. This prevents the system from becoming
idle and locking the screen, which is useful when you need to step away from
your computer but want to avoid re-entering your credentials.

The script can be run with a custom time interval for the key presses.

Usage:
    python Hodor.py [--interval SECONDS]

Example:
    python Hodor.py --interval 60
"""
import argparse
import os
import sys
import threading
import time
from typing import Optional

from PIL import Image
from pynput.keyboard import Controller, Key
from pystray import Icon, Menu, MenuItem as item

def get_resource_path(relative_path: str) -> str:
    """Get absolute path to resource, works for dev and for PyInstaller.
    
    Args:
        relative_path: Path relative to the base directory
        
    Returns:
        Absolute path to the resource
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS  # type: ignore
    except AttributeError:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

class HodorApp:
    """Main application class that prevents system lock via simulated keyboard activity."""
    
    def __init__(self, interval: int) -> None:
        """Initialize the Hodor application.
        
        Args:
            interval: Time in seconds between keyboard activity simulations
        """
        self.interval = interval
        self.running = True
        self.keyboard = Controller()
        self.tray_icon = None
        self.hodor_thread = threading.Thread(target=self.hold_the_door)
        self.hodor_thread.daemon = True

    def hold_the_door(self) -> None:
        """Press the Shift key twice at the specified interval to prevent system lock.
        
        Uses Shift key to simulate activity without triggering Windows 11 toggle key popups
        (which occur with Num Lock, Caps Lock, etc.).
        """
        while self.running:
            # Press Shift twice to simulate activity without triggering Windows popups
            self.keyboard.press(Key.shift)
            self.keyboard.release(Key.shift)
            self.keyboard.press(Key.shift)
            self.keyboard.release(Key.shift)
            time.sleep(self.interval)

    def on_exit(self) -> None:
        """Stop the Hodor loop and exit the application."""
        self.running = False
        if self.tray_icon:
            self.tray_icon.stop()

    def run(self) -> None:
        """Start the Hodor thread and system tray icon."""
        self.hodor_thread.start()
        
        image = Image.open(get_resource_path("asset/hodor.png"))
        menu = Menu(
            item('Hodor', None, enabled=False),
            item(f'Interval: {self.interval}s', None, enabled=False),
            item('Valar Morghulis (Exit)', self.on_exit)
        )
        self.tray_icon = Icon("Hodor", image, "Hodor", menu)
        
        # Run the icon in a detached thread to avoid blocking
        self.tray_icon.run_detached()
        
        # Keep the main thread alive until exit signal
        self.hodor_thread.join()

def main() -> None:
    """Parse command-line arguments and run the Hodor application."""
    parser = argparse.ArgumentParser(
        description="Prevents the computer from locking by simulating keyboard activity."
    )
    parser.add_argument(
        "-i", "--interval",
        type=int,
        default=5,
        help="Time interval in seconds between key presses (default: 5)"
    )
    args = parser.parse_args()

    app = HodorApp(interval=args.interval)
    try:
        app.run()
    except KeyboardInterrupt:
        app.on_exit()

if __name__ == "__main__":
    main()



