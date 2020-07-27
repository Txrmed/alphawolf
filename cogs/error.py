import discord
from discord.ext import commands

class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArguments):
            await ctx.send('Please pass in all required arguments, do .help for list of functions')
            print(' [EXCEPTION] Command Did not get all required arguments')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(' You lack the permissions to do this. If you believe this is false, contact the Termed#6382')
            print(' [EXCEPTION] Command Did not get all required arguments')

def setup(bot):
    bot.add_cog(Error(bot))
