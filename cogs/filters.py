import discord
import os
from discord.ext import commands
from discord.utils import get
import asyncio

class onMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def check_for_capitals(self, ctx, message):
        message_content = message.content
        if message_content.isupper():
            message_author = message.author
            await message.channel.send('{} , Please refrain from using too many capital letters.'.format(message.author.mention))
            print(' Warned {} for too many capital letters'.format(message_author))


def setup(bot):
    bot.add_cog(onMessage(bot))
