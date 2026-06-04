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
from pynput.keyboard import Key, Controller

def hold_the_door(interval: int):
    """
    Presses the Num Lock key twice at a specified interval to prevent the
    system from locking.
    Args:
        interval (int): The time in seconds between key presses.
    """
    keyboard = Controller()
    print("Holding the door...")
    while True:
        print("Hodor")
        # Press Num Lock twice to simulate activity without changing its state
        keyboard.press(Key.num_lock)
        keyboard.release(Key.num_lock)
        keyboard.press(Key.num_lock)
        keyboard.release(Key.num_lock)
        time.sleep(interval)

if __name__ == "__main__":
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

    try:
        hold_the_door(args.interval)
    except KeyboardInterrupt:
        print("\nStopping Hodor. The door is no longer held.")



