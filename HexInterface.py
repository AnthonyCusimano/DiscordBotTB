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

    #
    @commands.command(name="getCurrentPosition", aliases=["getOurCurrentPosition", "getPCCurrentPosition"])
    async def getCurrentPosition(self, ctx):
        await ctx.channel.send("The PCs are at hex: " + str(HexInterface.theGrid.playerPosition[0]) + ", " +
                               str(HexInterface.theGrid.playerPosition[1]))
