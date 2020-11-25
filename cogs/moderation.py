import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions

class Moderation(commands.Cog):
    """ Moderation commands for discord """

    def __init__(self, bot):
        self.bot = bot


    @commands.command(help='Kicks people from the server')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send('Kicked {} for {}'.format(member, reason))
        print(' [INFO] Kicked {} for {}')



    @commands.command(help='Bans members from a server')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send('Banned {} for {}'.format(member, reason))
        print(' [INFO] Banned {} for {}'.format(member, reason))

    @commands.command(help="Gives Help")
    async def help(self, ctx):
        embed = discord.Embed(title="Help", description="Please use .help <cattegory> for help in a certain category", color=0x0669a0)
        embed.add_field(name="Music Commands", value="Commands for voice chat", inline=True)
        embed.add_field(name="Filtering Commands", value="Filtering the chats", inline=True)
        embed.add_field(name="Misc. Commands", value="Just some miscelanous commands", inline=True)
        embed.add_field(name="Moderation Commands", value="All commands for moderation purpose", inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))
