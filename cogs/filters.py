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
            await message.channel.send('{} , Please refrain from using too many capital letters.'.format(message.author.mention))


def setup(bot):
    bot.add_cog(onMessage(bot))
