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

    # @commands.Cog.listener()
    # async def on_message(self, ctx, message, member):
    #     return

    # try:
    #     c.execute("""CREATE TABLE levels (
    #         memberID integer,
    #         level integer,
    #         experience integer
    #         ) """)
    # except:
    #     print(" Table is already made")
    #
    # c.execute("INSERT INTO levels VALUES (69, 4, 73)")
    # c.execute("INSERT INTO levels VALUES (765, 35, 232)")
    #
    # c.execute("SELECT * FROM levels WHERE memberID = 69")
    #
    # print(c.fetchall())
    #
    #
    # connection.commit()
    # connection.close()


def setup(bot):
    bot.add_cog(LevelingSystem(bot))
