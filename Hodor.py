"""
A script to prevent the computer from locking by simulating keyboard activity.
This script, inspired by Hodor from Game of Thrones, "holds the door" by
repeatedly pressing the Num Lock key. This prevents the system from becoming
idle and locking the screen, which is useful when you need to step away from
your computer but want to avoid re-entering your credentials.
The script can be run with a custom time interval for the key presses.
Usage:
    python Hodor.py [--interval SECONDS]
Example:
    python Hodor.py --interval 60
"""
import argparse
import time
import threading
from PIL import Image
from pynput.keyboard import Key, Controller
from pystray import Icon as icon, MenuItem as item, Menu

import argparse
import time
import threading
from PIL import Image
from pynput.keyboard import Key, Controller
from pystray import Icon as icon, MenuItem as item, Menu

class HodorApp:
    def __init__(self, interval: int):
        self.interval = interval
        self.running = True
        self.keyboard = Controller()
        self.tray_icon = None
        self.hodor_thread = threading.Thread(target=self.hold_the_door)
        self.hodor_thread.daemon = True

    def hold_the_door(self):
        """
        Presses the Num Lock key twice at the specified interval to prevent the
        system from locking.
        """
        print("Holding the door...")
        while self.running:
            print("Hodor")
            # Press Num Lock twice to simulate activity without changing its state
            self.keyboard.press(Key.num_lock)
            self.keyboard.release(Key.num_lock)
            self.keyboard.press(Key.num_lock)
            self.keyboard.release(Key.num_lock)
            time.sleep(self.interval)

    def on_exit(self):
        """Stops the Hodor loop and exits the application."""
        print("\nStopping Hodor. The door is no longer held.")
        self.running = False
        if self.tray_icon:
            self.tray_icon.stop()

    def run(self):
        """Starts the Hodor thread and the system tray icon."""
        self.hodor_thread.start()
        
        image = Image.open("asset/hodor.png")
        menu = Menu(
            item('Hodor', None, enabled=False),
            item(f'Interval: {self.interval}s', None, enabled=False),
            item('Valar Morghulis (Exit)', self.on_exit)
        )
        self.tray_icon = icon("Hodor", image, "Hodor", menu)
        self.tray_icon.run()

def main():
    """
    Parses command-line arguments and runs the Hodor application.
    """
    parser = argparse.ArgumentParser(
        description="Prevents the computer from locking by simulating keyboard activity."
    )
    parser.add_argument(
        "-i", "--interval",
        type=int,
        default=5,
        help="The time interval in seconds between key presses. Defaults to 5 seconds."
    )
    args = parser.parse_args()

    app = HodorApp(interval=args.interval)
    try:
        app.run()
    except KeyboardInterrupt:
        app.on_exit()

if __name__ == "__main__":
    main()



