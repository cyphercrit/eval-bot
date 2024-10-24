import discord
from discord.ext import commands
from discord import app_commands

class Sync(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="sync")
    @commands.is_owner()  # ensures only the bot owner can use this command
    async def sync(self, ctx, guild_id: int = None):  # accepts guild id as optional argument
        if guild_id is None:
            # syncs globally when no id is provided
            await self.bot.tree.sync()
            await ctx.send('Global Application Commands Synced!')
        else:
            # syncs to specified guild
            guild = discord.Object(id=guild_id)
            await self.bot.tree.sync(guild=guild)
            await ctx.send(f'Application Commands Synced to Guild ID {guild_id}!')

async def setup(bot):
    await bot.add_cog(Sync(bot))