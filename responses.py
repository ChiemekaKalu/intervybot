import asyncio
import random
from datetime import datetime

async def disconnect_users_from_channel(channel, delay_seconds):
    await asyncio.sleep(delay_seconds)
    for member in channel.members:
        await member.move_to(None)

import re
from datetime import datetime

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there! I am totally not a schmegbot..'
    if p_message == 'andie':
        return 'It seems the fight for andy has begun..'
    if p_message == 'roll':
      roll = random.randint(1, 7)
      if roll == 7:
        return ":punch: :boom: You just got fucking ARM BARRED! https://tenor.com/view/wrestling-ronda-rousey-hall-da-fama-do-ufc-brasil-arm-bar-gif-16847389"
      else:
        return str(roll)

    if p_message == 'help':
        return '`I am a bot built by schmeeg and I am a work in progress`'

    return 'I did not understand what you wrote. Try $help.'
