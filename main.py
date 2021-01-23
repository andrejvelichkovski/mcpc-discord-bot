# Imports the discord and os modules needed to run everything
import discord

import random

# The dotenv modules allows us to use 
# .env file to save our tokens safely
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ';commands' or message.content == ';help':
        await message.channel.send("List of all commands")        

client.run(TOKEN)