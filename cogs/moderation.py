import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions

import wordfilter


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

     @commands.command(pass_context=True, name='kick', help='Kicks a certain user')
     @has_permissions(manage_roles=True, ban_members=True)
     async def kick(self, ctx, member : discord.Member, *, reason = None):
         dm = await member.create_dm()
         await member.kick(reason=reason)
         await bot.send_message(user, message)

    @commands.command(pass_context=True, name='clear', help='Clears a certain amount of messages in a channel')
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit = amount + 1)



def setup(bot):
    bot.add_cog(Moderation(bot))
