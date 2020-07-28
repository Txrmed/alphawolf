import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions

from threading import Timer


class Moderation(commands.Cog):
    """ Moderation commands for discord """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send('Wyrzucono {} za {}'.format(member, reason))
        print(' [INFO] Kicked {} for {}')


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send('Banned {} za {}'.format(member, reason))
        print(' [INFO] Banned {} for {}'.format(member, reason))


def setup(bot):
    bot.add_cog(Moderation(bot))
