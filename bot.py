import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='e.', intents=intents)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

cogs = ["echo", "sync"]
async def load_cogs(): # loads cogs
    for cog in cogs:
        try:
            await bot.load_extension(f'cogs.{cog.lower()}')
            print(f'{cog} cog loaded.')
        except Exception as e:
            print(f'Failed to load {cog} cog: {e}')

@bot.event
async def on_ready():
    await load_cogs()
    print(f'Initialized: {bot.user}')

@bot.event
async def on_message(message): # checks to make sure bot doesn't reply to it's own commands
    if message.author == bot.user:
        return
    await bot.process_commands(message)

bot.run(TOKEN)
