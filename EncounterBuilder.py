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

    @commands.command("goblinAmbush")
    async def goblinAmbush(self, ctx, _chaos=0):

        # ambush gets additional points
        T_myPointAdjustment = 200

        T_numSlings = random.randrange(2, numPlayers)
