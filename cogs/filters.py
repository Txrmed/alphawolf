import discord
import os
from discord.ext import commands
from discord.utils import get

class onMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        message_content = message.content
        if message_content.isupper():
            embed = discord.Embed(title="Warning", description="{}, Please refrain from using too many capital letters".format(message.author.mention))
            await message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(onMessage(bot))
