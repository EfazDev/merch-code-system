import requests
import platform
import subprocess
import sys
import os
import time
    
os.system("cls" if os.name == "nt" else "clear")
    
print("Welcome to Efaz's Merch Code System Launcher!")
print("")
print("Launcher Made by Efaz at efaz.dev")
print("")
print("Looking for System Device Details...")
print("Detected: " + platform.system())
print("Launching latest version...")
url = "https://raw.githubusercontent.com/EfazDev/merch-code-system/main/main.py"
time.sleep(2)
print("Locating Request from URL...")
resp = requests.get(url)
if resp.status_code == 200:
    print("Finished GET Request, saving script...")
    content = resp.text
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Finished Writing Script")
    print("Running Script...")
    subprocess.Popen([sys.executable, 'main.py'])
    print("Finished Running, ending launcher...")
    quit()
else:
    print("Server returned unknown status code. Extension not runned")