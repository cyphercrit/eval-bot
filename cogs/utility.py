import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def echo(self, ctx, *, message: commands.clean_content):
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.send(message)  # checks if in DM
        else:
            await ctx.message.delete()
            await ctx.send(message)

    @commands.hybrid_command()
    async def sync(ctx: commands.Context, guild=discord.Object(id="824106396685172736")):
        await bot.tree.sync(guild=guild) # syncs application commands

async def setup(bot):
    await bot.add_cog(Utility(bot))