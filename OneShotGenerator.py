from random import randrange
from random import choice

from discord.ext import commands


#
with open("OneShot.txt") as o:
    shotLines = o.readlines()
shotOne = shotLines[0].split(',')
shotTwo = shotLines[1].split(',')
shotOne[-1] = shotOne[-1][:-1]


#
def FormOneShot():
    T_Return = "A small group of "
    T_Return += choice(shotOne)
    T_Return += " has been attacking the village"

    return T_Return


#
class OneShotGenerator(commands.Cog):

    #
    @commands.command(name="OneShot", aliases=["QuickAdventure"])
    async def OneShot(self, ctx):
        await ctx.channel.send(FormOneShot())
