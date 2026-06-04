# Hodor
A simple Python script to prevent your computer from locking by simulating keyboard activity. Inspired by the loyal character from Game of Thrones, this script "holds the door" for you by periodically pressing the Num Lock key.

## Description
This script is designed to run in the background and prevent your system from becoming idle and locking the screen. This is particularly useful when you are running long tasks, monitoring processes, or just need to step away from your desk without wanting to log back in.

## Usage
You can run the script from the command line. By default, it will press the Num Lock key every 5 seconds. You can specify a custom interval using the `--interval` or `-i` argument.

### Examples
Run with the default 5-second interval:
```bash
python Hodor.py
```
Run with a 60-second interval:
```bash
python Hodor.py --interval 60
```
or
```bash
python Hodor.py -i 60
```
To stop the script, press `Ctrl+C`.

## Installation
The script requires the `pynput` library. You can install it using pip:
```bash
pip install -r requirements.txt
```
