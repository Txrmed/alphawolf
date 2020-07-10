import discord
import os
from discord.ext import commands
from discord.utils import get
import asyncio

class onMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(ctx, message):
        if "XD" or "XDD" or "XDDD" or "XDDDD" or "XDDDD" in message.content:
            pass
        else:
            message_content = message.content
            if message_content.isupper():
                if message.author.id == '704646393473663019':
                    await message.channel.send('{} TOBIE BARTOSZ NIE ODPOWIEM BO MENDA I DZIAD JESTEŚ'.format(message.author.mention))
                message_author = message.author
                await message.channel.send('{} , Please refrain from using too many capital letters.'.format(message.author.mention))
                print(' Warned {} for too many capital letters'.format(message_author))

def setup(bot):
    bot.add_cog(onMessage(bot))
