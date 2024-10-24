import discord
from discord.ext import commands
from discord import app_commands

class Echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="echo")
    async def echo(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(message) 

async def setup(bot):
    await bot.add_cog(Echo(bot))