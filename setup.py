import json
import sys
import pip
import platform
import time
import os

LocalMachineOS = platform.system()
pythonVersion = sys.version_info
if LocalMachineOS == "Darwin" or LocalMachineOS == "Linux":
    os.system("clear")
elif (
    LocalMachineOS == "win32"
    or LocalMachineOS == "win64"
    or LocalMachineOS == "Windows"
):
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

checkpip = input("Do you want to install modules if haven't already? (y/n):")
if checkpip.lower() == "y":
    print("Awaiting pip...")
    time.sleep(2.1)
    pip.main(['install', "discord.py"])
    pip.main(['install', "asyncio"])
    print("Finished running pip, continuing setup..")

alreadyexists = input(
    "Do you have an existing Merch Code System installation or no? (y/n):"
)
if alreadyexists.lower() == "y":
    directory = input("Enter the directory of the old installation: ")
    newDirect = directory.replace("'", "")
    if LocalMachineOS == "Darwin" or LocalMachineOS == "Linux":
        if not newDirect.endswith("/"):
            newDirect = newDirect + "/"
    elif (
        LocalMachineOS == "win32"
        or LocalMachineOS == "win64"
        or LocalMachineOS == "Windows"
    ):
        if not newDirect.endswith("\\"):
            newDirect = newDirect + "\\"
    print("Reviewing Directory...")
    print("New directory:")
    print(newDirect)
    confirm = input("Is this directory correct? (y/n): ")
    if confirm.lower() == "y":
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
            botTokenNew["NotificationChannelId"] = botToken["MainChannelId"]
        if testIfVariableExists(botToken, "NotificationChannelId"):
            botTokenNew["NotificationChannelId"] = botToken["NotificationChannelId"]

        if testIfVariableExists(botToken, "OwnerId"):
            if isinstance(botToken["OwnerId"], int):
                botTokenNew["Admins"] = [botToken["OwnerId"]]
            else:
                botTokenNew["Admins"] = botToken["OwnerId"]

        if testIfVariableExists(botToken, "Admins"):
            if isinstance(botToken["Admins"], int):
                botTokenNew["Admins"] = [botToken["Admins"]]
            else:
                botTokenNew["Admins"] = botToken["Admins"]

        if testIfVariableExists(botToken, "ServerID"):
            botTokenNew["ServerID"] = botToken["ServerID"]
        if testIfVariableExists(botToken, "SlashCommandsOnly"):
            botTokenNew["SlashCommandsOnly"] = botToken["SlashCommandsOnly"]
        if testIfVariableExists(botToken, "BlacklistedUsers"):
            botTokenNew["BlacklistedUsers"] = botToken["BlacklistedUsers"]

        # codes

        for code in codes.keys():
            real_code = codes[code]
            if not testIfVariableExists(real_code, "Role"):
                codes[code]["Role"] = 0
            if not testIfVariableExists(code, "Reward"):
                codes[code]["Reward"] = real_code["reward"]
                codes[code]["reward"] = ""
        codesNew = code

        # users

        userDataNew = userData

        # economy

        if testIfVariableExists(economy, "Enabled"):
            economyNew["Enabled"] = economy["Enabled"]
        if testIfVariableExists(economy, "UserData"):
            economyNew["UserData"] = economy["UserData"]
        if testIfVariableExists(economy, "StoreInventory"):
            economyNew["StoreInventory"] = economy["StoreInventory"]
        if testIfVariableExists(economy, "EconomyName"):
            economyNew["EconomyName"] = economy["EconomyName"]
        if testIfVariableExists(economy, "Commands"):
            economyNew["Commands"] = economy["Commands"]
        if testIfVariableExists(economy, "SuccessRate"):
            economyNew["SuccessRate"] = economy["SuccessRate"]
        if testIfVariableExists(economy, "JobList"):
            economyNew["JobList"] = economy["JobList"]
        if testIfVariableExists(economy, "RoleMultiplier"):
            economyNew["RoleMultiplier"] = economy["RoleMultiplier"]
        if testIfVariableExists(economy, "InventoryLimit"):
            economyNew["InventoryLimit"] = economy["InventoryLimit"]
        if testIfVariableExists(economy, "GreatReset"):
            economyNew["GreatReset"] = economy["GreatReset"]

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
    botInfo1 = input(
        "Your Discord Bot token (Get from your Discord Developer Portal): "
    )
    botInfo2 = int(input("Your Owner ID (your user Id): "))
    botInfo3 = int(
        input(
            "Your Main Channel (the channel id you would like messages to be sent to for messages from bot): "
        )
    )
    botInfo4 = int(input("Your Guild or Discord Server ID: "))
    botInfo5 = input("Slash Commands Only? (y/n)")
    if botInfo5.lower() == "y":
        botInfo5 = True
    else:
        botInfo5 = False
    print("-- CODES SECTION --")
    codeInfo1 = input("Would you like to add an perm code? (Optional) (y/n)")
    codeInfo2 = None
    if codeInfo1.lower() == "y":
        codeInfo2 = input("Code?")
        codeInfo3 = input("Reward?")

    print("-- ECONOMY SECTION --")
    economy1 = input("Do you want to enable economy commands? (y/n):")
    if economy1.lower() == "y":
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

        if input("Do you want to enable Great Reset and Season commands? (y/n): ").lower() == "y":
            economy6 = True
            economy7 = input("Cash King Role ID? (): ")
            if int(economy7):
                economy7 = int(economy7)
            else:
                economy7 = 0

            economy8 = input("Reset Cash when the great reset starts? (y/n): ")
            if economy8.lower() == "y":
                economy8 = True
            else:
                economy8 = False
            economy9 = input("Reset Items when the great reset starts? (y/n): ")
            if economy9.lower() == "y":
                economy9 = True
            else:
                economy9 = False
            economy10 = input("Reset Roles with multipilers when the great reset starts? (y/n): ")
            if economy10.lower() == "y":
                economy10 = True
                economy11 = input("One role to reset when great reset? (): ")
                if int(economy11):
                    economy11 = int(economy11)
                else:
                    economy11 = 0
            else:
                economy10 = False
                economy11 = 0
        else:
            economy6 = False
            economy7 = 0
            economy8 = False
            economy9 = False
            economy10 = False
            economy11 = 0
    else:
        economy1 = False

    print("-- Finished Questions --")
    print("Preparing to generate JSONs")
    botJSON = {
        "Token": botInfo1,
        "Admins": [botInfo2],
        "NotificationChannelId": botInfo3,
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
            "Commands": {
                "Daily": economy4
            },
            "SuccessRate": economy3,
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
            "GreatReset": {
                "Enabled": economy6,
                "RolesToReset": [economy11],
                "SeasonNumber": 1,
                "DataToReset": {
                    "Cash": economy8,
                    "Roles": economy9,
                    "Items": economy10
                },
                "CashKingRoleID": economy7,
                "ItemDataWhenRestock": [
                    {
                        "stock": 1,
                        "price": 10000000,
                        "name": "Cash King",
                        "role": economy7
                    }
                ]
            },
            "RoleMultiplier": [],
            "InventoryLimit": economy5
        }
        with open("economy.json", "w") as outfile:
            outfile.write(json.dumps(economyJSON))
    if codeInfo1.lower() == "y":
        codeJSON = {
            codeInfo2: {
                "Reward": codeInfo3,
                "OneUserOnly": False,
                "Role": 0
            }
        }
        with open("codes.json", "w") as outfile:
            outfile.write(json.dumps(codeJSON))
    print("JSONs Ready")
    enter = input("Press Enter to finish setup: ")
    with open("bot.json", "w") as outfile:
        outfile.write(json.dumps(botJSON))
print("Setup is finished!")
