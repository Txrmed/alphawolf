import discord
from discord.ext import commands
from discord.utils import get
import os
from dotenv import load_dotenv
import random
import config

load_dotenv('.env')
token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix=config.COMMAND_PREFIX)

@bot.event
async def on_ready():

    with open("ascii.txt", "r") as f:
        print(f.read())

    print(' ----------')
    for file in os.listdir('./cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            bot.load_extension(f'cogs.{file[:-3]}')
            print(' Loaded {}'.format(file))


bot.run(token)
