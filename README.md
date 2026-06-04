# Hodor

A simple Python script to prevent your computer from locking by simulating keyboard activity. This script "holds the door" for you by periodically pressing the Shift key, twice in succession so your work goes uninterrupted, even if you're typing. The application runs in the system tray with a custom Hodor icon, allowing you to easily exit when you're done. Uses Shift key to avoid triggering Windows 11 toggle key popups.

![Hodor System Tray](asset/hodor.png)

## Features

*   **Prevents Screen Lock**: Simulates keyboard activity to keep your system awake.
*   **System Tray Icon**: Runs discreetly in the system tray with a custom Hodor icon.
*   **Configurable Interval**: Set the time between key presses via the command line.
*   **Graceful Exit**: Easily exit the application through the system tray menu.
*   **Silent Operation**: Designed to run silently in the background without triggering Windows popups.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/hodor.git
    cd hodor
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Command Line

Run the script from the command line. It will start the application and place the Hodor icon in your system tray.

```bash
python hodor.py
```

You can specify a custom interval (in seconds) for the key presses using the `--interval` or `-i` argument. The default is 5 seconds.

```bash
python hodor.py --interval 60
```

### System Tray

*   **Right-click** the Hodor icon in the system tray to open the menu.
*   Select **Valar Morghulis (Exit)** to close the application.

## Building

A `pyinstaller.bat` script is included to bundle the application into a single executable.

1.  Make sure you have PyInstaller installed:
    ```bash
    pip install pyinstaller
    ```

2.  Run the batch script:
    ```bash
    pyinstaller.bat
    ```

The executable will be created in the `dist` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
