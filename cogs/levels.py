import discord
from discord.ext import commands
from discord.utils import get

import sqlite3

class LevelingSystem(commands.Cog):
    """
    Leveling System for Discord using MySQL
    """

    connection = sqlite3.connect('levels.db')
    c = connection.cursor()

    try:
        c.execute("""CREATE TABLE levels (
            memberID integer,
            level integer,
            experience integer
            ) """)
    except:
        print(" Table is already made")

    c.xe

    connection.commit()
    connection.close()


def setup(bot):
    bot.add_cog(LevelingSystem(bot))
