from os import getenv
import logging

from discord.ext import commands
from dotenv import load_dotenv

from .utils import *

# logging
logging.basicConfig(level=logging.INFO)

load_dotenv() # take environment variables from .env

# SECRETS
BOT_TOKEN = getenv('BOT_TOKEN')
PREFIX = getenv('BOT_PREFIX')

# Set prefix
bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def play(ctx, difficulty=None):
    # Gen/Set seed
    seed = gen_seed()
    
    # Generate Bingo Board

    # Create Bingo Board embed

    # Send embed

    return
    
    
bot.run(BOT_TOKEN)