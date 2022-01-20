from discord.ext import commands

from EncounterBuilder import EncounterBuilder


#
class EncounterInterface(commands.Cog):

    myBuilder = EncounterBuilder()

    @commands.command(name="Attack")
    async def Attack(self, _targetID):

