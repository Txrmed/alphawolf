from discord.ext import commands
from discord.utils import get
import discord


class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='generate_verification', help='Generates verification message')
    async def generate_verification(self, ctx):
        message = await ctx.send(" Click the ✅ reaction to verify yourself")
        await message.add_reaction("✅")
        verification_message_id = message.id
        print(' [INFO] Added Verification message. ID : {}'.format(verification_message_id))

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild = self.bot.get_guild(payload.guild_id)
        role = discord.utils.get(guild.roles, name="Zweryfikowany")
        await payload.member.add_roles(role, reason="Verified Self", atomic=True)


def setup(bot):
    bot.add_cog(Verification(bot))
