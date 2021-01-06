import os
import discord
from random import randrange

from dotenv import load_dotenv
load_dotenv()

from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
ServerName = os.getenv("DISCORD_SERV")

# LOLE = discord.Client()
LOLE = commands.Bot(command_prefix="!")

# prefix
# STATIC_BOT_PREFIX = "!LOLE"


# on launch
@LOLE.event
async def on_ready():
    print(f'{LOLE.user} has connected to Discord!')
    guild = discord.utils.get(LOLE.guilds, name=ServerName)

    print(
        f'{LOLE.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    # num members
    T_MemberCount = guild.member_count
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


#
@LOLE.command(name="ping")
async def ping(ctx):
    await ctx.channel.send("Yo")


#
@LOLE.command(name="d6")
async def d6(ctx, _DC=1):
    # result of all our die rolls
    T_Return = 0
    # treating number of dice as an int
    for x in range(int(_DC)):
        T_Return += randrange(1, 6)
    await ctx.channel.send(T_Return)


#
@LOLE.command(name="di")
async def di(ctx):
    # result of all our die rolls
    T_Return = randrange(1, 6)
    T_Return += randrange(1, 8)
    await ctx.channel.send(T_Return)

#
LOLE.run(TOKEN)
