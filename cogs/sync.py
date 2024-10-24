import discord
from discord.ext import commands

class Sync(commands.cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def sync(self, ctx):
        await ctx.bot.tree.copy_global_to(guild=ctx.guild)
        await ctx.send(f'Application Commands Synced!')

async def setup(bot):
    await bot.add_cog(Sync(bot))