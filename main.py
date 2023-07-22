import pip
try:
    import os # python built-in
    import time # python built-in
    import discord # required
    import platform # python built-in
    from discord.ext.commands import Bot # required
    from discord.ext import commands # required
    from discord.ext import tasks, commands
    from discord import app_commands # required
    import string # python built-in
    import random # python built-in
    import json # python built-in
    import asyncio
    import sys # python built-in
    from operator import getitem
    from datetime import datetime
except Exception as e:
    print("Error while launching modules. This may be an module not found error. Do you want to install all the modules required? (y/n): ")
    if input(">> ").lower() == "y":
        pip.main(['install', "discord.py"])
        pip.main(['install', "asyncio"])
        print("Successfully installed modules. Restarting..")
        os.system(sys.executable + " main.py")
        exit()
    else:
        print("System Module Check session ended.")

# required command

# - Windows
# pip install discord.py asyncio

# - Unix
# pip3 install discord.py asyncio

# system info

LocalMachineOS = platform.system()
pythonVersion = sys.version_info
version = "1.5.1"
for _ in range(50):
    print()

def printSystemMessage(message):
    print(f"\033[38;5;208m{message}\033[0;0m")

# load saved data
print()
printSystemMessage("███████╗███████╗░█████╗░███████╗██╗░██████╗  ███╗░░░███╗███████╗██████╗░░█████╗░██╗░░██╗")
printSystemMessage("██╔════╝██╔════╝██╔══██╗╚════██║╚█║██╔════╝  ████╗░████║██╔════╝██╔══██╗██╔══██╗██║░░██║")
printSystemMessage("█████╗░░█████╗░░███████║░░███╔═╝░╚╝╚█████╗░  ██╔████╔██║█████╗░░██████╔╝██║░░╚═╝███████║")
printSystemMessage("██╔══╝░░██╔══╝░░██╔══██║██╔══╝░░░░░░╚═══██╗  ██║╚██╔╝██║██╔══╝░░██╔══██╗██║░░██╗██╔══██║")
printSystemMessage("███████╗██║░░░░░██║░░██║███████╗░░░██████╔╝  ██║░╚═╝░██║███████╗██║░░██║╚█████╔╝██║░░██║")
printSystemMessage("╚══════╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝░░░╚═════╝░  ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝")
print("")
printSystemMessage("░█████╗░░█████╗░██████╗░███████╗  ░██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗")
printSystemMessage("██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔════╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║")
printSystemMessage("██║░░╚═╝██║░░██║██║░░██║█████╗░░  ╚█████╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║")
printSystemMessage("██║░░██╗██║░░██║██║░░██║██╔══╝░░  ░╚═══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║")
printSystemMessage("╚█████╔╝╚█████╔╝██████╔╝███████╗  ██████╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║")
printSystemMessage("░╚════╝░░╚════╝░╚═════╝░╚══════╝  ╚═════╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝")
print("")
printSystemMessage("Welcome to Efaz's Merch Code System Bot!")
printSystemMessage("Please use setup.py if you want to setup your bot!")
printSystemMessage("Let's get started!")
printSystemMessage("System Messages:")
print()
print("Loaded Script Version: v" + version)
print("Loading System Data (codes, users, bot, economy)")

with open("codes.json") as f:
    codes = json.load(f)
with open("users.json") as f:
    userData = json.load(f)
with open("bot.json") as f:
    botToken = json.load(f)
with open("economy.json") as f:
    economy = json.load(f)

StoreItems = economy["StoreInventory"]

print("Loaded Saved Data in JSONs")
print("Loading Functions and Commands")

def loadLists():
    with open("codes.json") as f:
        global codes
        codes = json.load(f)
    with open("users.json") as f:
        global userData
        userData = json.load(f)
    with open("bot.json") as f:
        global botToken
        botToken = json.load(f)
    with open("economy.json") as f:
        global economy
        economy = json.load(f)
        global StoreItems
        StoreItems = economy["StoreInventory"]

def testIfVariableExists(tablee, variablee):
    if tablee is dict:
        list = tablee.keys()
        for i in list:
            if i == variablee:
                return True
        return False
    else:
        if variablee in tablee:
            return True
        else:
            return False
        
def testIfInt(a):
    try:
        int(a)
        return True
    except Exception as e:
        return False

if __name__ == "__main__":
    if not botToken["SlashCommandsOnly"]:
        async def sendEmbed(ctx, message, colorType):
            decimal = None
            if colorType == 1:
                decimal = 65280
            elif colorType == 2:
                decimal = 16538115
            else:
                decimal = 16711680
            embed = discord.Embed(
                color=decimal, title="Merch Code System", description=message
            )
            embed.set_footer(
                text="Made by Efaz from efaz.dev - v" + version,
                icon_url="https://cdn.discordapp.com/attachments/1099414684286861332/1112068066319270019/1W.png",
            )
            print("User " + ctx.message.author.name + " used command: " + ctx.message.content)
            await ctx.reply(embed=embed)

        # normal
        intents = discord.Intents.all()
        intents.message_content = True

        bot = Bot(intents=intents, command_prefix="$!")

        @bot.event
        async def on_ready():
            print(f"Logged on the bot: " + bot.user.name)
            print("System is ready!")
            decimal = 16538115
            embed = discord.Embed(
                color=decimal,
                title="Merch Code System",
                description="Thanks for using Efaz's Merch Code System! Please put a star in our GitHub to support for newer updates!",
            )
            embed.set_footer(
                text="Made by Efaz from efaz.dev - v" + version,
                icon_url="https://cdn.discordapp.com/attachments/1099414684286861332/1112068066319270019/1W.png",
            )
            channel = bot.get_channel(botToken["NotificationChannelId"])
            await channel.send(embed=embed)
            status_task.start()

        @tasks.loop()
        async def status_task():
            while True:
                randomized = random.randint(1, 4)
                if randomized == 1:
                    await bot.change_presence(
                        activity=discord.Game(name=" Efaz's Merch Code System")
                    )
                elif randomized == 2:
                    await bot.change_presence(
                        activity=discord.Activity(type=discord.ActivityType.listening, name=" users redeeming codes")
                    )
                elif randomized == 3:
                    await bot.change_presence(
                        activity=discord.Streaming(name=" live redeeming codes", url="https://www.youtube.com/watch?v=Yr7txrMWRSs")
                    )
                else:
                    await bot.change_presence(
                        activity=discord.Activity(type=discord.ActivityType.watching, name=" giving rewards from codes")
                    )
                await asyncio.sleep(10)

        def predicate(ctx):
            if ctx.message.author.id in botToken["Admins"]:
                return True
            else:
                return False
            
        def blacklisted(ctx):
            if testIfVariableExists(botToken["BlacklistedUsers"], str(ctx.message.author.id)):
                return True
            else:
                return False


        @bot.command()
        async def refreshLists(ctx):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                await sendEmbed(ctx, "Access Denied", 3)
            else:
                print("Loading System Data (codes, users, bot)")
                loadLists()
                print("Loaded Saved Data in JSONs")
                await sendEmbed(ctx, "Refreshed List, restarting main.py script.", 2)

        @bot.command()
        async def restartBot(ctx):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                await sendEmbed(ctx, "Access Denied", 3)
            else:
                await sendEmbed(ctx, "Restarting bot..", 2)
                os.system(sys.executable + " main.py")
                exit()

        @bot.command()
        async def info(ctx):
            if blacklisted(ctx) == True:
                await sendEmbed(ctx, "Access Denied", 3)
                return
            
            main = "** MAIN ** \n `$!info` - This message \n`$!redeem <code>` - Redeem a code. \n`$!createCode <code> <reward> <tempornot>` - Create code in the system \n`$!refreshLists` - Refresh lists and restart main.py \n`$!deleteCode` - Delete code from system \n`$!viewCodes` - View all codes in system \n`$!createRandomized <prefix> <reward> <tempornot>` - Create a random generated code. \n`$!createMultipleRandomized <prefix> <reward> <tempornot> <count>` - Create multiple random generated codes. \n`$!searchUser <userPing>` - Get codes redeemed by user. \n`$!restartBot` - Restart bot. \n`$!blacklist <user> <reason>` - Blacklist an user from using the bot. \n`$!unblacklist <user>` - Unblacklist an user from the system. \n`$!blacklistyourself <reason>` - Blacklist yourself from using the bot. (WARNING: You can only get unblacklisted if you ask the owner of the server.) (THERE IS NO CONFIRMATION MESSAGE) \n`$!shutdown` - Shutdown bot \n"
            fun = "** FUN ** \n `$!flipCoin <amount> <guess>` - Flip a coin. \n`$!gamble <estimate> <max>` - Gamble for a chance of currency! \n`$!createcurrency <user> <amount>` - Create currency \n`$!removecurrency <user> <amount>` - Take currency \n`$!balance <user>` - Check your balance! \n`$!daily` - Get daily balance! \n`$!buy <itemname>` - Buy item from the store! \n`$!inventory` - View inventory you bought from the store! \n`$!greatReset` - If you have the Cash King role set on this bot, you can reset everyone's cash and items! (WORKS IF THE OWNER ENABLED IT) \n`$!use <itemname>` - Use item from your inventory \n`$!createItem <itemname> <stock> <price>` - Create an item in the store. \n`$!viewstorestock` - View what's available in the store. \n`$!sendMoney <user> <amount>` - Send an user money!. \n`$!rob <user>` - Rob an user for chance of money!. \n`$!cooldownCheck` - Check your cooldown!. \n`$!work` - Work for money!. \n`$!top10lb` - Get Top 10 leaderboard!. \n`$!multiplierCheck` - See your multiplier on the economy!. \n`$!endItemListing <itemname>` - End listing in the store!. \n More coming soon"
            if economy["Enabled"] == True:
                await sendEmbed(
                    ctx,
                    main + fun,
                    2,
                )
            else:
                await sendEmbed(
                    ctx,
                    main,
                    2,
                )
    
        @bot.command()
        async def redeem(ctx, arg):
            if blacklisted(ctx) == True:
                await sendEmbed(ctx, "Access Denied", 3)
                return
            if arg:
                if testIfVariableExists(userData, str(ctx.message.author.id)):
                    usersSavedData = userData[str(ctx.message.author.id)]
                    print("User requested to look for code: " + arg)
                    if testIfVariableExists(codes, arg):
                        codeInfo = codes[arg]
                        if testIfVariableExists(usersSavedData, arg):
                            await sendEmbed(ctx, "User has already used this code.", 3)
                        else:
                            if codeInfo["OneUserOnly"] == True:
                                if codes[arg]["Redeemed"] == False:
                                    userData[str(ctx.message.author.id)].append(arg)
                                    codes[arg]["Redeemed"] = True
                                    with open("codes.json", "w") as outfile:
                                        outfile.write(json.dumps(codes))
                                    with open("users.json", "w") as outfile:
                                        outfile.write(json.dumps(userData))

                                    extraString = ""

                                    if not codes[arg]["Role"] == 0:
                                        try:
                                            guild = bot.get_guild(guildId)
                                            role_data = guild.get_role(codes[arg]["Role"])
                                            await ctx.message.author.add_roles(role_data)
                                            extraString = " | Role Added: " + role_data.name
                                        except Exception as e:
                                            extraString = " | Role Added: (failed due to invalid permissions or error.)"

                                    await sendEmbed(
                                        ctx,
                                        "You have redeemed merch code: "
                                        + arg
                                        + " for reward: "
                                        + codeInfo["Reward"] + extraString,
                                        1,
                                    )
                                    print(
                                        ctx.message.author.name + " has redeemed a code: " + arg
                                    )

                                    decimal = 65280
                                    embed = discord.Embed(
                                        color=decimal,
                                        title="Merch Code System",
                                        description="User " + "<@" + str(ctx.message.author.id) + ">" + " has redeemed a merch code: " + arg + " for reward: " + codeInfo["Reward"],
                                    )
                                    embed.set_footer(
                                        text="Made by Efaz from efaz.dev - v" + version,
                                        icon_url="https://cdn.discordapp.com/attachments/1099414684286861332/1112068066319270019/1W.png",
                                    )
                                    channel = bot.get_channel(botToken["NotificationChannelId"])
                                    await channel.send(embed=embed)
                                else:
                                    await sendEmbed(
                                        ctx,
                                        "Code is already redeemed: " + arg,
                                        3,
                                    )
                            else:
                                userData[str(ctx.message.author.id)].append(arg)
                                with open("users.json", "w") as outfile:
                                    outfile.write(json.dumps(userData))
                                
                                extraString = ""
                                    
                                if not codes[arg]["Role"] == 0:
                                    try:
                                        guild = bot.get_guild(guildId)
                                        role_data = guild.get_role(codes[arg]["Role"])
                                        await ctx.message.author.add_roles(role_data)
                                        extraString = " | Role Added: " + role_data.name
                                    except Exception as e:
                                        extraString = " | Role Added: (failed due to invalid permissions or error.)"

                                await sendEmbed(
                                    ctx,
                                    "You have redeemed perm code: "
                                    + arg
                                    + " for reward: "
                                    + codeInfo["Reward"] + extraString,
                                    1,
                                )
                                print(
                                    ctx.message.author.name + " has redeemed a code: " + arg
                                )

                                decimal = 65480
                                embed = discord.Embed(
                                    color=decimal,
                                    title="Merch Code System",
                                    description="User " + "<@" + str(ctx.message.author.id) + ">" + " has redeemed a perm code: " + arg + " for reward: " + codeInfo["Reward"],
                                )
                                embed.set_footer(
                                    text="Made by Efaz from efaz.dev - v" + version,
                                    icon_url="https://cdn.discordapp.com/attachments/1099414684286861332/1112068066319270019/1W.png",
                                )
                                channel = bot.get_channel(botToken["NotificationChannelId"])
                                await channel.send(embed=embed)
                    else:
                        await sendEmbed(ctx, "Code doesn't exist.", 3)
                else:
                    usersSavedData = []
                    userData[str(ctx.message.author.id)] = usersSavedData
                    print("User requested to look for code: " + arg)
                    if testIfVariableExists(codes, arg):
                        codeInfo = codes[arg]
                        if testIfVariableExists(usersSavedData, arg):
                            await sendEmbed(ctx, "User has already used this code.", 3)
                        else:
                            if codeInfo["OneUserOnly"] == True:
                                if codes[arg]["Redeemed"] == False:
                                    userData[str(ctx.message.author.id)].append(arg)
                                    codes[arg]["Redeemed"] = True
                                    with open("codes.json", "w") as outfile:
                                        outfile.write(json.dumps(codes))
                                    with open("users.json", "w") as outfile:
                                        outfile.write(json.dumps(userData))

                                    extraString = ""
                                    
                                    if not codes[arg]["Role"] == 0:
                                        try:
                                            guild = bot.get_guild(guildId)
                                            role_data = guild.get_role(codes[arg]["Role"])
                                            await ctx.message.author.add_roles(role_data)
                                            extraString = " | Role Added: " + role_data.name
                                        except Exception as e:
                                            extraString = " | Role Added: (failed due to invalid permissions or error.)"

                                    await sendEmbed(
                                        ctx,
                                        "You have redeemed merch code: "
                                        + arg
                                        + " for reward: "
                                        + codeInfo["Reward"] + extraString,
                                        1,
                                    )
                                    print(
                                        ctx.message.author.name + " has redeemed a code: " + arg
                                    )
        
                                    decimal = 65280
                                    embed = discord.Embed(
                                        color=decimal,
                                        title="Merch Code System",
                                        description="User " + "<@" + str(ctx.message.author.id) + ">" + " has redeemed a merch code: " + arg + " for reward: " + codeInfo["Reward"],
                                    )
                                    embed.set_footer(
                                        text="Made by Efaz from efaz.dev - v" + version,
                                        icon_url="https://cdn.discordapp.com/attachments/1099414684286861332/1112068066319270019/1W.png",
                                    )
                                    channel = bot.get_channel(botToken["NotificationChannelId"])
                                    await channel.send(embed=embed)
                                else:
                                    await sendEmbed(
                                        ctx,
                                        "Code is already redeemed: " + arg,
                                        3,
                                    )
                            else:
                                userData[str(ctx.message.author.id)].append(arg)
                                with open("users.json", "w") as outfile:
                                    outfile.write(json.dumps(userData))

                                extraString = ""
                                    
                                if not codes[arg]["Role"] == 0:
                                    try:
                                        guild = bot.get_guild(guildId)
                                        role_data = guild.get_role(codes[arg]["Role"])
                                        await ctx.message.author.add_roles(role_data)
                                        extraString = " | Role Added: " + role_data.name
                                    except Exception as e:
                                        extraString = " | Role Added: (failed due to invalid permissions or error.)"

                                await sendEmbed(
                                    ctx,
                                    "You have redeemed perm code: "
                                    + arg
                                    + " for reward: "
                                    + codeInfo["Reward"] + extraString,
                                    1,
                                )
                                print(
                                    ctx.message.author.name + " has redeemed a code: " + arg
                                )

                                decimal = 65480
                                embed = discord.Embed(
                                    color=decimal,
                                    title="Merch Code System",
                                    description="User " + "<@" + str(ctx.message.author.id) + ">" + " has redeemed a perm code: " + arg + " for reward: " + codeInfo["Reward"],
                                )
                                embed.set_footer(
                                    text="Made by Efaz from efaz.dev - v" + version,
                                    icon_url="https://cdn.discordapp.com/attachments/1099414684286861332/1112068066319270019/1W.png",
                                )
                                channel = bot.get_channel(botToken["NotificationChannelId"])
                                await channel.send(embed=embed)
                    else:
                        await sendEmbed(ctx, "Code doesn't exist.", 3)
            else:
                await sendEmbed(ctx, "Code not found in message.", 3)

        @bot.command()
        async def ping(ctx):
            if blacklisted(ctx) == True:
                await sendEmbed(ctx, "Access Denied", 3)
                return
            await sendEmbed(ctx, f"Pong! {round(bot.latency * 1000)}ms", 2)

        @bot.command()
        async def createCode(ctx, args1, args2, args3, args4="0"):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbed(ctx, "Access Denied", 3)
            else:
                print("returns True")
                if args1:
                    if args2:
                        if testIfVariableExists(codes, args1):
                            await sendEmbed(ctx, "Code already exists: " + args1, 2)
                        else:
                            if testIfInt(args4):
                                if args3 == "true":
                                    codes[args1] = {"Reward": args2, "OneUserOnly": False, "Role": int(args4)}
                                else:
                                    codes[args1] = {"Reward": args2, "OneUserOnly": True, "Redeemed": False, "Role": int(args4)}

                                with open("codes.json", "w") as outfile:
                                    outfile.write(json.dumps(codes))
                                await sendEmbed(ctx, "Created code: " + args1, 2)
                                print("Created code: " + args1)
                            else:
                                await sendEmbed(ctx, "Invalid Role ID: " + args1, 3)
                    
                    else:
                        await sendEmbed(ctx, "No reward Inputted in args2, not created", 3)
                        print("No reward Inputted in args2, not created")
                else:
                    await sendEmbed(ctx, "No Code Inputted in args1, not created", 3)
                    print("No Code Inputted in args1, not created")

        @bot.command()
        async def createRandomized(ctx, args1, args2, args3, args4="0"):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbed(ctx, "Access Denied", 3)
            else:
                print("returns True")
                prefix = args1
                code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
                args1 = prefix + code
                if args1:
                    if args2:
                        if testIfVariableExists(codes, args1):
                            await sendEmbed(ctx, "Code already exists: " + args1, 2)
                        else:
                            if testIfInt(args4):
                                if args3 == "true":
                                    codes[args1] = {"Reward": args2, "OneUserOnly": False, "Role": int(args4)}
                                else:
                                    codes[args1] = {"Reward": args2, "OneUserOnly": True, "Redeemed": False, "Role": int(args4)}

                                with open("codes.json", "w") as outfile:
                                    outfile.write(json.dumps(codes))
                                await sendEmbed(ctx, "Created code: " + args1, 2)
                                print("Created code: " + args1)
                            else:
                                await sendEmbed(ctx, "Invalid Role ID: " + args1, 3)
                    
                    else:
                        await sendEmbed(ctx, "No reward Inputted in args2, not created", 3)
                        print("No reward Inputted in args2, not created")
                else:
                    await sendEmbed(ctx, "No Code Inputted in args1, not created", 3)
                    print("No Code Inputted in args1, not created")

        @bot.command()
        async def searchUser(ctx, user: discord.Member):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbed(ctx, "Access Denied", 3)
            else:
                id = str(user.id)
                if testIfVariableExists(userData, id):
                    message = "User has redeemed codes: "
                    for i in userData[id]:
                        message = message + "\n `" + i + "` "
                    await sendEmbed(ctx, message, 2)
                else:
                    await sendEmbed(ctx, "This user has no code data or redeemed any codes.", 3)

        @bot.command()
        async def about(ctx):
            if blacklisted(ctx) == True:
                await sendEmbed(ctx, "Access Denied", 3)
            else:
                main_about_string = f"**Made by Efaz at [efaz.dev](https://www.efaz.dev)** \nScript Version: `v{version}` \nSystem OS: `{platform.system()}` "
                main_about_string = main_about_string + "\n Admins: "
                for admin in botToken["Admins"]:
                    main_about_string = main_about_string + "<@" + str(admin) + "> "

                if economy['Enabled'] == True:
                    main_about_string = main_about_string + f"\n\n**Economy** \nEnabled: `{str(economy['Enabled'])}` \nCurrency Name: `{economy['EconomyName']}` "
                    if economy["GreatReset"]["Enabled"] == True:
                        main_about_string = main_about_string + f"\nGreat Resets Enabled: `{str(economy['GreatReset']['Enabled'])}` \nSeason Number: `{str(economy['GreatReset']['SeasonNumber'])}` "
                    else:
                        main_about_string = main_about_string + f"\nGreat Resets Enabled: `{str(economy['GreatReset']['Enabled'])}` "
                else:
                    main_about_string = main_about_string + f"\n\n**Economy** \nEnabled: `{str(economy['Enabled'])}` "

                await sendEmbed(ctx, main_about_string, 2)

        @bot.command()
        async def createMultipleRandomized(ctx, args1, args2, args3, args4, args5="0"):
            if args4 < 0:
                args4 = args4 * -1
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbed(ctx, "Access Denied", 3)
            else:
                print("returns True")

                list = []
                count = args4
                prefix = args1
                message = "New codes: "
                
                for _ in range(count):
                    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
                    args1 = prefix + code
                    if args1:
                        if args2:
                            if testIfVariableExists(codes, args1):
                                await sendEmbed(ctx, "Code already exists: " + args1, 2)
                            else:
                                if testIfInt(args5):
                                    if args3 == "true":
                                        codes[args1] = {"Reward": args2, "OneUserOnly": False, "Role": int(args4)}
                                    else:
                                        codes[args1] = {"Reward": args2, "OneUserOnly": True, "Redeemed": False, "Role": int(args4)}

                                    with open("codes.json", "w") as outfile:
                                        outfile.write(json.dumps(codes))
                                    list.append(args1)
                                    print("Created code: " + args1)
                                else:
                                    await sendEmbed(ctx, "Invalid Role ID: " + args1, 3)
                        else:
                            print("No reward Inputted in args2, not created")
                    else:
                        print("No Code Inputted in args1, not created")
                for i in list:
                    message = message + "\n `" + i + "` : `" + codes[i]["Reward"] + "` "
                
                await sendEmbed(ctx, message, 2)

        @bot.command()
        async def viewCodes(ctx):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbed(ctx, "Access Denied", 3)
            else:
                print("returns True")
                ListOfCodes = list(codes.keys())
                string = "List of **available** codes: "
                listNotAvailable = "List of not **available** codes: "
                for i in ListOfCodes:
                    if codes[i]["OneUserOnly"] == True:
                        if codes[i]["Redeemed"] == False:
                            if codes[i]["Role"] == 0:
                                string = string + "\n `" + i + "` : `" + codes[i]["Reward"] + "` "
                            else:
                                string = string + "\n `" + i + "` : `" + codes[i]["Reward"] + "` : <@&" + str(codes[i]["Role"]) + "> "
                        else:
                            if codes[i]["Role"] == 0:
                                listNotAvailable = listNotAvailable + "\n `" + i + "` : `" + codes[i]["Reward"] + "` "
                            else:
                                listNotAvailable = listNotAvailable + "\n `" + i + "` : `" + codes[i]["Reward"] + "` : <@&" + str(codes[i]["Role"]) + "> "
                    else:
                        if codes[i]["Role"] == 0:
                            string = string + "\n `" + i + "` : `" + codes[i]["Reward"] + "` "
                        else:
                            string = string + "\n `" + i + "` : `" + codes[i]["Reward"] + "` : <@&" + str(codes[i]["Role"]) + "> "

                await sendEmbed(ctx, string + " \n\n" + listNotAvailable, 2)

        @bot.command()
        async def clearAlreadyRedeemed(ctx):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbed(ctx, "Access Denied", 3)
            else:
                print("returns True")
                ListOfCodes = list(codes.keys())
                listNotAvailable = "List of **cleared** codes: "
                for i in ListOfCodes:
                    if codes[i]["OneUserOnly"] == True:
                        if codes[i]["Redeemed"] == True:
                            try:
                                add_string = "\n `" + i + "` : `" + codes[i]["Reward"] + "` "
                                
                                if not codes[i]["Role"] == 0:
                                    add_string = add_string + " : <@&" + str(codes[i]["Role"]) + "> "

                                codes.pop(i, None)
                                listNotAvailable = listNotAvailable + add_string
                            except Exception as e:
                                print("Failed to remove code: " + str(e))
                with open("codes.json", "w") as outfile:
                    outfile.write(json.dumps(codes))
                await sendEmbed(ctx, listNotAvailable, 2)

        @bot.command()
        async def deleteCode(ctx, arg1):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbed(ctx, "Access Denied", 3)
            else:
                if arg1:
                    if testIfVariableExists(codes, arg1):
                        codes.pop(arg1)
                        with open("codes.json", "w") as outfile:
                            outfile.write(json.dumps(codes))
                        await sendEmbed(ctx, "Code has been removed from the system", 2)
                    else:
                        await sendEmbed(ctx, "Code not found", 3)
                else:
                    await sendEmbed(ctx, "No arg1 found", 3)
        
        @bot.command()
        async def blacklist(ctx, user: discord.Member, reason):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbed(ctx, "Access Denied", 3)
            else:
                id = str(user.id)
                blackListedUsers = botToken["BlacklistedUsers"]
                if testIfVariableExists(blackListedUsers, id):
                    await sendEmbed(ctx, "User is already blacklisted from the bot.", 3)
                else:
                    botToken["BlacklistedUsers"][id] = reason
                    with open("bot.json", "w") as outfile:
                        outfile.write(json.dumps(botToken))
                    await sendEmbed(ctx, "User has been blacklisted from this bot. Any operations or actions to this bot from this user has been blocked.", 2)

        @bot.command()
        async def unblacklist(ctx, user: discord.Member):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbed(ctx, "Access Denied", 3)
            else:
                id = str(user.id)
                blackListedUsers = botToken["BlacklistedUsers"]
                if testIfVariableExists(blackListedUsers, id):
                    botToken["BlacklistedUsers"].pop(id)
                    with open("bot.json", "w") as outfile:
                        outfile.write(json.dumps(botToken))
                    await sendEmbed(ctx, "User has been unblacklisted from the bot.", 2)
                else:
                    await sendEmbed(ctx, "User is not blacklisted from the bot.", 3)

        

        @bot.command()
        async def blacklistyourself(ctx, reason):
            if blacklisted(ctx) == True:
                print("returns False")
                await sendEmbed(ctx, "Access Denied", 3)
            else:
                user = ctx.message.author
                id = str(user.id)
                blackListedUsers = botToken["BlacklistedUsers"]
                if testIfVariableExists(blackListedUsers, id):
                    await sendEmbed(ctx, "You're already blacklisted from the bot.", 3)
                else:
                    botToken["BlacklistedUsers"][id] = reason + " (Used Blacklist Yourself Command)"
                    with open("bot.json", "w") as outfile:
                        outfile.write(json.dumps(botToken))
                    await sendEmbed(ctx, "You're blacklisted from using the bot. Command operation is finished.", 2)

        @bot.command()
        async def viewBlacklistReason(ctx, user: discord.Member):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbed(ctx, "Access Denied", 3)
            else:
                id = str(user.id)
                blackListedUsers = botToken["BlacklistedUsers"]
                if testIfVariableExists(blackListedUsers, id):
                    await sendEmbed(ctx, f"<@{id}> has been blacklisted for: {botToken['BlacklistedUsers'][id]}", 2)
                else:
                    await sendEmbed(ctx, "User is not blacklisted from the bot.", 3)

        @bot.command()
        async def shutdown(ctx):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                await sendEmbed(ctx, "Access Denied", 3)
            else:
                await sendEmbed(ctx, "Bot is now shutting down. Thanks for using Efaz's Merch Code System, see you next time!", 2)
                print("Bot is shutting down..")
                await bot.change_presence(status=discord.Status.offline)
                printSystemMessage("Bot shut down, returning back to Command Prompt.")
                printSystemMessage("Thanks for using Efaz's Merch Code System, see you next time!")
                await bot.close()
                exit()

        # Economy Commands

        if economy["Enabled"] == True:
            def cooldownCommand(userId):
                if testIfVariableExists(economy["UserData"], str(userId)):
                    if economy["UserData"][str(userId)]["Cooldown"] > datetime.now().timestamp():
                        return True
                    else:
                        return False
                else:
                    economy["UserData"][str(userId)] = {
                            "Balance": 0,
                            "Inventory": [],
                            "LatestDate": 0,
                            "Cooldown": 0,
                    }
                    return False
            def setCooldown(userId):
                if userId in botToken["Admins"]:
                    return
                economy["UserData"][str(userId)]["Cooldown"] = datetime.now().timestamp() + 120
                with open("economy.json", "w") as outfile:
                    outfile.write(json.dumps(economy))
            def checkCurrencyAmount(userId):
                if testIfVariableExists(economy["UserData"], str(userId)):
                    return round(economy["UserData"][str(userId)]["Balance"])
                else:
                    return 0
            
            def createCurrency(userId, amount):
                if amount < 0:
                    amount = amount * -1
                if testIfVariableExists(economy["UserData"], str(userId)):
                    economy["UserData"][str(userId)]["Balance"] = round(economy["UserData"][str(userId)]["Balance"] + amount)
                    with open("economy.json", "w") as outfile:
                        outfile.write(json.dumps(economy))
                    return True
                else:
                    economy["UserData"][str(userId)] = {
                        "Balance": 0,
                        "Inventory": [],
                        "LatestDate": 0,
                        "Cooldown": 0,
                    }
                    economy["UserData"][str(userId)]["Balance"] = round(economy["UserData"][str(userId)]["Balance"] + amount)
                    with open("economy.json", "w") as outfile:
                        outfile.write(json.dumps(economy))
                    return True
            
            def takeCurrency(userId, amount):
                if amount < 0:
                    amount = amount * -1
                if checkCurrencyAmount(userId) >= amount:
                    if testIfVariableExists(economy["UserData"], str(userId)):
                        economy["UserData"][str(userId)]["Balance"] = round(economy["UserData"][str(userId)]["Balance"] - amount)
                        with open("economy.json", "w") as outfile: 
                            outfile.write(json.dumps(economy))
                        return True
                    else:
                        return False
                else:
                    return False
                
            def applyRoleMultiplier(user):
                listOfRolesWithMultipliers = economy["RoleMultiplier"]
                highestMultiplier = 1
                for i in listOfRolesWithMultipliers:
                    if bot.get_guild(guildId).get_role(i["roleid"]) in user.roles:
                        if i["multiplier"] > highestMultiplier:
                            highestMultiplier = i["multiplier"]
                return highestMultiplier

            @bot.command()
            async def flipCoin(ctx, amount, guess):
                if cooldownCommand(ctx.message.author.id):
                    await sendEmbed(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                else:
                    setCooldown(ctx.message.author.id)
                amount = int(amount)
                if amount < 0:
                    amount = amount * -1
                if blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    if guess == "Tails" or guess == "Heads":
                        if takeCurrency(ctx.message.author.id, amount):
                            randomized = random.randint(1, 2)
                            if randomized == 1:
                                await sendEmbed(ctx, "🪙 Heads!", 2)
                                if guess == "Heads":
                                    createCurrency(ctx.message.author.id, amount * 2)
                            else:
                                await sendEmbed(ctx, "🪙 Tails!", 2)
                                if guess == "Tails":
                                    createCurrency(ctx.message.author.id, amount * 2)
                        else:    
                            await sendEmbed(ctx, "Failed to take money: Insufficent Balance", 3)
                    else:
                        await sendEmbed(ctx, "Failed, guess must be either `Heads` or `Tails`", 3)
            @bot.command()
            async def gamble(ctx, estimate, max, amount):
                if cooldownCommand(ctx.message.author.id):
                    await sendEmbed(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                else:
                    setCooldown(ctx.message.author.id)
                estimate = int(estimate)
                max = int(max)
                amount = int(amount)

                if max < 0:
                    max = max * -1
                if amount < 0:
                    amount = amount * -1
                if estimate < 0:
                    estimate = estimate * -1

                if blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    if takeCurrency(ctx.message.author.id, amount):
                        randomized = random.randint(1, max)
                        if randomized == estimate:
                            await sendEmbed(ctx, "Success! You got it! Chances: " + str(round(1 / max * 100)) + "%", 2)
                            createCurrency(ctx.message.author.id, amount * max)
                        else:
                            await sendEmbed(ctx, "Failed! R.I.P. Chances: " + str(round(1 / max * 100)) + "%", 2)
                    else:
                        await sendEmbed(ctx, "Failed to take money: Insufficent Balance", 3)

            @bot.command()
            async def createcurrency(ctx, user: discord.Member, amount: int):
                if amount < 0:
                    amount = amount * -1
                if cooldownCommand(ctx.message.author.id):
                    await sendEmbed(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                else:
                    setCooldown(ctx.message.author.id)
                if predicate(ctx) == False or blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    if not testIfVariableExists(economy["UserData"], str(ctx.message.author.id)):
                        economy["UserData"][str(ctx.message.author.id)] = {
                            "Balance": 0,
                            "Inventory": [],
                            "LatestDate": 0,
                            "Cooldown": 0,
                        }
                    response = createCurrency(user.id, amount)
                    if response == True:
                        await sendEmbed(ctx, "Gave " + str(amount) + " currency to " + user.name + "!", 2)
                    else:
                        await sendEmbed(ctx, "Failed! Issue while giving user money.", 2)
            @bot.command()
            async def removecurrency(ctx, user: discord.Member, amount: int):
                if amount < 0:
                    amount = amount * -1
                if cooldownCommand(ctx.message.author.id):
                    await sendEmbed(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                else:
                    setCooldown(ctx.message.author.id)
                if predicate(ctx) == False or blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    if not testIfVariableExists(economy["UserData"], str(ctx.message.author.id)):
                        economy["UserData"][str(ctx.message.author.id)] = {
                            "Balance": 0,
                            "Inventory": [],
                            "LatestDate": 0,
                            "Cooldown": 0,
                        }
                    response = takeCurrency(user.id, amount)
                    if response == True:
                        await sendEmbed(ctx, "Gave " + str(amount) + " currency to " + user.name + "!", 2)
                    else:
                        await sendEmbed(ctx, "Failed to take money: Insufficent Balance", 3)

            @bot.command()
            async def balance(ctx, user: discord.Member):
                if blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    response = checkCurrencyAmount(user.id)
                    await sendEmbed(ctx, user.name + "'s Balance: \n" + str(response) + " " + economy["EconomyName"], 2)

            @bot.command()
            async def daily(ctx):
                if cooldownCommand(ctx.message.author.id):
                    await sendEmbed(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                if blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    if not testIfVariableExists(economy["UserData"], str(ctx.message.author.id)):
                        economy["UserData"][str(ctx.message.author.id)] = {
                            "Balance": 0,
                            "Inventory": [],
                            "LatestDate": 0,
                            "Cooldown": 0,
                        }
                    if economy["UserData"][str(ctx.message.author.id)]["LatestDate"] <= datetime.now().timestamp():
                        economy["UserData"][str(ctx.message.author.id)]["LatestDate"] = datetime.now().timestamp() + 86400
                        response = createCurrency(ctx.message.author.id, economy["Commands"]["Daily"] * applyRoleMultiplier(ctx.message.author))
                        if response == True:
                            await sendEmbed(ctx, "You've received " + str(economy["Commands"]["Daily"] * applyRoleMultiplier(ctx.message.author)) + " " + economy["EconomyName"] + "! Come back in 24 hours!", 2)
                    else:
                        await sendEmbed(ctx, "Time is still remaining. Please wait!", 3)

            @bot.command()
            async def buy(ctx, itemname: str):
                if blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    if cooldownCommand(ctx.message.author.id):
                        await sendEmbed(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                        return
                    else:
                        setCooldown(ctx.message.author.id)
                    if testIfVariableExists(StoreItems, itemname):
                        item = StoreItems[itemname]
                        if item["stock"] > 0:
                            if len(economy["UserData"][str(ctx.message.author.id)]["Inventory"]) + 1 > economy["InventoryLimit"]:
                                await sendEmbed(ctx, "Failed to buy item: No storage left, use an item in your inventory and try again!", 3)
                                return
                            if takeCurrency(ctx.message.author.id, item["price"]):
                                if not item["role"] == 0:
                                    if not bot.get_guild(guildId).get_role(item["role"]) in ctx.user.roles:
                                        await ctx.message.author.add_roles(bot.get_guild(guildId).get_role(item["role"]))
                                StoreItems[itemname]["stock"] = StoreItems[itemname]["stock"] - 1
                                economy["UserData"][str(ctx.message.author.id)]["Inventory"].append(itemname)
                                with open("economy.json", "w") as outfile:
                                    outfile.write(json.dumps(economy))
                                await sendEmbed(ctx, "Bought: " + itemname + "!", 2)
                            else:
                                await sendEmbed(ctx, "Failed to take money: Insufficent Balance", 3)
                        else:
                            await sendEmbed(ctx, "Failed to buy item: No stock for item is left.", 3)
                    else:
                        await sendEmbed(ctx, "Item is not found.", 3)
                        
            @bot.command()
            async def inventory(ctx):
                if blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    if cooldownCommand(ctx.message.author.id):
                        await sendEmbed(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                        return
                    if not testIfVariableExists(economy["UserData"], str(ctx.message.author.id)):
                        await sendEmbed(ctx, "No inventory found", 3)
                        return
                    userInventory = economy["UserData"][str(ctx.message.author.id)]["Inventory"]
                    message = "User's inventory: \n"
                    for i in userInventory:
                        message = message + "`" + i + "` \n"
                    await sendEmbed(ctx, message, 2)

            @bot.command()
            async def use(ctx, item: str):
                if blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    if cooldownCommand(ctx.message.author.id):
                        await sendEmbed(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                        return
                    if not testIfVariableExists(economy["UserData"], str(ctx.message.author.id)):
                        await sendEmbed(ctx, "No inventory found", 3)
                        return
                    userInventory = economy["UserData"][str(ctx.message.author.id)]["Inventory"]
                    itemFromInventory = ""
                    for i in userInventory:
                        if i == item:
                            itemFromInventory = item
                    
                    if itemFromInventory == "":
                        await sendEmbed(ctx, "Item is not found in your inventory", 3)
                    else:
                        itemLookUp = StoreItems[item]
                        if not itemLookUp["role"] == 0:
                            if bot.get_guild(guildId).get_role(itemLookUp["role"]) in ctx.user.roles:
                                print("User already has role, ignored.")
                            else:
                                await ctx.message.author.add_roles(bot.get_guild(guildId).get_role(itemLookUp["role"]))
                        economy["UserData"][str(ctx.message.author.id)]["Inventory"].remove(itemFromInventory)
                        with open("economy.json", "w") as outfile:
                            outfile.write(json.dumps(economy))

                        decimal = 65280
                        embed = discord.Embed(
                            color=decimal,
                            title="Merch Code System",
                            description="User " + "<@" + str(ctx.message.author.id) + ">" + " has redeemed a item: " + itemFromInventory,
                        )
                        embed.set_footer(
                            text="Made by Efaz from efaz.dev - v" + version,
                            icon_url="https://cdn.discordapp.com/attachments/1099414684286861332/1112068066319270019/1W.png",
                        )
                        channel = bot.get_channel(botToken["NotificationChannelId"])
                        await channel.send(embed=embed)

                        await sendEmbed(ctx, "Item used!", 2)

            @bot.command()
            async def createItem(ctx, item: str, stock: int, price: int, roleid: str="0"):
                if cooldownCommand(ctx.message.author.id):
                    await sendEmbed(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                else:
                    setCooldown(ctx.message.author.id)
                if price < 0:
                    price = price * -1
                if stock < 0:
                    stock = stock * -1

                roleId = int(roleId)
                if not roleId:
                    roleId = 0

                if roleId < 0:
                    roleId = roleId * -1

                if predicate(ctx) == False or blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    economy["StoreInventory"][item] = {
                        "stock": stock,
                        "price": price,
                        "name": item,
                        "role": roleId
                    }
                    with open("economy.json", "w") as outfile:
                        outfile.write(json.dumps(economy))
                    await sendEmbed(ctx, "Created item!", 2)

            @bot.command()
            async def viewstorestock(ctx):
                if cooldownCommand(ctx.message.author.id):
                    await sendEmbed(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                if blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    message = "Store Inventory: \n"
                    instock = "** In Stock ** \n"
                    outstock = "** Out of Stock ** \n"
                    for i in economy["StoreInventory"].keys():
                        item = economy["StoreInventory"][i]
                        if item["stock"] > 0:
                            instock = instock + "`" + item["name"] + "` | Price: `" + str(item["price"]) + "` | Stock: `" + str(item["stock"]) + "` \n"
                        else:
                            outstock = outstock + "`" + item["name"] + "` | Price: `" + str(item["price"]) + "` \n"

                    if instock == "** In Stock ** \n":
                        instock = "** In Stock ** \n No items available \n"
                    if outstock == "** Out of Stock ** \n":
                        outstock = "** Out of Stock ** \n No items out of stock \n"
                    await sendEmbed(ctx, message + instock + outstock, 2)    

            @bot.command()
            async def rob(ctx, user: discord.Member):
                if cooldownCommand(ctx.message.author.id):
                    await sendEmbed(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                else:
                    setCooldown(ctx.message.author.id)
                if blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    if user.id in botToken["Admins"]:
                        await sendEmbed(ctx, "Failed! You can't rob the admins of this bot!", 3)
                        return
                    randomized = random.randint(1, economy["SuccessRate"])
                    if checkCurrencyAmount(ctx.message.author.id) >= 1:
                        if randomized == 1:
                            amount = checkCurrencyAmount(user.id) * 0.5
                            response = takeCurrency(user.id, amount)
                            response2 = createCurrency(ctx.message.author.id, amount)
                            await sendEmbed(ctx, "Robbing Success! You have earned " + str(amount) + " " + economy["EconomyName"] + "!", 2)
                        else:
                            amount = checkCurrencyAmount(ctx.message.author.id) * 0.5
                            response = takeCurrency(ctx.message.author.id, amount)
                            await sendEmbed(ctx, "Robbing Failed! You have been charged " + str(amount) + " " + economy["EconomyName"] + "!", 3)
                    else:
                        await sendEmbed(ctx, "Robbing Failed! You have no money to use for this command!", 3)

            @bot.command()
            async def sendMoney(ctx, user: discord.Member, amount: int):
                if cooldownCommand(ctx.message.author.id):
                    await sendEmbed(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                else:
                    setCooldown(ctx.message.author.id)
                if amount < 0:
                    amount = amount * -1
                if blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    if checkCurrencyAmount(ctx.message.author.id) >= amount:
                        response = takeCurrency(ctx.message.author.id, amount)
                        response2 = createCurrency(user.id, amount)
                        await sendEmbed(ctx, "You have gave " + str(amount) + " " + economy["EconomyName"] + " to " + user.name + "!", 2)
                    else:
                        await sendEmbed(ctx, "Not enough funds!", 3)
            
            @bot.command()
            async def work(ctx):
                if cooldownCommand(ctx.message.author.id):
                    await sendEmbed(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                else:
                    setCooldown(ctx.message.author.id)
                if blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    jobList = economy["JobList"]
                    randomizedJob = jobList[random.randint(0, len(jobList) - 1)]
                    response = createCurrency(ctx.message.author.id, randomizedJob["amount"] * applyRoleMultiplier(ctx.message.author))
                    await sendEmbed(ctx, "You have earned " + str(randomizedJob["amount"] * applyRoleMultiplier(ctx.message.author)) + " from working as a " + randomizedJob["name"] + "!", 2)

            @bot.command()
            async def cooldownCheck(ctx):
                if blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    await sendEmbed(ctx, "Cooldown ends <t:" + str(round(economy["UserData"][str(ctx.message.author.id)]["Cooldown"])) + ":R>", 2)

            @bot.command()
            async def topleaderboard(ctx):
                if blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    lbList = economy["UserData"]
                    lbList = dict(sorted(lbList.items(), reverse=True, key=lambda x:x[1]["Balance"]))

                    message = "Top **10** Leaderboard! \n ** " + economy["EconomyName"] + " ** \n"

                    if len(lbList) < 10:
                        keys = lbList.keys()
                        for i in keys:
                            message = message + "<@" + str(i) + "> | " + str(economy["UserData"][i]["Balance"]) + " \n"
                    else:
                        keys = list(lbList.keys())
                        for i in range(10):
                            message = message + "<@" + str(keys[i]) + "> | " + str(economy["UserData"][keys[i]]["Balance"]) + " \n"

                    message = message + " ** Number of Items ** \n"
                    lbList = dict(sorted(lbList.items(), reverse=True, key=lambda x:len(x[1]["Inventory"])))

                    if len(lbList) < 10:
                        keys = lbList.keys()
                        for i in keys:
                            message = message + "<@" + str(i) + "> | " + str(len(economy["UserData"][i]["Inventory"])) + " \n"
                    else:
                        keys = list(lbList.keys())
                        for i in range(10):
                            message = message + "<@" + str(keys[i]) + "> | " + str(len(economy["UserData"][keys[i]]["Inventory"])) + " \n"


                    await sendEmbed(ctx, message, 2)

            @bot.command()
            async def multiplierCheck(ctx):
                if blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    await sendEmbed(ctx, "Multiplier applied on non-user involved commands: " + str(applyRoleMultiplier(ctx.message.author)) + "x Multiplier", 2)

            @bot.command()
            async def endItemListing(ctx, item: str):
                if predicate(ctx) == False or blacklisted(ctx) == True:
                    await sendEmbed(ctx, "Access Denied", 3)
                else:
                    if testIfVariableExists(economy["StoreInventory"], item): 
                        if economy["StoreInventory"][item]["stock"] == 0:
                            await sendEmbed(ctx, "Failed to end item: Item is already ended stock", 3)
                            return
                        economy["StoreInventory"][item]["stock"] = 0
                        await sendEmbed(ctx, "Item's stock is finished!", 2)
                    else:
                        await sendEmbed(ctx, "Failed to end item: Item is not found", 3)

            if economy["GreatReset"]["Enabled"] == True:
                greatResetCurrently = False
                def checkIfCashKing(user):
                    try:
                        if bot.get_guild(guildId).get_role(economy["GreatReset"]["CashKingRoleID"]) in user.roles:
                            return True
                        else:
                            return False
                    except Exception:
                        return False
                
                @bot.command()
                async def greatReset(ctx, confirm: str):
                    if checkIfCashKing(ctx.message.author) == False or blacklisted(ctx) == True:
                        await sendEmbed(ctx, "Access Denied", 3)
                    else:
                        if confirm.lower() == "Yes":
                            global greatResetCurrently
                            if greatResetCurrently == False:
                                guild = bot.get_guild(guildId)
                                await sendEmbed(ctx, "Launched a new Great Reset wave! A new message will appear when the process is finished!", 2)
                                greatResetCurrently = True
                                # Remove Roles
                                if economy["GreatReset"]["DataToReset"]["Roles"] == True:
                                    for roleId in economy["GreatReset"]["RolesToReset"]:
                                        role = guild.get_role(roleId)
                                        print(f"Received Role: {role.name}, {role.id}")
                                        for member in role.members:
                                            try:
                                                await member.remove_roles(role)
                                                print("Removed role: " + role.name + " from: " + str(member.id))
                                            except Exception as e:
                                                print("Error while removing role: " + str(e))

                                # Restock Items
                                if economy["GreatReset"]["DataToReset"]["Items"] == True:
                                    for item in economy["GreatReset"]["ItemDataWhenRestock"]:
                                        economy["StoreInventory"][item["name"]] = item

                                        global StoreItems
                                        StoreItems = economy["StoreInventory"]

                                        # Delete Everyone's inventory
                                        for userData in economy["UserData"].keys():
                                            for itemInInv in economy["UserData"][userData]["Inventory"]:
                                                if itemInInv == item["name"]:
                                                    economy["UserData"][userData]["Inventory"].remove(item["name"])

                                # Reset Cash
                                if economy["GreatReset"]["DataToReset"]["Cash"] == True:
                                    for userData in economy["UserData"].keys():
                                        economy["UserData"][userData]["Balance"] = 0
                                        economy["UserData"][userData]["LatestDate"] = 0
                                        economy["UserData"][userData]["Cooldown"] = 0
                                        print("Reset Data of: " + userData)

                                # New Season
                                if economy["GreatReset"]["SeasonNumber"] < 1:
                                    economy["GreatReset"]["SeasonNumber"] = 1
                                economy["GreatReset"]["SeasonNumber"] = economy["GreatReset"]["SeasonNumber"] + 1

                                # SAVE DATA

                                with open("economy.json", "w") as outfile:
                                    outfile.write(json.dumps(economy))
                                print("Saved Data")
                                decimal = 65280
                                embed = discord.Embed(
                                    color=decimal,
                                    title="Merch Code System",
                                    description="Season " + str(economy["GreatReset"]["SeasonNumber"] - 1) + " is finished! Bot has reset what the owner has set to reset! <@" + str(ctx.user.id) + ">'s Cash King role has been removed! Welcome to Season " + str(economy["GreatReset"]["SeasonNumber"]) + "!",
                                )
                                embed.set_footer(
                                    text="Made by Efaz from efaz.dev",
                                    icon_url="https://cdn.discordapp.com/attachments/1099414684286861332/1112068066319270019/1W.png",
                                )
                                channel = bot.get_channel(botToken["NotificationChannelId"])
                                await channel.send(embed=embed)
                                await ctx.channel.send(embed=embed)
                                greatResetCurrently = False
                                print("Finished Great Reset")
                            else:
                                await sendEmbed(ctx, "An another great reset is happening. Please wait.", 3)
                        else:
                            await sendEmbed(ctx, "Cash King declined confirmation", 3)
        else:
            print("Economy Commands have not been applied to the bot, switch Enabled variable to True to enable economy commands.")

        # Login to bot
        print("Loaded, logging into bot...")
        bot.run(botToken["Token"])
    else:
        # slash commands

        intents = discord.Intents.default()
        bot = discord.Client(intents=intents)
        tree = app_commands.CommandTree(bot)
        guildId = botToken["ServerID"]

        @bot.event
        async def on_ready():
            await tree.sync(guild=discord.Object(id=guildId))
            print(f"Logged on the bot: " + bot.user.name)
            print("System is ready!")
            decimal = 16538115
            embed = discord.Embed(
                color=decimal,
                title="Merch Code System",
                description="Thanks for using Efaz's Merch Code System! Please put a star in our GitHub to support for newer updates!",
            )
            embed.set_footer(
                text="Made by Efaz from efaz.dev - v" + version,
                icon_url="https://cdn.discordapp.com/attachments/1099414684286861332/1112068066319270019/1W.png",
            )
            channel = bot.get_channel(botToken["NotificationChannelId"])
            await channel.send(embed=embed)
            status_task.start()

        @tasks.loop()
        async def status_task():
            while True:
                randomized = random.randint(1, 4)
                if randomized == 1:
                    await bot.change_presence(
                        activity=discord.Game(name=" Efaz's Merch Code System")
                    )
                elif randomized == 2:
                    await bot.change_presence(
                        activity=discord.Activity(type=discord.ActivityType.listening, name=" users redeeming codes")
                    )
                elif randomized == 3:
                    await bot.change_presence(
                        activity=discord.Streaming(name=" live redeeming codes", url="https://www.youtube.com/watch?v=Yr7txrMWRSs")
                    )
                else:
                    await bot.change_presence(
                        activity=discord.Activity(type=discord.ActivityType.watching, name=" giving rewards from codes")
                    )
                await asyncio.sleep(10)

        async def sendEmbedTree(ctx, message, colorType):
            decimal = None
            if colorType == 1:
                decimal = 65280
            elif colorType == 2:
                decimal = 16538115
            else:
                decimal = 16711680
            embed = discord.Embed(
                color=decimal, title="Merch Code System", description=message
            )
            embed.set_footer(
                text="Made by Efaz from efaz.dev - v" + version,
                icon_url="https://cdn.discordapp.com/attachments/1099414684286861332/1112068066319270019/1W.png",
            )
            print("User " + ctx.user.name + " used command: " + ctx.message)
            await ctx.response.send_message(embed=embed)

        def predicate(ctx):
            if ctx.user.id in botToken["Admins"]:
                return True
            else:
                return False
            
        def blacklisted(ctx):
            if testIfVariableExists(botToken["BlacklistedUsers"], str(ctx.user.id)):
                return True
            else:
                return False

        @tree.command(
            name="createcode",
            description="Create code in the system",
            guild=discord.Object(id=guildId),
        )
        async def createcode(
            interaction: discord.Interaction, code: str, reward: str, permornot: bool, roleid: str="0"
        ):
            ctx = interaction
            if predicate(ctx) == False or blacklisted(ctx) == True:
                await sendEmbedTree(ctx, "Access Denied", 3)
            else:
                if code:
                    if reward:
                        if testIfVariableExists(codes, code):
                            await sendEmbedTree(ctx, "Code already exists: " + code, 2)
                        else:
                            if testIfInt(roleid):
                                if permornot == False:
                                    codes[code] = {"Reward": reward, "OneUserOnly": True, "Redeemed": False, "Role": int(roleid)}
                                else:
                                    codes[code] = {"Reward": reward, "OneUserOnly": False, "Role": int(roleid)}

                                with open("codes.json", "w") as outfile:
                                    outfile.write(json.dumps(codes))
                                await sendEmbedTree(ctx, "Created code: " + code, 2)
                                print("Created code: " + code)
                            else:
                                await sendEmbedTree(ctx, "Invalid Role ID: " + roleid, 3)
                    else:
                        await sendEmbedTree(
                            ctx, "No reward Inputted in reward, not created", 3
                        )
                        print("No reward Inputted in reward, not created")
                else:
                    await sendEmbedTree(ctx, "No Code Inputted in code, not created", 3)
                    print("No Code Inputted in code, not created")

        @tree.command(
            name="createrandomized",
            description="Create a randomized code",
            guild=discord.Object(id=guildId),
        )
        async def createRandomized(
            interaction: discord.Interaction, prefix: str, reward: str, permornot: bool, roleid: str="0"
        ):
            ctx = interaction
            if predicate(ctx) == False or blacklisted(ctx) == True:
                await sendEmbedTree(ctx, "Access Denied", 3)
            else:
                randomized = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
                code = prefix + randomized
                if code:
                    if reward:
                        if testIfVariableExists(codes, code):
                            await sendEmbedTree(ctx, "Code already exists: " + code, 2)
                        else:
                            if testIfInt(roleid):
                                if permornot == False:
                                    codes[code] = {"Reward": reward, "OneUserOnly": True, "Redeemed": False, "Role": int(roleid)}
                                else:
                                    codes[code] = {"Reward": reward, "OneUserOnly": False, "Role": int(roleid)}

                                with open("codes.json", "w") as outfile:
                                    outfile.write(json.dumps(codes))
                                await sendEmbedTree(ctx, "Created code: " + code, 2)
                                print("Created code: " + code)
                            else:
                                await sendEmbedTree(ctx, "Invalid Role ID: " + roleid, 3)
                    else:
                        await sendEmbedTree(
                            ctx, "No reward Inputted in reward, not created", 3
                        )
                        print("No reward Inputted in reward, not created")
                else:
                    await sendEmbedTree(ctx, "No Code Inputted in code, not created", 3)
                    print("No Code Inputted in code, not created")

        @tree.command(
            name="refreshlists",
            description="Refresh all lists",
            guild=discord.Object(id=guildId),
        )
        async def refreshLists(ctx: discord.Interaction):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                await sendEmbedTree(ctx, "Access Denied", 3)
            else:
                print("Loading System Data (codes, users, bot)")
                loadLists()
                StoreItems = economy["StoreInventory"]
                print("Loaded Saved Data in JSONs")
                await sendEmbedTree(ctx, "Refreshed List, restarting main.py script.", 2)

        @tree.command(
            name="viewcodes",
            description="View all codes in the list",
            guild=discord.Object(id=guildId),
        )
        async def viewCodes(ctx: discord.Interaction):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbedTree(ctx, "Access Denied", 3)
            else:
                print("returns True")
                ListOfCodes = list(codes.keys())
                string = "List of **available** codes: "
                listNotAvailable = "List of **not available** codes: "
                for i in ListOfCodes:
                    if codes[i]["OneUserOnly"] == True:
                        if codes[i]["Redeemed"] == False:
                            if codes[i]["Role"] == 0:
                                string = string + "\n `" + i + "` : `" + codes[i]["Reward"] + "` "
                            else:
                                string = string + "\n `" + i + "` : `" + codes[i]["Reward"] + "` : <@&" + str(codes[i]["Role"]) + "> "
                        else:
                            if codes[i]["Role"] == 0:
                                listNotAvailable = listNotAvailable + "\n `" + i + "` : `" + codes[i]["Reward"] + "` "
                            else:
                                listNotAvailable = listNotAvailable + "\n `" + i + "` : `" + codes[i]["Reward"] + "` : <@&" + str(codes[i]["Role"]) + "> "
                    else:
                        if codes[i]["Role"] == 0:
                            string = string + "\n `" + i + "` : `" + codes[i]["Reward"] + "` "
                        else:
                            string = string + "\n `" + i + "` : `" + codes[i]["Reward"] + "` : <@&" + str(codes[i]["Role"]) + "> "

                await sendEmbedTree(ctx, string + " \n\n" + listNotAvailable, 2)

        @tree.command(
            name="clearalreadyredeemedcodes",
            description="Clears and Deletes all already redeemed codes.",
            guild=discord.Object(id=guildId),
        )
        async def clearAlreadyRedeemed(ctx: discord.Interaction):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbedTree(ctx, "Access Denied", 3)
            else:
                print("returns True")
                ListOfCodes = list(codes.keys())
                listNotAvailable = "List of **cleared** codes: "
                for i in ListOfCodes:
                    if codes[i]["OneUserOnly"] == True:
                        if codes[i]["Redeemed"] == True:
                            try:
                                add_string = "\n `" + i + "` : `" + codes[i]["Reward"] + "` "

                                if not codes[i]["Role"] == 0:
                                    add_string = add_string + " : <@&" + str(codes[i]["Role"]) + "> "
                                
                                codes.pop(i, None)
                                listNotAvailable = listNotAvailable + add_string
                            except Exception as e:
                                print("Failed to remove code: " + str(e))
                with open("codes.json", "w") as outfile:
                    outfile.write(json.dumps(codes))
                await sendEmbedTree(ctx, listNotAvailable, 2)

        @tree.command(
            name="redeem",
            description="Redeem Code",
            guild=discord.Object(id=guildId),
        )
        async def redeem(ctx, code: str):
            if False or blacklisted(ctx) == True:
                await sendEmbedTree(ctx, "Access Denied", 3)
            else:
                if code:
                    if testIfVariableExists(userData, str(ctx.user.id)):
                        usersSavedData = userData[str(ctx.user.id)]
                        print("User requested to look for code: " + code)
                        if testIfVariableExists(codes, code):
                            codeInfo = codes[code]
                            if testIfVariableExists(usersSavedData, code):
                                await sendEmbedTree(ctx, "User has already used this code.", 3)
                            else:
                                if codeInfo["OneUserOnly"] == True:
                                    if codes[code]["Redeemed"] == False:
                                        userData[str(ctx.user.id)].append(code)
                                        codes[code]["Redeemed"] = True
                                        with open("codes.json", "w") as outfile:
                                            outfile.write(json.dumps(codes))
                                        with open("users.json", "w") as outfile:
                                            outfile.write(json.dumps(userData))

                                        extraString = ""
                                    
                                        if not codes[code]["Role"] == 0:
                                            try:
                                                guild = bot.get_guild(guildId)
                                                role_data = guild.get_role(codes[code]["Role"])
                                                await ctx.user.add_roles(role_data)
                                                extraString = " | Role Added: " + role_data.name
                                            except Exception as e:
                                                extraString = " | Role Added: (failed due to invalid permissions or error.)"

                                        await sendEmbedTree(
                                            ctx,
                                            "You have redeemed merch code: "
                                            + code
                                            + " for reward: "
                                            + codeInfo["Reward"] + extraString,
                                            1,
                                        )
                                        print(
                                        ctx.user.name + " has redeemed a merch code: " + code
                                        )
        
                                        decimal = 65280
                                        embed = discord.Embed(
                                            color=decimal,
                                            title="Merch Code System",
                                            description="User " + "<@" + str(ctx.user.id) + ">" + " has redeemed a merch code: " + code + " for reward: " + codeInfo["Reward"],
                                        )
                                        embed.set_footer(
                                            text="Made by Efaz from efaz.dev - v" + version,
                                            icon_url="https://cdn.discordapp.com/attachments/1099414684286861332/1112068066319270019/1W.png",
                                        )
                                        channel = bot.get_channel(botToken["NotificationChannelId"])
                                        await channel.send(embed=embed)
                                    else:
                                        await sendEmbedTree(
                                            ctx,
                                            "Code is already redeemed: " + code,
                                            3,
                                        )
                                else:
                                    userData[str(ctx.user.id)].append(code)
                                    with open("users.json", "w") as outfile:
                                        outfile.write(json.dumps(userData))
                                    
                                    extraString = ""
                                    
                                    if not codes[code]["Role"] == 0:
                                        try:
                                            guild = bot.get_guild(guildId)
                                            role_data = guild.get_role(codes[code]["Role"])
                                            await ctx.user.add_roles(role_data)
                                            extraString = " | Role Added: " + role_data.name
                                        except Exception as e:
                                            extraString = " | Role Added: (failed due to invalid permissions or error.)"

                                    await sendEmbedTree(
                                        ctx,
                                        "You have redeemed perm code: "
                                        + code
                                        + " for reward: "
                                        + codeInfo["Reward"] + extraString,
                                        1,
                                    )
                                    print(
                                        ctx.user.name + " has redeemed a code: " + code
                                    )

                                    decimal = 65480
                                    embed = discord.Embed(
                                        color=decimal,
                                        title="Merch Code System",
                                        description="User " + "<@" + str(ctx.user.id) + ">" + " has redeemed a perm code: " + code + " for reward: " + codeInfo["Reward"],
                                    )
                                    embed.set_footer(
                                        text="Made by Efaz from efaz.dev - v" + version,
                                        icon_url="https://cdn.discordapp.com/attachments/1099414684286861332/1112068066319270019/1W.png",
                                    )
                                    channel = bot.get_channel(botToken["NotificationChannelId"])
                                    await channel.send(embed=embed)
                        else:
                            await sendEmbedTree(ctx, "Code doesn't exist.", 3)
                    else:
                        usersSavedData = []
                        userData[str(ctx.user.id)] = usersSavedData
                        print("User requested to look for code: " + code)
                        if testIfVariableExists(codes, code):
                            codeInfo = codes[code]
                            if testIfVariableExists(usersSavedData, code):
                                await sendEmbedTree(ctx, "User has already used this code.", 3)
                            else:
                                if codeInfo["OneUserOnly"] == True:
                                    if codes[code]["Redeemed"] == False:
                                        userData[str(ctx.user.id)].append(code)
                                        codes[code]["Redeemed"] = True
                                        with open("codes.json", "w") as outfile:
                                            outfile.write(json.dumps(codes))
                                        with open("users.json", "w") as outfile:
                                            outfile.write(json.dumps(userData))

                                        extraString = ""
                                    
                                        if not codes[code]["Role"] == 0:
                                            try:
                                                guild = bot.get_guild(guildId)
                                                role_data = guild.get_role(codes[code]["Role"])
                                                await ctx.user.add_roles(role_data)
                                                extraString = " | Role Added: " + role_data.name
                                            except Exception as e:
                                                extraString = " | Role Added: (failed due to invalid permissions or error.)"

                                        await sendEmbedTree(
                                            ctx,
                                            "You have redeemed merch code: "
                                            + code
                                            + " for reward: "
                                            + codeInfo["Reward"] + extraString,
                                            1,
                                        )
                                        print(
                                            ctx.user.name + " has redeemed a code: " + code
                                        )
        
                                        decimal = 65280
                                        embed = discord.Embed(
                                            color=decimal,
                                            title="Merch Code System",
                                            description="User " + "<@" + str(ctx.user.id) + ">" + " has redeemed a merch code: " + code + " for reward: " + codeInfo["Reward"],
                                        )
                                        embed.set_footer(
                                            text="Made by Efaz from efaz.dev - v" + version,
                                            icon_url="https://cdn.discordapp.com/attachments/1099414684286861332/1112068066319270019/1W.png",
                                        )
                                        channel = bot.get_channel(botToken["NotificationChannelId"])
                                        await channel.send(embed=embed)
                                    else:
                                        await sendEmbedTree(
                                            ctx,
                                            "Code is already redeemed: " + code,
                                            3,
                                        )
                                else:
                                    userData[str(ctx.user.id)].append(code)
                                    with open("users.json", "w") as outfile:
                                        outfile.write(json.dumps(userData))

                                    extraString = ""
                                    
                                    if not codes[code]["Role"] == 0:
                                        try:
                                            guild = bot.get_guild(guildId)
                                            role_data = guild.get_role(codes[code]["Role"])
                                            await ctx.user.add_roles(role_data)
                                            extraString = " | Role Added: " + role_data.name
                                        except Exception as e:
                                            extraString = " | Role Added: (failed due to invalid permissions or error.)"

                                    await sendEmbedTree(
                                        ctx,
                                        "You have redeemed perm code: "
                                        + code
                                        + " for reward: "
                                        + codeInfo["Reward"] + extraString,
                                        1,
                                    )
                                    print(
                                        ctx.user.name + " has redeemed a code: " + code
                                    )

                                    decimal = 65480
                                    embed = discord.Embed(
                                        color=decimal,
                                        title="Merch Code System",
                                        description="User " + "<@" + str(ctx.user.id) + ">" + " has redeemed a perm code: " + code + " for reward: " + codeInfo["Reward"],
                                    )
                                    embed.set_footer(
                                        text="Made by Efaz from efaz.dev - v" + version,
                                        icon_url="https://cdn.discordapp.com/attachments/1099414684286861332/1112068066319270019/1W.png",
                                    )
                                    channel = bot.get_channel(botToken["NotificationChannelId"])
                                    await channel.send(embed=embed)
                        else:
                            await sendEmbedTree(ctx, "Code doesn't exist.", 3)
                else:
                    await sendEmbedTree(ctx, "Code not found in message.", 3)

        @tree.command(
            name="deletecode",
            description="Delete Code from system",
            guild=discord.Object(id=guildId),
        )
        async def deleteCode(ctx, code: str):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbedTree(ctx, "Access Denied", 3)
            else:
                if code:
                    if testIfVariableExists(codes, code):
                        codes.pop(code)
                        with open("codes.json", "w") as outfile:
                            outfile.write(json.dumps(codes))
                        await sendEmbedTree(ctx, "Code has been removed from the system", 2)
                    else:
                        await sendEmbedTree(ctx, "Code not found", 3)
                else:
                    await sendEmbedTree(ctx, "No arg1 found", 3)

        @tree.command(
            name="ping",
            description="Run Ping Test on system",
            guild=discord.Object(id=guildId),
        )
        async def ping(ctx):
            if blacklisted(ctx) == True:
                await sendEmbedTree(ctx, "Access Denied", 3)
                return
            await sendEmbedTree(ctx, f"Pong! {round(bot.latency * 1000)}ms", 2)

        @tree.command(
            name="createmultiplerandomized",
            description="Create multiple randomized codes for the system.",
            guild=discord.Object(id=guildId),
        )
        async def createMultipleRandomized(ctx, prefix: str, reward: str, permornot: bool, count: int, roleid: str="0"):
            if count < 0:
                count = count * -1
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbedTree(ctx, "Access Denied", 3)
            else:
                print("returns True")

                list = []
                message = "New codes: "
                
                for _ in range(count):
                    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
                    args1 = prefix + code
                    if args1:
                        if reward:
                            if testIfVariableExists(codes, args1):
                                await sendEmbedTree(ctx, "Code already exists: " + args1, 2)
                            else:
                                if testIfInt(roleid):
                                    if permornot == True:
                                        codes[args1] = {"Reward": reward, "OneUserOnly": False, "Role": int(roleid)}
                                    else:
                                        codes[args1] = {"Reward": reward, "OneUserOnly": True, "Redeemed": False, "Role": int(roleid)}
                                    with open("codes.json", "w") as outfile:
                                        outfile.write(json.dumps(codes))
                                    list.append(args1)
                                    print("Created code: " + args1)
                                else:
                                    await sendEmbedTree(ctx, "Invalid Role ID: " + roleid, 3)
                        else:
                            print("No reward Inputted in args2, not created")
                    else:
                        print("No Code Inputted in args1, not created")
                for i in list:
                    message = message + "\n `" + i + "` : `" + codes[i]["Reward"] + "` "
                
                await sendEmbedTree(ctx, message, 2)

        @tree.command(
            name="searchuser",
            description="Search user for redeemed codes.",
            guild=discord.Object(id=guildId),
        )
        async def searchUser(ctx, user: discord.Member):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbedTree(ctx, "Access Denied", 3)
            else:
                id = str(user.id)
                if testIfVariableExists(userData, id):
                    message = "User has redeemed codes: "
                    for i in userData[id]:
                        message = message + "\n `" + i + "` "
                    await sendEmbedTree(ctx, message, 2)
                else:
                    await sendEmbedTree(ctx, "This user has no code data or redeemed any codes.", 3)

        @tree.command(
            name="blacklist",
            description="Blacklist an user from using the bot.",
            guild=discord.Object(id=guildId),
        )
        async def blacklist(ctx, user: discord.Member, reason: str):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbedTree(ctx, "Access Denied", 3)
            else:
                id = str(user.id)
                blackListedUsers = botToken["BlacklistedUsers"]
                if testIfVariableExists(blackListedUsers, id):
                    await sendEmbedTree(ctx, "User is already blacklisted from the bot.", 3)
                else:
                    botToken["BlacklistedUsers"][id] = reason
                    with open("bot.json", "w") as outfile:
                        outfile.write(json.dumps(botToken))
                    await sendEmbedTree(ctx, "User has been blacklisted from this bot. Any operations or actions to this bot from this user has been blocked.", 2)

        @tree.command(
            name="blacklistyourself",
            description="Blacklist yourself from the bot (THERE IS NO CONFIRMATION MESSAGE)",
            guild=discord.Object(id=guildId),
        )
        async def blacklistyourself(ctx, reason: str):
            if blacklisted(ctx) == True:
                print("returns False")
                await sendEmbedTree(ctx, "Access Denied", 3)
            else:
                user = ctx.user
                id = str(user.id)
                blackListedUsers = botToken["BlacklistedUsers"]
                if testIfVariableExists(blackListedUsers, id):
                    await sendEmbedTree(ctx, "You're already blacklisted from the bot.", 3)
                else:
                    botToken["BlacklistedUsers"][id] = reason + " (Used Blacklist Yourself Command)"
                    with open("bot.json", "w") as outfile:
                        outfile.write(json.dumps(botToken))
                    await sendEmbedTree(ctx, "You're blacklisted from using the bot. Command operation is finished.", 2)

        @tree.command(
            name="unblacklist",
            description="Unblacklist an user from using the bot.",
            guild=discord.Object(id=guildId),
        )
        async def unBlacklist(ctx, user: discord.Member):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbedTree(ctx, "Access Denied", 3)
            else:
                id = str(user.id)
                blackListedUsers = botToken["BlacklistedUsers"]
                if testIfVariableExists(blackListedUsers, id):
                    botToken["BlacklistedUsers"].pop(id)
                    with open("bot.json", "w") as outfile:
                        outfile.write(json.dumps(botToken))
                    await sendEmbedTree(ctx, "User has been unblacklisted from the bot.", 2)
                else:
                    await sendEmbedTree(ctx, "User is not blacklisted from the bot.", 3)

        @tree.command(
            name="viewblacklistreason",
            description="View Blacklist Reason of an user.",
            guild=discord.Object(id=guildId),
        )
        async def viewBlacklistReason(ctx, user: discord.Member):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                print("returns False")
                await sendEmbedTree(ctx, "Access Denied", 3)
            else:
                id = str(user.id)
                blackListedUsers = botToken["BlacklistedUsers"]
                if testIfVariableExists(blackListedUsers, id):
                    await sendEmbedTree(ctx, f"<@{id}> has been blacklisted for: {botToken['BlacklistedUsers'][id]}", 2)
                else:
                    await sendEmbedTree(ctx, "User is not blacklisted from the bot.", 3)

        @tree.command(
            name="restartbot",
            description="Restart bot.",
            guild=discord.Object(id=guildId),
        )
        async def restartBot(ctx):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                await sendEmbedTree(ctx, "Access Denied", 3)
            else:
                await sendEmbedTree(ctx, "Restarting bot..", 2)
                os.system(sys.executable + " main.py")
                exit()

        @tree.command(
            name="shutdown",
            description="Shutdown bot.",
            guild=discord.Object(id=guildId),
        )
        async def shutdown(ctx):
            if predicate(ctx) == False or blacklisted(ctx) == True:
                await sendEmbedTree(ctx, "Access Denied", 3)
            else:
                await sendEmbedTree(ctx, "Bot is now shutting down. Thanks for using Efaz's Merch Code System, see you next time!", 2)
                print("Bot is shutting down..")
                await bot.change_presence(status=discord.Status.offline)
                printSystemMessage("Bot shut down, returning back to Command Prompt.")
                printSystemMessage("Thanks for using Efaz's Merch Code System, see you next time!")
                await bot.close()
                exit()

        # Economy Commands

        if economy["Enabled"] == True:
            def checkCurrencyAmount(userId):
                if testIfVariableExists(economy["UserData"], str(userId)):
                    return round(economy["UserData"][str(userId)]["Balance"])
                else:
                    return 0
                
            def createCurrency(userId, amount):
                if amount < 0:
                    amount = amount * -1
                if testIfVariableExists(economy["UserData"], str(userId)):
                    economy["UserData"][str(userId)]["Balance"] = round(economy["UserData"][str(userId)]["Balance"] + amount)
                    with open("economy.json", "w") as outfile:
                        outfile.write(json.dumps(economy))
                    return True
                else:
                    economy["UserData"][str(userId)] = {
                        "Balance": 0,
                        "Inventory": [],
                        "LatestDate": 0,
                        "Cooldown": 0,
                    }
                    economy["UserData"][str(userId)]["Balance"] = round(economy["UserData"][str(userId)]["Balance"] + amount)
                    with open("economy.json", "w") as outfile:
                        outfile.write(json.dumps(economy))
                    return True
                
            def takeCurrency(userId, amount):
                if amount < 0:
                    amount = amount * -1
                if checkCurrencyAmount(userId) >= amount:
                    if testIfVariableExists(economy["UserData"], str(userId)):
                        economy["UserData"][str(userId)]["Balance"] = round(economy["UserData"][str(userId)]["Balance"] - amount)
                        with open("economy.json", "w") as outfile: 
                            outfile.write(json.dumps(economy))
                        return True
                    else:
                        return False
                else:
                    return False
                
            def applyRoleMultiplier(user):
                listOfRolesWithMultipliers = economy["RoleMultiplier"]
                highestMultiplier = 1
                for i in listOfRolesWithMultipliers:
                    if bot.get_guild(guildId).get_role(i["roleid"]) in user.roles:
                        if i["multiplier"] > highestMultiplier:
                            highestMultiplier = i["multiplier"]
                return highestMultiplier
                
            def cooldownCommand(userId):
                if testIfVariableExists(economy["UserData"], str(userId)):
                    if economy["UserData"][str(userId)]["Cooldown"] > datetime.now().timestamp():
                        return True
                    else:
                        return False
                else:
                    economy["UserData"][str(userId)] = {
                            "Balance": 0,
                            "Inventory": [],
                            "LatestDate": 0,
                            "Cooldown": 0,
                    }
                    return False
                    
            def setCooldown(userId):
                if userId in botToken["Admins"]:
                    return
                economy["UserData"][str(userId)]["Cooldown"] = datetime.now().timestamp() + 120
                with open("economy.json", "w") as outfile:
                    outfile.write(json.dumps(economy))
            @tree.command(
                name="flipcoin",
                description="Flip a coin. (2x winning)",
                guild=discord.Object(id=guildId),
            )
            async def flipCoin(ctx, amount: int, guess: str):
                if cooldownCommand(ctx.user.id):
                    await sendEmbedTree(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                else:
                    setCooldown(ctx.user.id)
                if amount < 0:
                    amount = amount * -1
                if blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    if guess == "Tails" or guess == "Heads":
                        if takeCurrency(ctx.user.id, amount):
                            randomized = random.randint(1, 2)
                            if randomized == 1:
                                await sendEmbedTree(ctx, "🪙 Heads!", 2)
                                if guess == "Heads":
                                    createCurrency(ctx.user.id, amount * 2 * applyRoleMultiplier(ctx.user))
                            else:
                                await sendEmbedTree(ctx, "🪙 Tails!", 2)
                                if guess == "Tails":
                                    createCurrency(ctx.user.id, amount * 2 * applyRoleMultiplier(ctx.user))
                        else:
                            await sendEmbedTree(ctx, "Failed to take money: Insufficent Balance", 3)
                    else:
                        await sendEmbedTree(ctx, "Failed, guess must be either `Heads` or `Tails`", 3)

            @tree.command(
                name="gamble",
                description="Gamble for a chance of max!",
                guild=discord.Object(id=guildId),
            )
            async def gamble(ctx, estimate: int, max: int, amount: int):
                if cooldownCommand(ctx.user.id):
                    await sendEmbedTree(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                else:
                    setCooldown(ctx.user.id)
                if amount < 0:
                    amount = amount * -1
                if max < 0:
                    max = max * -1
                if estimate < 0:
                    estimate = estimate * -1
                if blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    if takeCurrency(ctx.user.id, amount):
                        randomized = random.randint(1, max)
                        if randomized == estimate:
                            await sendEmbedTree(ctx, "Success! You got it! Chances: " + str(round(1 / max * 100)) + "%", 2)
                            createCurrency(ctx.user.id, amount * max * applyRoleMultiplier(ctx.user))
                        else:
                            await sendEmbedTree(ctx, "Failed! R.I.P. Chances: " + str(round(1 / max * 100)) + "%", 2)
                    else:
                        await sendEmbedTree(ctx, "Failed to take money: Insufficent Balance", 3)

            @tree.command(
                name="createcurrency",
                description="Create currency",
                guild=discord.Object(id=guildId),
            )
            async def createcurrency(ctx, user: discord.Member, amount: int):
                if cooldownCommand(ctx.user.id):
                    await sendEmbedTree(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                else:
                    setCooldown(ctx.user.id)
                if amount < 0:
                    amount = amount * -1
                if predicate(ctx) == False or blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    if not testIfVariableExists(economy["UserData"], str(ctx.user.id)):
                        economy["UserData"][str(ctx.user.id)] = {
                            "Balance": 0,
                            "Inventory": [],
                            "LatestDate": 0,
                            "Cooldown": 0,
                        }
                    response = createCurrency(user.id, amount)
                    if response == True:
                        await sendEmbedTree(ctx, "Gave " + str(amount) + " currency to " + user.name + "!", 2)
                    else:
                        await sendEmbedTree(ctx, "Failed! Issue while giving user money.", 2)
            
            @tree.command(
                name="takecurrency",
                description="Take currency",
                guild=discord.Object(id=guildId),
            )
            async def removecurrency(ctx, user: discord.Member, amount: int):
                if cooldownCommand(ctx.user.id):
                    await sendEmbedTree(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                else:
                    setCooldown(ctx.user.id)
                if amount < 0:
                    amount = amount * -1
                if predicate(ctx) == False or blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    if not testIfVariableExists(economy["UserData"], str(ctx.user.id)):
                        economy["UserData"][str(ctx.user.id)] = {
                            "Balance": 0,
                            "Inventory": [],
                            "LatestDate": 0,
                            "Cooldown": 0,
                        }
                    response = takeCurrency(user.id, amount)
                    if response == True:
                        await sendEmbedTree(ctx, "Removed " + str(amount) + " currency from " + user.name + "!", 2)
                    else:
                        await sendEmbedTree(ctx, "Failed to take money: Insufficent Balance", 3)

            @tree.command(
                name="balance",
                description="Check balance!",
                guild=discord.Object(id=guildId),
            )
            async def balance(ctx, user: discord.Member):
                if blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    response = checkCurrencyAmount(user.id)
                    await sendEmbedTree(ctx, user.name + "'s Balance: \n" + str(response) + " " + economy["EconomyName"], 2)

            @tree.command(
                name="daily",
                description="Get daily balance",
                guild=discord.Object(id=guildId),
            )
            async def daily(ctx):
                if cooldownCommand(ctx.user.id):
                    await sendEmbedTree(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                if blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    if not testIfVariableExists(economy["UserData"], str(ctx.user.id)):
                        economy["UserData"][str(ctx.user.id)] = {
                            "Balance": 0,
                            "Inventory": [],
                            "LatestDate": 0,
                            "Cooldown": 0,
                        }
                    if economy["UserData"][str(ctx.user.id)]["LatestDate"] <= datetime.now().timestamp():
                        economy["UserData"][str(ctx.user.id)]["LatestDate"] = datetime.now().timestamp() + 86400
                        response = createCurrency(ctx.user.id, economy["Commands"]["Daily"] * applyRoleMultiplier(ctx.user))
                        if response == True:
                            await sendEmbedTree(ctx, "You've received " + str(economy["Commands"]["Daily"] * applyRoleMultiplier(ctx.user)) + " " + economy["EconomyName"] + "! Come back in 24 hours!", 2)
                    else:
                        await sendEmbedTree(ctx, "Time is still remaining. Please wait!", 3)

            @tree.command(
                name="buy",
                description="Buy from the store!",
                guild=discord.Object(id=guildId),
            )
            async def buy(ctx, itemname: str):
                if cooldownCommand(ctx.user.id):
                    await sendEmbedTree(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                if blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    if testIfVariableExists(StoreItems, itemname):
                        item = StoreItems[itemname]
                        if item["stock"] > 0:
                            if len(economy["UserData"][str(ctx.user.id)]["Inventory"]) + 1 > economy["InventoryLimit"]:
                                await sendEmbedTree(ctx, "Failed to buy item: No storage left, use an item in your inventory and try again!", 3)
                                return
                            if takeCurrency(ctx.user.id, item["price"]):
                                if not item["role"] == 0:
                                    if not bot.get_guild(guildId).get_role(item["role"]) in ctx.user.roles:
                                        await ctx.user.add_roles(bot.get_guild(guildId).get_role(item["role"]))
                                economy["StoreInventory"][itemname]["stock"] = economy["StoreInventory"][itemname]["stock"] - 1
                                economy["UserData"][str(ctx.user.id)]["Inventory"].append(itemname)
                                with open("economy.json", "w") as outfile:
                                    outfile.write(json.dumps(economy))
                                await sendEmbedTree(ctx, "Bought: " + itemname + "!", 2)
                            else:
                                await sendEmbedTree(ctx, "Failed to take money: Insufficent Balance", 3)
                        else:
                            await sendEmbedTree(ctx, "Failed to buy item: No stock for item is left.", 3)
                    else:
                        await sendEmbedTree(ctx, "Item is not found.", 3)
                        
            @tree.command(
                name="inventory",
                description="View inventory you bought from the store!",
                guild=discord.Object(id=guildId),
            )
            async def inventory(ctx):
                if cooldownCommand(ctx.user.id):
                    await sendEmbedTree(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                if blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    if not testIfVariableExists(economy["UserData"], str(ctx.user.id)):
                        await sendEmbedTree(ctx, "No inventory found", 3)
                        return
                    userInventory = economy["UserData"][str(ctx.user.id)]["Inventory"]
                    message = "User's inventory: \n"
                    for i in userInventory:
                        message = message + "`" + i + "` \n"
                    await sendEmbedTree(ctx, message, 2)

            @tree.command(
                name="use",
                description="Use item from your inventory",
                guild=discord.Object(id=guildId),
            )
            async def use(ctx, item: str):
                if cooldownCommand(ctx.user.id):
                    await sendEmbedTree(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                if blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    if not testIfVariableExists(economy["UserData"], str(ctx.user.id)):
                        await sendEmbedTree(ctx, "No inventory found", 3)
                        return
                    userInventory = economy["UserData"][str(ctx.user.id)]["Inventory"]
                    itemFromInventory = ""
                    for i in userInventory:
                        if i == item:
                            itemFromInventory = item
                    
                    if itemFromInventory == "":
                        await sendEmbedTree(ctx, "Item is not found in your inventory", 3)
                    else:
                        itemLookUp = StoreItems[itemFromInventory]
                        if not itemLookUp["role"] == 0:
                            if bot.get_guild(guildId).get_role(itemLookUp["role"]) in ctx.user.roles:
                                print("User already has role, ignored.")
                            else:
                                await ctx.user.add_roles(bot.get_guild(guildId).get_role(itemLookUp["role"]))
                        economy["UserData"][str(ctx.user.id)]["Inventory"].remove(itemFromInventory)
                        with open("economy.json", "w") as outfile:
                            outfile.write(json.dumps(economy))

                        decimal = 65280
                        embed = discord.Embed(
                            color=decimal,
                            title="Merch Code System",
                            description="User " + "<@" + str(ctx.user.id) + ">" + " has redeemed a item: " + itemFromInventory,
                        )
                        embed.set_footer(
                            text="Made by Efaz from efaz.dev - v" + version,
                            icon_url="https://cdn.discordapp.com/attachments/1099414684286861332/1112068066319270019/1W.png",
                        )
                        channel = bot.get_channel(botToken["NotificationChannelId"])
                        await channel.send(embed=embed)

                        await sendEmbedTree(ctx, "Item used!", 2)

            @tree.command(
                name="createitem",
                description="Create an item in the store.",
                guild=discord.Object(id=guildId),
            )
            async def createItem(ctx, item: str, stock: int, price: int, roleid: str="0"):
                if price < 0:
                    price = price * -1
                if stock < 0:
                    stock = stock * -1

                roleId = int(roleid)
                if not roleId:
                    roleId =  0

                if roleId < 0:
                    roleId = roleId * -1
                if predicate(ctx) == False or blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    if not roleId == 0: 
                        economy["StoreInventory"][item] = {
                            "stock": stock,
                            "price": price,
                            "name": item,
                            "role": roleId
                        }
                    else:
                        economy["StoreInventory"][item] = {
                            "stock": stock,
                            "price": price,
                            "name": item,
                            "role": 0
                        }
                    with open("economy.json", "w") as outfile:
                        outfile.write(json.dumps(economy))
                    await sendEmbedTree(ctx, "Created item!", 2)

            @tree.command(
                name="enditemlisting",
                description="End item listing from the store",
                guild=discord.Object(id=guildId),
            )
            async def endItemListing(ctx, item: str):
                if predicate(ctx) == False or blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    if testIfVariableExists(economy["StoreInventory"], item): 
                        if economy["StoreInventory"][item]["stock"] == 0:
                            await sendEmbedTree(ctx, "Failed to end item: Item is already ended stock", 3)
                            return
                        economy["StoreInventory"][item]["stock"] = 0
                        await sendEmbedTree(ctx, "Item's stock is finished!", 2)
                    else:
                        await sendEmbedTree(ctx, "Failed to end item: Item is not found", 3)

            @tree.command(
                name="viewstorestock",
                description="View Current stock inside the store.",
                guild=discord.Object(id=guildId),
            )
            async def viewstorestock(ctx):
                if cooldownCommand(ctx.user.id):
                    await sendEmbedTree(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                if blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    message = "Store Inventory: \n"
                    instock = "** In Stock ** \n"
                    outstock = "** Out of Stock ** \n"
                    for i in economy["StoreInventory"].keys():
                        item = economy["StoreInventory"][i]
                        if item["stock"] > 0:
                            instock = instock + "`" + item["name"] + "` | Price: `" + str(item["price"]) + "` | Stock: `" + str(item["stock"]) + "` \n"
                        else:
                            outstock = outstock + "`" + item["name"] + "` | Price: `" + str(item["price"]) + "` \n"

                    if instock == "** In Stock ** \n":
                        instock = "** In Stock ** \n No items available \n"
                    if outstock == "** Out of Stock ** \n":
                        outstock = "** Out of Stock ** \n No items out of stock \n"
                    await sendEmbedTree(ctx, message + instock + outstock, 2)      

            @tree.command(
                name="rob",
                description="Rob an user for chance of money!",
                guild=discord.Object(id=guildId),
            )
            async def rob(ctx, user: discord.Member):
                if cooldownCommand(ctx.user.id):
                    await sendEmbedTree(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                else:
                    setCooldown(ctx.user.id)
                if blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    if user.id in botToken["Admins"]:
                        await sendEmbedTree(ctx, "Failed! You can't rob the admins of this bot!", 3)
                        return
                    randomized = random.randint(1, economy["SuccessRate"])
                    if checkCurrencyAmount(ctx.user.id) >= 1:
                        if randomized == 1:
                            amount = checkCurrencyAmount(user.id) * 0.5
                            response = takeCurrency(user.id, amount)
                            response2 = createCurrency(ctx.user.id, amount)
                            await sendEmbedTree(ctx, "Robbing Success! You have earned " + str(amount) + " " + economy["EconomyName"] + "!", 2)
                        else:
                            amount = checkCurrencyAmount(ctx.user.id) * 0.5
                            response = takeCurrency(ctx.user.id, amount)
                            await sendEmbedTree(ctx, "Robbing Failed! You have been charged " + str(amount) + " " + economy["EconomyName"] + "!", 3)
                    else:
                        await sendEmbedTree(ctx, "Robbing Failed! You have no money to use for this command!", 3)

            @tree.command(
                name="sendmoney",
                description="Send money to an user!",
                guild=discord.Object(id=guildId),
            )
            async def sendMoney(ctx, user: discord.Member, amount: int):
                if cooldownCommand(ctx.user.id):
                    await sendEmbedTree(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                else:
                    setCooldown(ctx.user.id)
                if amount < 0:
                    amount = amount * -1
                if blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    if checkCurrencyAmount(ctx.user.id) >= amount:
                        response = takeCurrency(ctx.user.id, amount)
                        response2 = createCurrency(user.id, amount)
                        await sendEmbedTree(ctx, "You have gave " + str(amount) + " " + economy["EconomyName"] + " to " + user.name + "!", 2)
                    else:
                        await sendEmbedTree(ctx, "Not enough funds!", 3)  

            @tree.command(
                name="work",
                description="Work for money!",
                guild=discord.Object(id=guildId),
            )
            async def work(ctx):
                if cooldownCommand(ctx.user.id):
                    await sendEmbedTree(ctx, "Access Denied: Still on 2 minute cooldown, try again later!", 3)
                    return
                else:
                    setCooldown(ctx.user.id)
                if blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    jobList = economy["JobList"]
                    randomizedJob = jobList[random.randint(0, len(jobList) - 1)]
                    response = createCurrency(ctx.user.id, randomizedJob["amount"] * applyRoleMultiplier(ctx.user))
                    await sendEmbedTree(ctx, "You have earned " + str(randomizedJob["amount"] * applyRoleMultiplier(ctx.user)) + " from working as a " + randomizedJob["name"] + "!", 2)

            @tree.command(
                name="about",
                description="View information about the bot!",
                guild=discord.Object(id=guildId),
            )
            async def about(ctx):
                if blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    main_about_string = f"**Made by Efaz at [efaz.dev](https://www.efaz.dev)** \nScript Version: `v{version}` \nSystem OS: `{platform.system()}` "
                    main_about_string = main_about_string + "\n Admins: "
                    for admin in botToken["Admins"]:
                        main_about_string = main_about_string + "<@" + str(admin) + "> "

                    if economy['Enabled'] == True:
                        main_about_string = main_about_string + f"\n\n**Economy** \nEnabled: `{str(economy['Enabled'])}` \nCurrency Name: `{economy['EconomyName']}` "
                        if economy["GreatReset"]["Enabled"] == True:
                            main_about_string = main_about_string + f"\nGreat Resets Enabled: `{str(economy['GreatReset']['Enabled'])}` \nSeason Number: `{str(economy['GreatReset']['SeasonNumber'])}` "
                        else:
                            main_about_string = main_about_string + f"\nGreat Resets Enabled: `{str(economy['GreatReset']['Enabled'])}` "
                    else:
                        main_about_string = main_about_string + f"\n\n**Economy** \nEnabled: `{str(economy['Enabled'])}` "

                    await sendEmbedTree(ctx, main_about_string, 2)

            @tree.command(
                name="cooldowncheck",
                description="Check your cooldown",
                guild=discord.Object(id=guildId),
            )
            async def cooldownCheck(ctx):
                if blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    await sendEmbedTree(ctx, "Cooldown ends <t:" + str(round(economy["UserData"][str(ctx.user.id)]["Cooldown"])) + ":R>", 2)
            @tree.command(
                name="top10lb",
                description="Check the top 10 leaderboard on cash!",
                guild=discord.Object(id=guildId),
            )
            async def topleaderboard(ctx):
                if blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    lbList = economy["UserData"]
                    lbList = dict(sorted(lbList.items(), reverse=True, key=lambda x:x[1]["Balance"]))

                    message = "Top **10** Leaderboard! \n ** " + economy["EconomyName"] + " ** \n"

                    if len(lbList) < 10:
                        keys = lbList.keys()
                        for i in keys:
                            message = message + "<@" + str(i) + "> | " + str(economy["UserData"][i]["Balance"]) + " \n"
                    else:
                        keys = list(lbList.keys())
                        for i in range(10):
                            message = message + "<@" + str(keys[i]) + "> | " + str(economy["UserData"][keys[i]]["Balance"]) + " \n"

                    message = message + " ** Number of Items ** \n"
                    lbList = dict(sorted(lbList.items(), reverse=True, key=lambda x:len(x[1]["Inventory"])))

                    if len(lbList) < 10:
                        keys = lbList.keys()
                        for i in keys:
                            message = message + "<@" + str(i) + "> | " + str(len(economy["UserData"][i]["Inventory"])) + " \n"
                    else:
                        keys = list(lbList.keys())
                        for i in range(10):
                            message = message + "<@" + str(keys[i]) + "> | " + str(len(economy["UserData"][keys[i]]["Inventory"])) + " \n"

                    await sendEmbedTree(ctx, message, 2)
            @tree.command(
                name="multipliercheck",
                description="Check your Multiplier",
                guild=discord.Object(id=guildId),
            )
            async def multiplierCheck(ctx):
                if blacklisted(ctx) == True:
                    await sendEmbedTree(ctx, "Access Denied", 3)
                else:
                    await sendEmbedTree(ctx, "Multiplier applied on non-user involved commands: " + str(applyRoleMultiplier(ctx.user)) + "x Multiplier", 2)

            if economy["GreatReset"]["Enabled"] == True:
                greatResetCurrently = False
                def checkIfCashKing(user):
                    try:
                        if bot.get_guild(guildId).get_role(economy["GreatReset"]["CashKingRoleID"]) in user.roles:
                            return True
                        else:
                            return False
                    except Exception:
                        return False
                
                @tree.command(
                    name="greatreset",
                    description="Do the Great Reset! ONLY THE CASH KING CAN DO. Resets data of all users.",
                    guild=discord.Object(id=guildId),
                )
                async def greatReset(ctx: discord.Interaction, confirm: bool):
                    if checkIfCashKing(ctx.user) == False or blacklisted(ctx) == True:
                        await sendEmbedTree(ctx, "Access Denied", 3)
                    else:
                        if confirm == True:
                            global greatResetCurrently
                            if greatResetCurrently == False:
                                guild = bot.get_guild(guildId)
                                greatResetCurrently = True
                                await sendEmbedTree(ctx, "Launched a new Great Reset wave! A new message will appear when the process is finished!", 2)
                                # Remove Roles
                                if economy["GreatReset"]["DataToReset"]["Roles"] == True:
                                    for roleId in economy["GreatReset"]["RolesToReset"]:
                                        role = guild.get_role(roleId)
                                        print(f"Received Role: {role.name}, {role.id}")
                                        for member in role.members:
                                            try:
                                                await member.remove_roles(role)
                                                print("Removed role: " + role.name + " from: " + str(member.id))
                                            except Exception as e:
                                                print("Error while removing role: " + str(e))

                                # Restock Items
                                if economy["GreatReset"]["DataToReset"]["Items"] == True:
                                    for item in economy["GreatReset"]["ItemDataWhenRestock"]:
                                        economy["StoreInventory"][item["name"]] = item

                                        global StoreItems
                                        StoreItems = economy["StoreInventory"]

                                        # Delete Everyone's inventory
                                        for userData in economy["UserData"].keys():
                                            for itemInInv in economy["UserData"][userData]["Inventory"]:
                                                if itemInInv == item["name"]:
                                                    economy["UserData"][userData]["Inventory"].remove(item["name"])

                                # Reset Cash
                                if economy["GreatReset"]["DataToReset"]["Cash"] == True:
                                    for userData in economy["UserData"].keys():
                                        economy["UserData"][userData]["Balance"] = 0
                                        economy["UserData"][userData]["LatestDate"] = 0
                                        economy["UserData"][userData]["Cooldown"] = 0
                                        print("Reset Data of: " + userData)

                                # New Season
                                if economy["GreatReset"]["SeasonNumber"] < 1:
                                    economy["GreatReset"]["SeasonNumber"] = 1
                                economy["GreatReset"]["SeasonNumber"] = economy["GreatReset"]["SeasonNumber"] + 1

                                # SAVE DATA

                                with open("economy.json", "w") as outfile:
                                    outfile.write(json.dumps(economy))
                                print("Saved Data")
                                decimal = 65280
                                embed = discord.Embed(
                                    color=decimal,
                                    title="Merch Code System",
                                    description="Season " + str(economy["GreatReset"]["SeasonNumber"] - 1) + " is finished! Bot has reset what the owner has set to reset! <@" + str(ctx.user.id) + ">'s Cash King role has been removed! Welcome to Season " + str(economy["GreatReset"]["SeasonNumber"]) + "!",
                                )
                                embed.set_footer(
                                    text="Made by Efaz from efaz.dev",
                                    icon_url="https://cdn.discordapp.com/attachments/1099414684286861332/1112068066319270019/1W.png",
                                )
                                channel = bot.get_channel(botToken["NotificationChannelId"])
                                await channel.send(embed=embed)
                                await ctx.channel.send(embed=embed)
                                print("Finished Great Reset")
                                greatResetCurrently = False
                            else:
                                await sendEmbedTree(ctx, "An another great reset is happening. Please wait.", 3)
                        else:
                            await sendEmbedTree(ctx, "Cash King declined confirmation", 3)

        else:
            print("Economy Commands have not been applied to the bot, switch Enabled variable to True to enable economy commands.")

        print("Loaded, logging into bot...")
        bot.run(botToken["Token"])
else:
    printSystemMessage("System doesn't support module mode. Sorry!")
# End of script
# Made by Efaz at efaz.dev