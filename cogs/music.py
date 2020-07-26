from discord.ext import commands
from discord.utils import get
import discord

from youtubesearchpython import SearchVideos
import os
import Lavalink


class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, help='Drops some sick beat')
    async def play(self, ctx, *,  phrase):
        search = SearchVideos(phrase, offset=1, mode="dict", max_results=1)
        searchResults = search.result()

        try:
            url = searchResults["search_result"][0]["link"]
            title = searchResults["search_result"][0]["title"]
            duration = searchResults["search_result"][0]["duration"]
            yt_channel = searchResults["search_result"][0]["channel"]
        except IndexError:
            await ctx.send("AlphaWolf nie znajdzie czegoś co ma za dużo słów więc postaraj się ujać tytuł w kilku słowach")

        author_vc= ctx.author.voice
        channel = ctx.author.voice.channel
        if author_vc:
            await author_vc.channel.connect()
            print(" Connected to vc : {}".format(, author_vc.channel))



def setup(bot):
    bot.add_cog(Music(bot))
