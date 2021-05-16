from random import randrange
from random import choice

from discord.ext import commands

# TODO hex location generator with biome (and surrounding biomes maybe?)

#
with open("OneShot.txt") as o:
    shotLines = o.readlines()
shotOne = shotLines[0].split(',')
shotTwo = shotLines[1].split(',')
shotThree = shotLines[2].split(',')
oneShotAccomplices = shotLines[3].split(',')
oneShotPuppetmasters = shotLines[4].split(',')
oneShot3rdParties = shotLines[5].split(',')
shotOne[-1] = shotOne[-1][:-1]
shotTwo[-1] = shotTwo[-1][:-1]
shotThree[-1] = shotThree[-1][:-1]
oneShotPuppetmasters[-1] = oneShotPuppetmasters[-1][:-1]
# oneShot3rdParties[-1] = oneShot3rdParties[-1][:-1]


#
def FormOneShot(_gamer):

    T_AdventureTypeRando = randrange(0, 2)

    T_Return = ""

    if T_AdventureTypeRando == 0:
        T_EnemyCountRando = randrange(99)
        T_EnemySize = ""
        if T_EnemyCountRando < 35:
            T_EnemySize = "Small "
        # "kinda big?
        elif T_EnemyCountRando < 70:
            T_EnemySize = "large "
        else:
            T_EnemySize = "massive "

        T_Return = "A "
        T_Return += T_EnemySize
        T_Return += "group of "
        _gamer.myHookType = choice(shotOne)
        T_Return += _gamer.myHookType
        T_Return += " has been attacking the village"

    else:
        T_EnemyCountRando = randrange(99)
        T_EnemySize = ""
        if T_EnemyCountRando < 35:
            T_EnemySize = "Small "
        # "kinda big?
        elif T_EnemyCountRando < 70:
            T_EnemySize = "large "
        else:
            T_EnemySize = "massive "

        T_Return = "A "
        T_Return += T_EnemySize
        T_Return += "group of "
        _gamer.myHookType = choice(shotOne)
        T_Return += _gamer.myHookType
        T_Return += " is encamped at a "
        T_Return += choice(shotThree)
        # TODO how far outside town?
        T_Return += " outside town"

    return T_Return


#
class OneShotGenerator(commands.Cog):

    myHookType = ""

    #
    def DetermineOneShotTwist(self):
        T_Twister = randrange(0, 2)

        T_Return = ""

        if T_Twister == 0:
            T_Return = "The group of "
            T_Return += self.myHookType
            T_Return += " are being manipulated by a "
            T_Return += choice(oneShotPuppetmasters)

        else:
            T_Return = "The group of ", self.myHookType, " are running away from a larger force of ", \
                       choice(oneShot3rdParties)

        return T_Return

    #
    @commands.command(name="OneShot", aliases=["QuickAdventure"])
    async def OneShot(self, ctx):
        await ctx.channel.send(FormOneShot(self))
        # TODO roll up secrets about the adventure and send them to the person who called this method
        await ctx.author.send(self.DetermineOneShotTwist())
