import discord
from discord.ext import commands
from discord.utils import get
import json
import random

class LevelingSystem(commands.Cog):
    """ Leveling system for discord """

    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def get_data():
        with open('members.json', 'r') as file:
            return loads(file.read())

    @staticmethod
    def set_data(members):
        with open('members.json', 'w') as file:
            file.write(dumps(members, indent=2))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        members = self.get_data()
        members.append({'name': member.name, 'id': member.id, 'level': 0,'xp': 0})
        self.set_data(members)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        members = self.get_data()
        members.remove({'name': member.name, 'id': member.id, 'level': member.level,'xp': member.xp})
        self.set_data(members)

    @commands.Cog.listener()
    async def on_message(self, message):
        author = message.author.id
        members = self.get_data()
        for member in members:
            if author == member['id']:
                member['xp'] += randint(5, 10)
            if member['xp'] > self.base_xp * (member['level']+1 * self.factor):
                member['level'] += 1
                await message.channel.send(f":partying_face: {message.author.mention} you have reached level {member['level']}")
        self.set_data(members)


def setup(bot):
    bot.add_cog(LevelingSystem(bot))
