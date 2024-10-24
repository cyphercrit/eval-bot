import discord
from discord.ext import commands, app_commands

class Echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def echo(self, ctx, *, message: commands.clean_content):
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.send(message)  # checks if in DM
        else:
            await ctx.message.delete()
            await ctx.send(message)

async def setup(bot):
    await bot.add_cog(Echo(bot))