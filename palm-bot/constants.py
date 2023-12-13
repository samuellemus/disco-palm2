# --- 
# Description: 
#  Constants file for palm-bot project
#  Contains the constants used by the palm-bot project
#  Reads from the config.properties file in the resources folder
#  and generates the constants from there.
# To get a PALM2 API key, go to: https://developers.generativeai.google/palm2
# To get a discord bot token, go to: https://discord.com/developers/applications
# 
# Author:
#  Samuel Lemus
# ---



import os 
# import dacite 
# from base import Config
from typing import Dict, List
from jproperties import Properties

def generate_discord_constants() -> Dict[str, str]:
    configs = Properties()
    with open('resources/config.properties', 'rb') as config_file:
        configs.load(config_file)
    try: 
        # calls for discord reqs 
        discord_bot_token = configs["DISCORD_TOKEN"].data
        discord_bot_url = configs["DISCORD_JOIN_URL"].data
        # return 
        return discord_bot_token, discord_bot_url
    except Exception as e:
        logger.exception(e)
        return None, None
    
def generate_palm_constants() -> Dict[str, str]:
    configs = Properties()
    with open('resources/config.properties', 'rb') as config_file:
        configs.load(config_file)
    try: 
        palm_token = configs["PALM_TOKEN"].data
        palm_url = configs["PALM_URL"].data

        # return 
        return palm_token, palm_url
    except Exception as e:
        logger.exception(e)
        return None, None