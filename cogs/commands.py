import discord
from discord.ext import commands
from discord.utils import get

import random
import praw

class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, name='github', help='Gives the url to github')
    async def github(self, ctx):
        await ctx.send('Heres where the magic happens :' + ' https://github.com/Termed/alphawolf')

    @commands.command(pass_context=True, name='meme', help='Throws memes at you')
    async def meme(self, ctx):
        r = praw.Reddit('bot1')

        initialized = False
        if initialized != True:
            initialized = True
            posts = []
            for post in r.subreddit('memes').new():
                posts.append(post.url)
            for post in r.subreddit('dankmemes').new():
                posts.append(post.url)
            for post in r.subreddit('PewdiepieSubmissions').new():
                posts.append(post.url)

        meme = posts[random.randint(0, len(posts) - 1)]
        print(" [INFO] Sent meme : {}".format(meme))
        await ctx.send(meme)

def setup(bot):
    bot.add_cog(Commands(bot))
