from discord.ext import commands

import random

goblinAnkleShankerPoints = 100
goblinHunterSlingPoints = 50

# tbh I forget if this goes here lole
numPlayers = 4
playerLevel = 1


#
class EncounterBuilder(commands.Cog):
    """"""""

    def pointCalculator(self):
        return numPlayers * playerLevel

    @commands.command("goblinAmbush")
    async def goblinAmbush(self, ctx, _chaos=0):

        # ambush gets additional points and are always deadly++
        T_myPointAdjustment = 200
        T_myPointValue = 200 + self.pointCalculator()
        T_myPointsRemaining = T_myPointValue

        # horribly named number of blowguns
        T_numSlings = random.randrange(2, numPlayers)

        # TODO meld adding units to an encounter and removing points from the encounter

        T_myPointsRemaining -= T_numSlings * goblinHunterSlingPoints

        T_Return = {}

        for i in range(T_numSlings):
            T_Return[-1] = "sling"

        # all we have left is ankleshankers currently
        while T_myPointsRemaining > 0:
            T_Return[-1] = "ankleshanker"
            T_myPointsRemaining -= goblinAnkleShankerPoints

        return T_Return

