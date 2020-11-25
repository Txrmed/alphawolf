import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

import os
import os.path


token = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")

bot = commands.Bot(command_prefix=".")

bot.remove_command('help')

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

    open("cogs/vdata.alphawolf", "w").close()


bot.run("NzE0ODM0MDE3OTk1ODQ5ODIw.Xs0bDg.2WogELa_waOiEqew3p3x4KFaY8k")
