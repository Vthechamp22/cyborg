# TODO: Clear all messages
# TODO: get profile_pic
# TODO: pixelate
# TODO: announce when clearing messages
# TODO: Random number guessing game
# TEST: Handle error when cog isn't loaded and you try to reload it
# TODO: Meme adder
# TODO: Finish Tictactoe
# TODO: Add suggestions thingy

from bot import bot
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

assert TOKEN is not None, f"Token is {TOKEN!r}, please check .env"
bot.run(TOKEN)
