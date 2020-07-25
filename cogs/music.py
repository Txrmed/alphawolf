from discord.ext import commands
from discord.utils import get
import discord

from youtube_search import YoutubeSearch

class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, help='Drops some sick beat')
    async def play(self, ctx, *,  phrase):
        a = YoutubeSearch(phrase, max_results=10).to_dict()
        print(a)


def setup(bot):
    bot.add_cog(Music(bot))
