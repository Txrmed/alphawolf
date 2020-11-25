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
    async def help(self, ctx, *, category=None):
        if category == None:
            embed = discord.Embed(title="Help", description="Please use .help <cattegory> for help in a certain category", color=0x0669a0)
            embed.add_field(name="Music Commands", value=".help music", inline=True)
            embed.add_field(name="Filtering Commands", value=".help filtering", inline=True)
            embed.add_field(name="Misc. Commands", value=".help misc", inline=True)
            embed.add_field(name="Moderation Commands", value=".help moderation", inline=True)
            await ctx.send(embed=embed)
        elif category == "music":
            m_embed = discord.Embed(title="Music commands", description="All the music commands")
            m_embed.add_field(name="Play", value="Plays anything found on YT")
            m_embed.add_field(name="Pause", value="Pauses anything currently playing")
            m_embed.add_field(name="Resume", value="Resumes anything paused")
            m_embed.add_field(name="Stop", value="Stops anything playing")
            await ctx.send(embed=m_embed)
        elif category == "filtering":
            f_embed = discord.Embed(title="Filtering", description="Filtering stuff")
            f_embed.add_field(name="Capital Letter", value="Checks for capitals")
            await ctx.send(embed=f_embed)
        elif category == "misc":
            mi_embed = discord.Embed(title="Misc Commands", description="Random Commands")
            mi_embed.add_field(name="Meme", value="Sends a meme")
            mi_embed.add_field(name="Github", value="Look at the machinery")
            mi_embed.add_field(name="Create Channels", value="Create channels with current member coumnt")
            mi_embed.add_field(name="Change Status", value="Changes bot status")
            mi_embed.add_field(name="Clear", value="Clears x amount of messages up to 100")
            await ctx.send(embed=mi_embed)
        elif category == "moderation":
            mo_embed = discord.Embed(title="Moderation Commands", description="Only if someone was naughty")
            mo_embed = mo_embed.add_field(name="Kick", value=".kick <member> <reason>")
            mo_embed = mo_embed.add_field(name="Ban", value=".ban <member> <reason>")
            await ctx.send(embed=mo_embed)
        else:
            await ctx.send("Ye nah u got shit mixed up m8")

def setup(bot):
    bot.add_cog(Moderation(bot))
