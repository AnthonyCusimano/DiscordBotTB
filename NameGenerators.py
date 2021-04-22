from random import randrange
from random import choice

from discord.ext import commands

# 
with open("Tavern.txt") as f:
    tavernLines = f.readlines()
tavernOne = tavernLines[0].split(',')
tavernTwo = tavernLines[1].split(',')
tavernThree = tavernLines[2].split(',')
tavernFour = tavernLines[3].split(',')
tavernOne[-1] = tavernOne[-1][:-1]
tavernTwo[-1] = tavernTwo[-1][:-1]
tavernThree[-1] = tavernThree[-1][:-1]

# 
with open("City.txt") as c:
    cityLines = c.readlines()
cityOne = cityLines[0].split(',')
cityTwo = cityLines[1].split(',')
cityOne[-1] = cityOne[-1][:-1]
# unneeded for bottom line
# cityTwo[-1] = cityTwo[-1][:-1]

# 
with open("Ship.txt") as s:
    shipLines = s.readlines()
shipOne = shipLines[0].split(',')
shipTwo = shipLines[1].split(',')
shipThree = shipLines[2].split(',')
shipFour = shipLines[3].split(',')
shipOne[-1] = shipOne[-1][:-1]
shipTwo[-1] = shipTwo[-1][:-1]
shipThree[-1] = shipThree[-1][:-1]

# 
with open("WeaponNames.txt") as w:
    weaponLines = w.readlines()
weaponOne = weaponLines[0].split(',')
weaponTwo = weaponLines[1].split(',')
weaponOne[-1] = weaponOne[-1][:-1]

# meals have comas everywhere it's a pain
# mealOne breakfast
# mealTwo crappy lunch / dinner
# mealThree high quality lunch / dinner
with open("Meals.txt") as m:
    mealLines = m.readlines()
mealOne = mealLines[0].split('&')
mealTwo = mealLines[1].split('&')
mealThree = mealLines[2].split('&')
mealOne[-1] = mealOne[-1][:-1]
mealTwo[-1] = mealTwo[-1][:-1]


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
        T_Return += "'s "
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
def FormWeaponName():
    T_Return = choice(weaponOne)
    T_Return += " " + choice(weaponTwo)
    return T_Return


# TODO type 4 name should read "Joho's Valor"
def FormShipName():
    T_TypeRando = randrange(0, 4)
    T_Return = ""
    if T_TypeRando == 0:
        T_Return = "The "
        T_Return += choice(shipOne)
        T_Return += " "
        T_Return += choice(shipTwo)

    elif T_TypeRando == 1:
        T_Return = "The "
        T_Return += choice(shipTwo)
        T_Return += " of the sea"

    elif T_TypeRando == 2:
        T_Return = choice(shipThree)
    elif T_TypeRando == 3:
        T_Return = choice(shipFour)
        T_Return += "'s "
        T_Return += choice(shipThree)
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

    #
    @commands.command(name="ship", aliases=["shipName"])
    async def ship(self, ctx):
        await ctx.channel.send(FormShipName())

    #
    @commands.command(name="weapon", aliases=["weaponName", "formWeaponName", "magicWeaponName"])
    async def weapon(self, ctx):
        await ctx.channel.send(FormWeaponName())

