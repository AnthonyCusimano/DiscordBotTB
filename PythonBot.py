import os
import discord
import random

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
ServerName = os.getenv("DISCORD_SERV")

client = discord.Client()


# on launch
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild = discord.utils.get(client.guilds, name=ServerName)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    # num members
    count = guild.member_count
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


# primary listener
@client.event
async def on_message(_message):
    if _message.author == client.user:
        return

    # gamer check
    if "gamer" in _message.content.lower():
        T_Response = "Gamer!"
        await _message.channel.send(T_Response)

#
client.run(TOKEN)
