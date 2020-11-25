import discord
from discord.ext import commands
from discord.utils import get

import random
import praw

import time

memes = []

index = range(1, 101)
if index[random.randint(0, len(index))] == 69:
    memes = []
    print(' [INFO] Refreshed memes array : {}'.format(str(memes)))

class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True, name='github', help='Gives the url to github')
    async def github(self, ctx):
        await ctx.send('Heres where the magic happens :' + ' https://github.com/Termed/alphawolf')

    @commands.command(pass_context=True, name='meme', help='Throws memes at you')
    async def meme(self, ctx):
        r = praw.Reddit('bot1')
        meme = None

        if len(memes) == 0:
            for post in r.subreddit('memes').hot():
                url = post.url
                memes.append(url)
        else:
            meme = memes[random.randint(0, len(memes))]

        if meme == None:
            meme = memes[random.randint(0, len(memes))]
        print(" [INFO] Sent meme : {}".format(meme))
        await ctx.send(meme)

    @commands.command(pass_context=True, name='alphawolf', help='me?')
    async def alphawolf(self, ctx):
        await ctx.send('Did anyone call me?')

    @commands.command(name='create_channels', help='Creates channels with member count')
    async def create_channels(self, ctx, members):
        members = len([m for m in ctx.guild.members if not m.bot])
        guild = ctx.message.guild

        await guild.create_text_channel('Members : {}'.format(members))

    @commands.command(name='change_status', help="Changes discord bot status", pass_context=True)
    async def change_status(self, ctx, value, *, status=None):
        if status == None:
            await ctx.send(" Status cannot be None. Please specify a status")

        if value.lower() == "streaming":
            await self.bot.change_presence(activity=discord.Activity(type=discord.streaming, name=status))
        elif value.lower() == "listening":
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))
        elif value.lower() == "playing":
            await self.bot.change_presence(activity=discord.Activity(type=discord.Game , name=status))
        elif value.lower() == "watching":
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        else:
            return await ctx.send(" There is no such activity as {}".format(value))

    @commands.command(name="clear", help="Clears x amount of messages", pass_context=True)
    async def clear(self, ctx, amount: int):

        if amount > 100:
            await ctx.send("Cannot delete over 100 messages.")
        
        await ctx.channel.purge(limit=amount)
        print(" [INFO] Deleted {} of messages in channel: {}".format(amount, ctx.channel))


def setup(bot):
    bot.add_cog(Commands(bot))
