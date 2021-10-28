from discord.ext import commands

from HexGrid import HexGrid


#
class HexInterface(commands.Cog):
    ""

    theGrid = HexGrid()

    #
    @commands.command(name="HexStartup")
    async def HexStartup(self, ctx):
        ""
        # currently unneeded cus HexGrid calls this in it's constructor
        # HexGrid.initGrid()

    #
    @commands.command(name="movePCs", aliases=["moveOnHex"])
    async def movePCs(self, ctx, _direct):
        HexInterface.theGrid.moveParty(int(_direct))
