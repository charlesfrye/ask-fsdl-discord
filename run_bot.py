import os

import discord
from dotenv import load_dotenv

import bot

load_dotenv()
DISCORD_AUTH = os.environ["DISCORD_AUTH"]

client = bot.make_client()

client.run(DISCORD_AUTH)
