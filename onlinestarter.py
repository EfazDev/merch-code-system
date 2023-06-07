import requests
import platform
import subprocess
import os
import time

def whichPythonCommand():
    LocalMachineOS = platform.system()
    if LocalMachineOS == "Darwin" or LocalMachineOS == "Linux":
        return "python3"
    elif LocalMachineOS == "win32" or LocalMachineOS == "win64" or LocalMachineOS == "Windows":
        return "python"
    else:
        return "python3"
    
if whichPythonCommand() == "python3":
    os.system("clear")
else:
    os.system("cls")
    
print("Welcome to Efaz's Merch Code System Launcher!")
print("")
print("Launcher Made by EfazDev#0220")
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
    f = open("main.py", "w")
    f.write(content)
    print("Finished Writing Script")
    print("Running Script...")
    subprocess.Popen([whichPythonCommand(), 'main.py'])
    print("Finished Running, ending launcher...")
    quit()
else:
    print("Server returned unknown status code. Extension not runned")