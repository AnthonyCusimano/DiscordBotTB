from DiceRolls import DiceRolls

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

# tavern name garbage
# TODO create external tool for this
sectionOne = ["Blue", "Red"]
sectionTwo = ["Dragon", "Turtle"]


# TODO broken LOLE
# just replace with TypeError catch
def DiceCallCheck(_int):
    #
    if _int > 50:
        return 50
    #
    if _int < 1:
        return 1


# hook up the dice roller
LOLE.add_cog(DiceRolls())


# 
def FormTavernName():
    T_Return = choice(sectionOne)
    T_Return += choice(sectionTwo)
    return T_Return


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
@LOLE.command(name="iq")
async def iq(ctx):
    T_Return = randrange(1, 200)
    await ctx.channel.send("{user} has {T_Return} iq".format(user=ctx.message.author.mention, T_Return=T_Return))


#
@LOLE.command(name="tavern")
async def tavern(ctx):
    await ctx.channel.send(FormTavernName())

# go
LOLE.run(TOKEN)
