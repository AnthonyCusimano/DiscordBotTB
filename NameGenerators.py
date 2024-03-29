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
# with open("Ship.txt") as s:
#     shipLines = s.readlines()
# shipOne = shipLines[0].split(',')
# shipTwo = shipLines[1].split(',')
# shipThree = shipLines[2].split(',')
# shipFour = shipLines[3].split(',')
# shipOne[-1] = shipOne[-1][:-1]
# shipTwo[-1] = shipTwo[-1][:-1]
# shipThree[-1] = shipThree[-1][:-1]

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
desertsPoor = mealLines[3].split('&')
desertsRich = mealLines[4].split('&')
mealOne[-1] = mealOne[-1][:-1]
mealTwo[-1] = mealTwo[-1][:-1]
desertsPoor[-1] = desertsPoor[-1][:-1]

# TODO needs update
#
with open("LocationName.txt") as l:
    locationLines = l.readlines()
locationPrefixMountain = locationLines[0].split(',')
locationPrefixGrassland = locationLines[1].split(',')
locationBaseSwamp = locationLines[2].split(',')
locationLocationMountain = locationLines[3].split(',')
# TODO
# locationTitle = locationLines[6].split(',')
locationTitle = "The "
locationPrefixMountain[-1] = locationPrefixMountain[-1][:-1]
locationPrefixGrassland[-1] = locationPrefixGrassland[-1][:-1]
locationBaseSwamp[-1] = locationBaseSwamp[-1][:-1]
locationLocationMountain[-1] = locationLocationMountain[-1][:-1]

# people
with open("CreatureNames.txt") as cr:
    creatureLines = cr.readlines()
creatureFirstNameMale = creatureLines[0].split(',')
creatureFirstNameFemale = creatureLines[1].split(',')
creatureFirstNameUnisex = creatureLines[2].split(',')
creatureLastNamePrefix = creatureLines[3].split(',')
creatureLastNameSuffix = creatureLines[4].split(',')
creatureLastNameFull = creatureLines[5].split(',')
streetNames = creatureLines[6].split(',')
greenDragonFirstNames = creatureLines[7].split(',')
greenDragonLastNames = creatureLines[8].split(',')
creatureFirstNameMale[-1] = creatureFirstNameMale[-1][:-1]
creatureFirstNameFemale[-1] = creatureFirstNameFemale[-1][:-1]
creatureFirstNameUnisex[-1] = creatureFirstNameUnisex[-1][:-1]
creatureLastNamePrefix[-1] = creatureLastNamePrefix[-1][:-1]
creatureLastNameSuffix[-1] = creatureLastNameSuffix[-1][:-1]
creatureLastNameFull[-1] = creatureLastNameFull[-1][:-1]
streetNames[-1] = streetNames[-1][:-1]
greenDragonFirstNames[-1] = greenDragonFirstNames[-1][:-1]


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


# Vyryxmythyx
# TODO have neat words for each vowel sound
def FormSilverDragonName():
    T_Vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    T_Consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    # both of these extremes sound hilarious to me
    T_NameLength = randrange(5, 18)

    T_Vowel = choice(T_Vowels)
    T_FirstLetter = choice(T_Consonants)
    T_FirstLetter = T_FirstLetter.upper()

    T_Return = T_FirstLetter
    
    for i in range(T_NameLength):

        if i % 2 == 0:
            T_Return += T_Vowel
        else:
            T_Return += choice(T_Consonants)

    return T_Return


#
def FormGreenDragonName():

    T_First = choice(greenDragonFirstNames)
    T_Last = choice(greenDragonLastNames)

    T_GreenMiddleParts = [" of ", " with "]
    T_Middle = choice(T_GreenMiddleParts)

    T_Return = T_First + T_Middle + T_Last
    return T_Return


# TODO type 4 name should read "Joho's Valor"
def FormShipName():
    T_TypeRando = randrange(0, 4)
    T_Return = ""
    T_Return = "broken method sorry"
    # if T_TypeRando == 0:
    #     T_Return = "The "
    #     T_Return += choice(shipOne)
    #     T_Return += " "
    #     T_Return += choice(shipTwo)
    #
    # elif T_TypeRando == 1:
    #     T_Return = "The "
    #     T_Return += choice(shipTwo)
    #     T_Return += " of the sea"
    #
    # elif T_TypeRando == 2:
    #     T_Return = choice(shipThree)
    # elif T_TypeRando == 3:
    #     T_Return = choice(shipFour)
    #     T_Return += "'s "
    #     T_Return += choice(shipThree)
    return T_Return


# TODO this sucks LOLE
def FormLocationName(_biome):
    T_Return = ""

    if _biome == "none":
        T_Return += choice(locationPrefixMountain + locationPrefixGrassland + locationBaseSwamp)

    if _biome == "swamp":
        T_Return += choice(locationTitle) + ' '
        T_Return += choice(locationBaseSwamp)

    return T_Return


#
def FormLastName():

    T_TypeRoll = randrange(1, 10)
    if T_TypeRoll < 6:
        return choice(creatureLastNamePrefix) + choice(creatureLastNameSuffix)
    else:
        return choice(creatureLastNameFull)


#
def FormNobleName(_gender):

    T_Return = ""

    T_UnisexNameChance = 33
    T_UnisexRoll = randrange(1, 100)

    if _gender == '0' or _gender == "male" or _gender == 'm':

        if T_UnisexRoll > T_UnisexNameChance:
            T_Return += choice(creatureFirstNameMale)
        else:
            T_Return += choice(creatureFirstNameUnisex)

        T_Return += " "
        T_Return += FormLastName()

    elif _gender == '1' or _gender == "female" or _gender == 'f':

        if T_UnisexRoll > T_UnisexNameChance:
            T_Return += choice(creatureFirstNameFemale)
        else:
            T_Return += choice(creatureFirstNameUnisex)

        T_Return += " "
        T_Return += FormLastName()

    elif _gender == "none":
        T_MaleBiasedCoinFlip = randrange(1, 10)
        if T_MaleBiasedCoinFlip > 4:

            if T_UnisexRoll > T_UnisexNameChance:
                T_Return += choice(creatureFirstNameMale)
            else:
                T_Return += choice(creatureFirstNameUnisex)

            T_Return += " "
            T_Return += FormLastName()
        else:

            if T_UnisexRoll > T_UnisexNameChance:
                T_Return += choice(creatureFirstNameFemale)
            else:
                T_Return += choice(creatureFirstNameUnisex)

            T_Return += " "
            T_Return += FormLastName()

    else:
        T_Return = "Please provide a valid gender code."

    return T_Return


#
def FormFirstName(_gender="none"):
    T_Return = ""

    T_UnisexNameChance = 33
    T_UnisexRoll = randrange(1, 100)

    if _gender == '0' or _gender == "male" or _gender == 'm':

        if T_UnisexRoll > T_UnisexNameChance:
            T_Return += choice(creatureFirstNameMale)
        else:
            T_Return += choice(creatureFirstNameUnisex)

    elif _gender == '1' or _gender == "female" or _gender == 'f':

        if T_UnisexRoll > T_UnisexNameChance:
            T_Return += choice(creatureFirstNameFemale)
        else:
            T_Return += choice(creatureFirstNameUnisex)

    elif _gender == "none":
        T_MaleBiasedCoinFlip = randrange(1, 10)
        if T_MaleBiasedCoinFlip > 4:

            if T_UnisexRoll > T_UnisexNameChance:
                T_Return += choice(creatureFirstNameMale)
            else:
                T_Return += choice(creatureFirstNameUnisex)

        else:

            if T_UnisexRoll > T_UnisexNameChance:
                T_Return += choice(creatureFirstNameFemale)
            else:
                T_Return += choice(creatureFirstNameUnisex)

    else:
        T_Return = "Please provide a valid gender code."

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

    #
    @commands.command(name="locationName",
                      aliases=["evocativeLocation", "wildernessLocation", "wildernessLocationName"])
    async def locationName(self, ctx, _biome="none"):
        await ctx.channel.send(FormLocationName(_biome))

    #
    @commands.command(name="nobleName", aliases=["noble", "nobilityName"])
    async def nobleName(self, ctx, _gender="none"):
        await ctx.channel.send(FormNobleName(_gender))

    #
    @commands.command(name="streetName", aliases=["nickname", "thiefAlias"])
    async def streetName(self, ctx):
        await ctx.channel.send(choice(streetNames))

    #
    @commands.command(name="silverDragonName")
    async def silverDragonName(self, ctx):
        await ctx.channel.send(FormSilverDragonName())

    #
    @commands.command(name="greenDragonName", aliases =["formGreenDragonName"])
    async def greenDragonName(self, ctx):
        await ctx.channel.send(FormGreenDragonName())
