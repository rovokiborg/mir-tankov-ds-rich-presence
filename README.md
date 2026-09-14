# World of Tanks — Discord Rich Presence

A small Python script that automatically enables Discord Rich Presence when **World of Tanks** is running.

The script monitors the game process and:

* automatically connects to Discord when the game starts;
* displays a custom Discord Rich Presence status;
* shows the current game session duration;
* randomly changes the activity description;
* automatically clears the status when the game is closed;
* runs silently in the background using `pythonw.exe`.

## Requirements

* Windows 10/11
* Python 3.10+
* Discord Desktop
* World of Tanks
* A Discord Application with a configured Rich Presence image asset

Python dependencies:

```text
psutil
pypresence
```

## Project Structure

Example:

```text
tanki-rpc/
│
├── tanki.bat
├── tanki.pyw
├── requirements.txt
│
└── mir_tankov/
    ├── Scripts/
    │   ├── python.exe
    │   ├── pythonw.exe
    │   └── pip.exe
    └── ...
```

`mir_tankov` is the Python virtual environment.

## Installation

### 1. Create a virtual environment

Open Command Prompt inside the project folder:

```bat
python -m venv mir_tankov
```

### 2. Install dependencies

```bat
mir_tankov\Scripts\pip.exe install -r requirements.txt
```

Or:

```bat
mir_tankov\Scripts\python.exe -m pip install -r requirements.txt
```

## Discord Application Setup

The script currently uses:

```python
CLIENT_ID = "1458048320575508665"
```

This is the Discord Application ID.

To use your own Discord application:

1. Open the Discord Developer Portal.
2. Create a new Application.
3. Copy the `Application ID`.
4. Replace the value in the script:

```python
CLIENT_ID = "YOUR_APPLICATION_ID"
```

5. Add a Rich Presence image asset with the key:

```text
tank
```

The asset key must match:

```python
IMAGE_KEY = "tank"
```

## Monitored Processes

The script considers the game running if it detects one of the following processes:

```python
POSSIBLE_PROCESSES = [
    "tanki.exe",
    "worldoftanks.exe",
    "wot.exe"
]
```

If your game executable has a different filename, add it to this list.

## Running the Script

The project uses:

```text
tanki.bat
```

Recommended contents:

```bat
@echo off
cd /d "%~dp0"

if exist "mir_tankov\Scripts\pythonw.exe" (
    set PYTHON_EXE="mir_tankov\Scripts\pythonw.exe"
) else (
    echo ERROR: pythonw.exe was not found in mir_tankov\Scripts
    pause
    exit /b 1
)

start "" %PYTHON_EXE% "tanki.pyw"
```

The script runs without a console window because it uses `pythonw.exe`.

After launch, it stays in the background and waits for the game process to appear.

## How It Works

Every 15 seconds, the script checks the list of running Windows processes:

```python
time.sleep(15)
```

When World of Tanks is detected:

1. the script connects to Discord RPC;
2. the session start time is saved;
3. Discord Rich Presence is updated.

Example activity:

```text
World of Tanks

Rolling into battle
On the battlefield

00:42:17 elapsed
```

The activity description is selected randomly from:

```python
DESCRIPTIONS = [
    "Пьет пиво",
    "Ебет на бабахе",
    "Качает ветку",
    "Отращивает пузо",
    "Ебет тухлозадых",
    "Раздает в зюзю",
    "Артаводы кто?"
]
```

You can replace these strings with any custom messages you want.

When the game is closed, the Rich Presence activity is automatically cleared.

## Discord Must Be Running

`pypresence` connects to the local Discord Desktop client.

If Discord is not running, the connection will fail.

The script will automatically try again during the next process check.

## Run Automatically on Windows Startup

To start the script automatically when Windows starts:

1. Press `Win + R`.
2. Enter:

```text
shell:startup
```

3. Create a shortcut to:

```text
tanki.bat
```

The script will then start automatically after you sign in to Windows.

## Stopping the Script

Because the script uses `pythonw.exe`, there is no visible console window.

To stop it manually, open Task Manager and terminate the corresponding `pythonw.exe` process.

If you have other Python applications running through `pythonw.exe`, make sure you terminate the correct process.

## Configuration

### Change the State

```python
state="На поле боя"
```

For example:

```python
state="On the battlefield"
```

### Change Activity Descriptions

Edit:

```python
DESCRIPTIONS = [...]
```

### Change the Rich Presence Image

Edit:

```python
IMAGE_KEY = "tank"
```

An image asset with the same key must exist in your Discord Application.

### Change the Process Check Interval

Current interval:

```python
time.sleep(15)
```

For example, to check every 5 seconds:

```python
time.sleep(5)
```

## Dependencies

The project uses:

* `psutil` — detects whether the game process is running;
* `pypresence` — communicates with Discord Rich Presence.

## License

This project is intended for personal use.
