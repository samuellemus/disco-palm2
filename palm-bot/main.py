# --- 
# Description: 
#  Main file for palm-bot project
#  Contains the discord client, which is used to listen for messages
#  from users, and respond to them with a message from the palm api.
#  This is a very basic implementation and I intend to improve it over time. 
# Author:
#  Samuel Lemus
# --- 

import discord
import json 
import logging 
import os 
import requests 

from base import Message, Conversation 
from constants import generate_discord_constants
from discord import Message as DiscordMessage
from utils import palm_bot

intents = discord.Intents.default() 
intents.message_content = True 
client = discord.Client(intents = intents) 
tree = discord.app_commands.CommandTree(client)

logging.basicConfig(format="[%(asctime)s] [%(filename)s:%(lineno)d] %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

palm_bot()

@client.event 
async def on_ready():
    logger.info(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message: DiscordMessage): 
    try : 
        if message.author == client.user: 
            return 
        if message.content.startswith('hey palm, '): 
            # TODO: Implement command tree
            # 
            message.content = message.content[10:]
            response = palm_bot.query_palm(message.content)
            await message.channel.send(response)

    except Exception as e:
        logger.exception(e)

discord_bot_token, discord_bot_url = generate_discord_constants()

client.run(discord_bot_token)

