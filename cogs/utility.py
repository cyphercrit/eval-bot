import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

class echoFlags(commands.FlagConverter):
    message: str

@commands.hybrid_command()
async def echo()