import discord
from discord.ext import commands
from discord.utils import get

import random

class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, name='github', help='Gives the url to github')
    async def github(self, ctx):
        await ctx.send('Heres where the magic happens :' + ' https://github.com/Termed/alphawolf')

def setup(bot):
    bot.add_cog(Commands(bot))
