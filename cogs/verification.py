from discord.ext import commands
from discord.utils import get
import discord


class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='generate_verification', help='Generates verification message')
    async def generate_verification(self, ctx):
        message = await ctx.send(" Click the ✅ reaction to verify yourself")
        verification_message_id = message.id
        print(' [INFO] Added Verification message. ID : {}'.format(verification_message_id))

        # Check if Verification role already exists

        if get(ctx.guild.roles, name="Verified"): 
            pass
        else:
            perms = discord.Permissions()
            perms.general()
            perms.text()
            perms.voice()                            

            await ctx.guild.create_role(name="Verified", permissions=perms, colour=discord.Colour(0x00bd09))

        await message.add_reaction("✅")
        

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild = self.bot.get_guild(payload.guild_id)
        role = discord.utils.get(guild.roles, name="Verified")
        await payload.member.add_roles(role, reason="Verified Self", atomic=True)


def setup(bot):
    bot.add_cog(Verification(bot))
