# - *- coding: utf- 8 - *-
import configparser
import asyncio

loop = asyncio.get_event_loop()

# Чтение конфига
read_config = configparser.ConfigParser()
read_config.read("settings.ini")

bot_token = read_config['settings']['token'].strip().replace(" ", "")