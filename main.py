import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

import os
import os.path

load_dotenv()
token = os.getenv("TOKEN")  
prefix = os.getenv("PREFIX")

bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="over my servers"))

    with open("ascii.txt", "r") as f:
        print(f.read())

    print(' ----------')
    num = 0
    for file in os.listdir("./cogs"):
        if file.endswith('.py'):
            num += 1

    loaded = 0
    for file in os.listdir('./cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            loaded += 1
            bot.load_extension(f'cogs.{file[:-3]}')
            print(' [INFO] Loaded {} : {}/{}'.format(file, loaded, num))

    if os.isfile("cogs/data.dat"):
        pass
    else:
        os.mkdir("cogs/data.dat")

bot.run(token)
