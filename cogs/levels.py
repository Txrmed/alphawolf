import discord
from discord.ext import commands
from discord.utils import get
import json
import random

class LevelingSystem(commands.Cog):
    """ Leveling system for discord
    In progress
    Sorry
                - Termed
    """


def setup(bot):
    bot.add_cog(LevelingSystem(bot))
