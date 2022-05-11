from discord.ext import commands

from Combat import Combat
# from CombatZone import CombatZone
# from CombatZoneConnection import CombatZoneConnection


#
class ManualEncounterBuilder (commands.Cogs):

    #
    def __init__(self):
        self.ourCombat = Combat()

    #
    async def AddZone(self, ctx, _name=""):
        self.ourCombat.newZone(_name)

    #
    async def AddConnection(self, ctx, _zone1, _zone2):
        """"todd"""
