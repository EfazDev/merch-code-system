import json
import sys
import platform
import time
import os

LocalMachineOS = platform.system()
pythonVersion = sys.version_info
if LocalMachineOS == "Darwin" or LocalMachineOS == "Linux":
    os.system("clear")
elif LocalMachineOS == "win32" or LocalMachineOS == "win64" or LocalMachineOS == "Windows":
    os.system("cls")

def testIfVariableExists(tablee, variablee):
    if variablee in tablee:
        return True
    else:
        return False

print()
print("\033[38;5;208m███████╗███████╗░█████╗░███████╗██╗░██████╗  ███╗░░░███╗███████╗██████╗░░█████╗░██╗░░██╗\033[0;0m")
print("\033[38;5;208m██╔════╝██╔════╝██╔══██╗╚════██║╚█║██╔════╝  ████╗░████║██╔════╝██╔══██╗██╔══██╗██║░░██║\033[0;0m")
print("\033[38;5;208m█████╗░░█████╗░░███████║░░███╔═╝░╚╝╚█████╗░  ██╔████╔██║█████╗░░██████╔╝██║░░╚═╝███████║\033[0;0m")
print("\033[38;5;208m██╔══╝░░██╔══╝░░██╔══██║██╔══╝░░░░░░╚═══██╗  ██║╚██╔╝██║██╔══╝░░██╔══██╗██║░░██╗██╔══██║\033[0;0m")
print("\033[38;5;208m███████╗██║░░░░░██║░░██║███████╗░░░██████╔╝  ██║░╚═╝░██║███████╗██║░░██║╚█████╔╝██║░░██║\033[0;0m")
print("\033[38;5;208m╚══════╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝░░░╚═════╝░  ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝\033[0;0m")
print("")
print("\033[38;5;208m░█████╗░░█████╗░██████╗░███████╗  ░██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗\033[0;0m")
print("\033[38;5;208m██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔════╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║\033[0;0m")
print("\033[38;5;208m██║░░╚═╝██║░░██║██║░░██║█████╗░░  ╚█████╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║\033[0;0m")
print("\033[38;5;208m██║░░██╗██║░░██║██║░░██║██╔══╝░░  ░╚═══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║\033[0;0m")
print("\033[38;5;208m╚█████╔╝╚█████╔╝██████╔╝███████╗  ██████╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║\033[0;0m")
print("\033[38;5;208m░╚════╝░░╚════╝░╚═════╝░╚══════╝  ╚═════╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝\033[0;0m")
print("")
print("\033[38;5;208mWelcome to Efaz's Discord Merch Code System Setup\033[0;0m")
print("\033[38;5;208mTo set up your JSONs, please continue from here.\033[0;0m")

checkpip = input("Do you want to install modules if haven't already? (true/false):")
if checkpip == "true":
    print("Awaiting pip...")
    time.sleep(2.1)
    if LocalMachineOS == "Darwin" or LocalMachineOS == "Linux":
        os.system("pip3 install discord.py asyncio")
    elif LocalMachineOS == "win32" or LocalMachineOS == "win64" or LocalMachineOS == "Windows":
        os.system("pip install discord.py asyncio")
    print("Finished running pip, continuing setup..")

alreadyexists = input("Do you have an existing Merch Code System installation or no? (true/false):")
if alreadyexists == "true":
    directory = input("Enter the directory of the old installation: ")
    newDirect = directory.replace("'", "")
    if LocalMachineOS == "Darwin" or LocalMachineOS == "Linux":
        if not newDirect.endswith('/'):
            newDirect = newDirect + "/"
    elif LocalMachineOS == "win32" or LocalMachineOS == "win64" or LocalMachineOS == "Windows":
       if not newDirect.endswith('\\'):
            newDirect = newDirect + "\\"
    print("Reviewing Directory...")
    print("New directory:")
    print(newDirect)
    confirm = input("Is this directory correct?")
    if confirm == "true":
         with open(newDirect + "codes.json") as f:
              codes = json.load(f)
         with open(newDirect + "users.json") as f:
              userData = json.load(f)
         with open(newDirect + "bot.json") as f:
              botToken = json.load(f)
         with open(newDirect + "economy.json") as f:
              economy = json.load(f)
         with open("codes.json") as f:
              codesNew = json.load(f)
         with open("users.json") as f:
              userDataNew = json.load(f)
         with open("bot.json") as f:
              botTokenNew = json.load(f)
         with open("economy.json") as f:
              economyNew = json.load(f)
        
        # exchange conversion center

        # bot
         if testIfVariableExists(botToken, "Token"):
            botTokenNew["Token"] = botToken["Token"]
         if testIfVariableExists(botToken, "MainChannelId"):
            botTokenNew["MainChannelId"] = botToken["MainChannelId"]
         if testIfVariableExists(botToken, "OwnerId"):
            botTokenNew["OwnerId"] = botToken["OwnerId"]
         if testIfVariableExists(botToken, "ServerID"):
            botTokenNew["ServerID"] = botToken["ServerID"]
         if testIfVariableExists(botToken, "SlashCommandsOnly"):
            botTokenNew["SlashCommandsOnly"] = botToken["SlashCommandsOnly"]   
         if testIfVariableExists(botToken, "BlacklistedUsers"):
            botTokenNew["BlacklistedUsers"] = botToken["BlacklistedUsers"]   

        # codes

         codesNew = codes
    
        # users

         userDataNew = userData

        # economy

         economyNew = economy

        # end of conversion

         with open("bot.json", "w") as outfile:
              outfile.write(json.dumps(botTokenNew))
         with open("users.json", "w") as outfile:
              outfile.write(json.dumps(userDataNew))
         with open("codes.json", "w") as outfile:
              outfile.write(json.dumps(codesNew))
         with open("economy.json", "w") as outfile:
              outfile.write(json.dumps(economy))
         enter = input("Press Enter to finish setup: ")
    else:
         print("Ending process..")
         exit()
else:
    print("-- BOT SECTION --")
    botInfo1 = input("Your Discord Bot token (Get from your Discord Developer Portal): ")
    botInfo2 = int(input("Your Owner ID (your user Id): "))
    botInfo3 = int(input("Your Main Channel (the channel id you would like messages to be sent to for messages from bot): "))
    botInfo4 = int(input("Your Guild or Discord Server ID: "))
    botInfo5 = input("Slash Commands Only? (true/false)")
    if botInfo5 == "true":
        botInfo5 = True
    else:
        botInfo5 = False
    print("-- CODES SECTION --")
    codeInfo1 = input("Would you like to add an perm code? (Optional) (true or false)")
    codeInfo2 = None
    if codeInfo1 == "true":
        codeInfo2 = input("Code?")
        codeInfo3 = input("Reward?")

    print("-- ECONOMY SECTION --")
    economy1 = input("Do you want to enable economy commands? (true/false):")
    if economy1 == "true":
        economy1 = True
        economy2 = input("Economy Name?")
        economy3 = input("Success Rate? (1 / <what number your put here>): ")
        if int(economy3):
            economy3 = int(economy3)
        else:
            economy3 = 4
        economy4 = input("Daily Amount?")
        if int(economy4):
            economy4 = int(economy4)
        else:
            economy4 = 100
        economy5 = input("Inventory Limit?")
        if int(economy5):
            economy5 = int(economy5)
        else:
            economy5 = 20
    else:
        economy1 = False

    print("-- Finished Questions --")
    print("Preparing to generate JSONs")
    botJSON = {
        "Token": botInfo1,
        "OwnerId": botInfo2,
        "MainChannelId": botInfo3,
        "ServerID": botInfo4,
        "SlashCommandsOnly": botInfo5,
        "BlacklistedUsers": {}
    }
    if economy1 == True:
        economyJSON = {
            "Enabled": True,
            "UserData": {},
            "StoreInventory": {},
            "EconomyName": economy2,
            "SuccessRate": economy3,
            "Commands": {
                "Daily": economy4
            },
            "JobList": [
        {
            "name": "Mayor",
            "amount": 5000
        },
        {
            "name": "District Worker",
            "amount": 1000
        },
        {
            "name": "Principal",
            "amount": 500
        },
        {
            "name": "Teacher",
            "amount": 100
        }
    ],
            "InventoryLimit": economy5
        }
        with open("economy.json", "w") as outfile:
            outfile.write(json.dumps(economyJSON))
    if codeInfo1 == "true":
        codeJSON = {
            codeInfo2: {
                "reward": codeInfo3,
                "OneUserOnly": False,
            }
        }
        with open("codes.json", "w") as outfile:
            outfile.write(json.dumps(codeJSON))
    print("JSONs Ready")
    enter = input("Press Enter to finish setup: ")
    with open("bot.json", "w") as outfile:
        outfile.write(json.dumps(botJSON))
print("Setup is finished!")