from DiceRolls import DiceRolls
from NameGenerators import NameGenerators

# need these still
import os
import discord

from random import randrange
from random import choice

from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
ServerName = os.getenv("DISCORD_SERV")

LOLE = commands.Bot(command_prefix=os.getenv("COMMAND_PREFIX"), case_insensitive=True)

# Reading
# with open('Tavern.txt') as f:
#     lines = f.readlines()
tavernLines = []
# should close automatically
# TODO could probably go one by one with readline
with open("Tavern.txt") as f:
          tavernLines = f.readlines()
tavernOne = tavernLines[0].split(',')
tavernTwo = tavernLines[1].split(',')


# TODO broken LOLE
# just replace with TypeError catch
def DiceCallCheck(_int):
    #
    if _int > 50:
        return 50
    #
    if _int < 1:
        return 1


# hook up the dice roller & tavern name generator
LOLE.add_cog(DiceRolls())
LOLE.add_cog(NameGenerators())


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


# TODO find use case and properly implement
async def on_close():
    print("Closing my guy")


#
@LOLE.command(name="ping")
async def ping(ctx):
    await ctx.channel.send("Yo")


#
@LOLE.command(name="iq")
async def iq(ctx):
    T_Return = randrange(1, 200)
    await ctx.channel.send("{user} has {T_Return} iq".format(user=ctx.message.author.mention, T_Return=T_Return))


# go
LOLE.run(TOKEN)
