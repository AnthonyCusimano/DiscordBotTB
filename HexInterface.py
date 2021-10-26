from discord.ext import commands

from HexGrid import HexGrid


#
class HexInterface(commands.Cog):
    ""

    theGrid = HexGrid()

    #
    @commands.command(name="HexStartup")
    async def HexStartup(self):
        ""
        # currently unneeded cus HexGrid calls this in it's constructor
        # HexGrid.initGrid()

    #
    @commands.command(name="movePCs", aliases=["moveOnHex"])
    async def movePCs(self, _direct):
        print("lole")
        # HexGrid.moveParty(_direct)
