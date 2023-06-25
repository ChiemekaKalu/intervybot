import discord
import responses
import asyncio
from datetime import datetime, timedelta

async def send_message(message, user_message):
    try:
        response = responses.get_response(user_message)
        if response is not None:
            await message.channel.send(response)

    except Exception as e:
        print(e)

async def disconnect_users_from_channel(channel, delay_seconds, message):
    try:
        await message.channel.send(f"Disconnecting you in {delay_seconds // 60} minutes.")
        await asyncio.sleep(delay_seconds)
        for member in channel.members:
            await member.move_to(None)
        await message.channel.send(f"Okay, you have been disconnected at: {datetime.now().strftime('%I:%M %p')}")
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'cant put this on github lol'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}"')

        if user_message.startswith('$'):
            user_message = user_message[1:]
            if user_message.lower().startswith("disconnect "):
                author_voice_state = message.author.voice
                if author_voice_state is not None:
                    author_voice_channel = author_voice_state.channel
                    time_str = user_message.lower()[11:]
                    try:
                        disconnect_time = datetime.strptime(time_str, "%I:%M %p")
                        now = datetime.now()
                        now_time = now.replace(year=1900, month=1, day=1)
                        delay_seconds = (disconnect_time - now_time).seconds
                        asyncio.create_task(disconnect_users_from_channel(author_voice_channel, delay_seconds, message))
                        print(f'Disconnecting users in {delay_seconds // 60} minutes.')
                    except ValueError:
                        await message.channel.send("Invalid time format. Please provide the time in the format 'HH:MM AM/PM'.")
                else:
                    await message.channel.send("You need to be in a voice channel to use this command.")
            else:
                await send_message(message, user_message)

    client.run(TOKEN)