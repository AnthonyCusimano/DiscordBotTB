from random import randrange
from random import choice

from discord.ext import commands

with open("Tavern.txt") as f:
    tavernLines = f.readlines()
tavernOne = tavernLines[0].split(',')
tavernTwo = tavernLines[1].split(',')


#
def FormTavernName():
    T_Return = choice(tavernOne)
    T_Return += ' '
    T_Return += choice(tavernTwo)
    return T_Return


#
class NameGenerators(commands.Cog):

    #
    @commands.command(name="tavern", aliases=["tavernName", "inn", "innName"])
    async def tavern(self, ctx):
        await ctx.channel.send(FormTavernName())
