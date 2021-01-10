import os
import discord

from random import randrange

from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
ServerName = os.getenv("DISCORD_SERV")

LOLE = commands.Bot(command_prefix=os.getenv("COMMAND_PREFIX"), case_insensitive=True)


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
@LOLE.command(name="d20")
async def d20(ctx):
    await ctx.channel.send(randrange(1, 20))


#
@LOLE.command(name="d100")
async def d20(ctx):
    await ctx.channel.send(randrange(1, 100))


#
@LOLE.command(name="di")
async def di(ctx):
    # result of all our die rolls
    T_Return = randrange(1, 6)
    T_Return += randrange(1, 8)
    await ctx.channel.send(T_Return)


#
@LOLE.command(name="iq")
async def iq(ctx):
    T_Return = randrange(1, 200)
    await ctx.channel.send("{user} has {T_Return} iq".format(user=ctx.message.author.mention, T_Return=T_Return))

# go
LOLE.run(TOKEN)
