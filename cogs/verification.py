from discord.ext import commands
from discord.utils import get
import discord
from discord.ext.commands import has_permissions, CheckFailure

class Verification(commands.Cog):
    """ Verification for AlphaWolf"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='generate_verification', help='Generates verification message')
    async def generate_verification(self, ctx):

        with open("X:\\Code\\Projects\\alphawolf\\cogs\\vdata.alphawolf", "r+") as f:
            data = f.read()
            if data == "1":
                await ctx.send("This verification message has been already generated.")
                return
            else:
                data = "1"
                f.write(data)

        message = await ctx.send(" Click the ✅ reaction to verify yourself")

        verification_message_id = message.id

        print(' [INFO] Added Verification message. ID : {}'.format(verification_message_id))

        # Check if Verification role already exists

        if not get(ctx.guild.roles, name="Verified"):
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

    @commands.Cog.listener()
    @has_permissions(administrator=True)
    async def clear_vdata(self, ctx):
        open("cogs/vdata.alphawolf", "w").close()
        embed = discord.Embed(title="Info", description="Cleared verification data for verification messages")
        await ctx.send(embed)

def setup(bot):
    bot.add_cog(Verification(bot))
