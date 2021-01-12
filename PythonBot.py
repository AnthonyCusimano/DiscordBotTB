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

sectionOne = ["Blue ", "Red "]

sectionTwo = ["Dragon", "Turtle"]


#
def DiceCallCheck(_int):
    #
    if _int > 50:
        return 50
    #
    if _int < 1:
        return 1


class DiceRolls(commands.Cog):
    """lole"""

    # TODO have D6 return the results on each individual die
    @commands.command(name="d6")
    async def d6(self, ctx, _DC=1):
        # result of all our die rolls
        # T_Test = int(_DC)
        T_Return = 0
        # TODO for some reason DiceCallCheck can fail if using the default value for _DC
        if _DC != 1:
            _DC = DiceCallCheck(_DC)
        # treating number of dice as an int
        for x in range(int(_DC)):
            T_Return += randrange(1, 6)
        await ctx.channel.send(T_Return)

    #
    @commands.command(name="df")
    async def df(self, ctx, _DC=4):
        T_Return = int(0)
        T_Die = 0
        # _DC = DiceCallCheck(_DC)
        for x in range(int(_DC)):
            T_Die = randrange(1, 6)
            if T_Die > 4:
                T_Return += 1
            elif T_Die < 3:
                T_Return -= 1
        await ctx.channel.send(T_Return)

    #
    @commands.command(name="d10")
    async def d10(self, ctx, _DC=1):
        # total result of all die rolls
        T_Return = ""
        for x in range(int(_DC)):
            T_Return += randrange(1, 10)

        await ctx.channel.send(T_Return)

    #
    @commands.command(name="d10s")
    async def d10f(self, ctx, _DC=1):
        T_Return = 0
        T_Die = 0
        # _DC = DiceCallCheck(_DC)
        for x in range(int(_DC)):
            T_Die = randrange(1, 10)
            if T_Die > 6:
                T_Return += 1

        T_ReturnS = str("{} successes").format(T_Return)
        await ctx.channel.send(T_ReturnS)

    #
    @commands.command(name="d16")
    async def d16(self, ctx):
        await ctx.channel.send(randrange(1, 16))

    #
    @commands.command(name="d20")
    async def d20(self, ctx):
        await ctx.channel.send(randrange(1, 20))

    #
    @commands.command(name="d100")
    async def d100(self, ctx):
        await ctx.channel.send(randrange(1, 100))

    # lole
    @commands.command(name="di")
    async def di(self, ctx):
        # result of all our die rolls
        T_Return = randrange(1, 6)
        T_Return += randrange(1, 8)
        await ctx.channel.send(T_Return)


LOLE.add_cog(DiceRolls())


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
