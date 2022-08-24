from discord.ext import commands

from NobleFamilyGenerator import NobleFamily


#
class NobleFamilyInterface(commands.Cog):

    def __init__(self):
        self.NFG = NobleFamily()

    #
    @commands.command(name="formNobleFamily")
    async def formNobleFamily(self, ctx):
        T_FamilyName = self.NFG.determineFamilyName()
        self.NFG.getFamilyCurrentSize()
        await ctx.channel.send(T_FamilyName + " " + str(self.NFG.determineChildrenName()))
