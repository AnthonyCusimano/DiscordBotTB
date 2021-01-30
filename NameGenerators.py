from random import randrange
from random import choice

from discord.ext import commands

with open("Tavern.txt") as f:
    tavernLines = f.readlines()
tavernOne = tavernLines[0].split(',')
tavernTwo = tavernLines[1].split(',')
tavernThree = tavernLines[2].split(',')
tavernFour = tavernLines[3].split(',')
tavernOne[-1] = tavernOne[-1][:-1]
tavernTwo[-1] = tavernTwo[-1][:-1]
tavernThree[-1] = tavernThree[-1][:-1]
# ignoring bottom line

with open("City.txt") as c:
    cityLines = c.readlines()
cityOne = cityLines[0].split(',')
cityTwo = cityLines[1].split(',')
cityOne[-1] = cityOne[-1][:-1]
# unneeded for bottom line
# cityTwo[-1] = cityTwo[-1][:-1]


#
def FormTavernName():
    T_TypeRando = randrange(0, 75)
    T_Return = ""
    if T_TypeRando > 25:
        T_Return = choice(tavernOne)
        T_Return += ' '
        T_Return += choice(tavernTwo)
    # type two
    elif T_TypeRando > 50:
        T_Return = choice(tavernTwo)
        # making sure you can't have a "wagon and wagon"
        T_ReturnProtection = T_Return
        T_ReturnTwo = choice(tavernTwo)
        while T_ReturnTwo == T_ReturnProtection:
            T_ReturnTwo = choice(tavernTwo)
        T_Return += " and "
        T_Return += T_ReturnTwo

    # type three
    else:
        T_Return = choice(tavernThree)
        T_Return += ' '
        T_Return += choice(tavernFour)
    return T_Return


#
def FormCityName():
    T_TypeRando = randrange(0, 2)
    T_Return = ""
    if T_TypeRando < 1:
        T_Return = "The "
        T_Return += choice(cityOne)
        T_Return += " City"
    else:
        T_Return = "City of "
        T_Return += choice(cityTwo)
    return T_Return


#
class NameGenerators(commands.Cog):

    #
    @commands.command(name="tavern", aliases=["tavernName", "inn", "innName"])
    async def tavern(self, ctx):
        await ctx.channel.send(FormTavernName())

    #
    @commands.command(name="cityAlias", aliases=["city"])
    async def cityAlias(self, ctx):
        await ctx.channel.send(FormCityName())
