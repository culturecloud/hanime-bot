import logging
import uvloop
import asyncio

from os import path
from dotenv import load_dotenv

load_dotenv()

from bot.log_config import setup_logging

if path.exists('info.log'):
    with open('info.log', 'r+') as f:
        f.truncate(0)
if path.exists('debug.log'):
    with open('debug.log', 'r+') as f:
        f.truncate(0)

setup_logging()
LOGGER = logging.getLogger(__name__)

main_loop = uvloop.new_event_loop()
asyncio.set_event_loop(main_loop)