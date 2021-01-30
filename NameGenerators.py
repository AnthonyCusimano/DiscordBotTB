from random import randrange
from random import choice

from discord.ext import commands

with open("Tavern.txt") as f:
    tavernLines = f.readlines()
tavernOne = tavernLines[0].split(',')
tavernTwo = tavernLines[1].split(',')
tavernOne[-1] = tavernOne[-1][:-1]
tavernTwo[-1] = tavernTwo[-1][:-1]


#
def FormTavernName():
    T_TypeRando = randrange(0, 50)
    T_Return = ""
    if T_TypeRando > 25:
        T_Return = choice(tavernOne)
        T_Return += ' '
        T_Return += choice(tavernTwo)
    # type two
    else:
        T_Return = choice(tavernTwo)
        # making sure you can't have a "wagon and wagon"
        T_ReturnProtection = T_Return
        T_ReturnTwo = choice(tavernTwo)
        while T_ReturnTwo == T_ReturnProtection:
            T_ReturnTwo = choice(tavernTwo)
        T_Return += " and "
        T_Return += T_ReturnTwo
    return T_Return


#
class NameGenerators(commands.Cog):

    #
    @commands.command(name="tavern", aliases=["tavernName", "inn", "innName"])
    async def tavern(self, ctx):
        await ctx.channel.send(FormTavernName())

    #
    @commands.command(name="townAlias", aliases=["town"])
    async def townAlias(self, ctx):
        await ctx.channel.send("under construction command")
