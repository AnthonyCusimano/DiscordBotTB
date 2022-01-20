from discord.ext import commands

from Monster import Monster

import random

goblinAnkleShankerPoints = 100
goblinHunterSlingPoints = 50

anhkegPoints = 450

# tbh I forget if this goes here lole
numPlayers = 4
playerLevel = 1


#
class EncounterBuilder(commands.Cog):

    monsters = []

    #
    def pointCalculator(self):
        return numPlayers * playerLevel

    #
    @commands.command("goblinAmbush")
    async def goblinAmbush(self, ctx, _chaos=0):

        # ambush gets additional points and are always deadly++
        T_myPointAdjustment = 200
        T_myPointValue = T_myPointAdjustment + self.pointCalculator()
        T_myPointsRemaining = T_myPointValue

        # horribly named number of blowguns
        T_numSlings = random.randrange(2, numPlayers)

        # TODO meld adding units to an encounter and removing points from the encounter

        T_myPointsRemaining -= T_numSlings * goblinHunterSlingPoints

        T_Return = []

        for i in range(T_numSlings):
            # fake adding one to i just for user comfort
            EncounterBuilder.monsters.append(Monster("Goblin Slinger " + str(i)))
            T_Return.append("sling")

        T_Counter = 1
        # all we have left is ankleshankers currently
        while T_myPointsRemaining > 0:

            EncounterBuilder.monsters.append(Monster("Goblin Ankle Shanker" + str(T_Counter)))
            T_Return.append("ankleshanker")
            T_myPointsRemaining -= goblinAnkleShankerPoints
            T_Counter += 1

        print(len(EncounterBuilder.monsters))
        for i in range(len(EncounterBuilder.monsters)):
            print(EncounterBuilder.monsters[i].myName)
        await ctx.channel.send(T_Return)

    @commands.command("roamingAnkheg")
    async def roamingAnkheg(self, ctx):

        if playerLevel == 2:
            ""

        T_MyPointAdjustment = 0
        T_myPointValue = T_MyPointAdjustment + self.pointCalculator()

        # TODO

    @commands.command("singleMonster")
    async def singleMonster(self, HD=1):
        ""

