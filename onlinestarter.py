import requests
import platform
import subprocess
import sys
import os
import time
    
os.system("cls" if os.name == "nt" else "clear")

def printSystemMessage(message):
    print(f"\x1b[38;2;255;75;0m{message}\033[38;5;231m")

def printMainMessage(mes):
    print(f"\x1b[38;2;255;255;255m{mes}\033[38;5;231m")

def printErrorMessage(mes):
    print(f"\x1b[38;2;255;0;0m{mes}\033[38;5;231m")

def printSuccessMessage(mes):
    print(f"\x1b[38;2;0;255;0m{mes}\033[38;5;231m")

printSystemMessage('''
Welcome to Efaz's Merch Code System Launcher!
Launcher Made by Efaz at efaz.dev

Logs:
''')
printMainMessage("Looking for System Device Details...")
printMainMessage("Detected: " + platform.system())
printMainMessage("Launching latest version...")
url = "https://raw.githubusercontent.com/EfazDev/merch-code-system/main/main.py"
time.sleep(2)
printMainMessage("Locating Request from URL...")
resp = requests.get(url)
if resp.status_code == 200:
    printSuccessMessage("Finished GET Request, saving script...")
    content = resp.text
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    printSuccessMessage("Finished Writing Script")
    printMainMessage("Running Script...")
    subprocess.Popen([sys.executable, 'main.py'])
    printSuccessMessage("Finished Running, ending launcher...")
    quit()
else:
    printErrorMessage("Server returned unknown status code. Merch Code System not ran")