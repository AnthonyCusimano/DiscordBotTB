from discord.ext import commands

from HexGrid import HexGrid


#
class HexInterface(commands.Cog):

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

        try:
            if int(_direct) < 0 or int(_direct) > 5:
                raise ValueError
            T_FormerPCPosition = [HexInterface.theGrid.playerPosition[0], HexInterface.theGrid.playerPosition[1]]
            HexInterface.theGrid.moveParty(int(_direct))
            await ctx.channel.send("the PCs moved from hex " + str(T_FormerPCPosition[0]) + ", " +
                                   str(T_FormerPCPosition[1]) + " to hex " +
                                   str(HexInterface.theGrid.playerPosition[0]) + ", " +
                                   str(HexInterface.theGrid.playerPosition[1]))
        except(TypeError, ValueError):
            await ctx.channel.send("Please send a real number for movement (0-5)")

    #
    @commands.command(name="getCurrentPosition", aliases=["getOurCurrentPosition", "getPCCurrentPosition"])
    async def getCurrentPosition(self, ctx):
        await ctx.channel.send("The PCs are at hex: " + str(HexInterface.theGrid.playerPosition[0]) + ", " +
                               str(HexInterface.theGrid.playerPosition[1]))

    #
    @commands.command(name="getCurrentHexInfo", aliases=["currentHexInfo"])
    async def getCurrentHexInfo(self, ctx):

        T_XFactor = HexInterface.theGrid.playerPosition[0] * 2.0
        T_YFactor = HexInterface.theGrid.playerPosition[1] * 2.0 * HexInterface.theGrid.mySizeMaxX

        T_Return = "The current hex is a: " +\
                   str(HexInterface.theGrid.myGrid[int(T_YFactor + T_XFactor)].myPrimaryBiome)

        if HexInterface.theGrid.myGrid[int(T_YFactor + T_XFactor)].myRiver[0] == -1:
            T_Return += ", This hex has no notable traversable river"

        T_currentHexAddress = HexInterface.theGrid.myGrid[int(T_YFactor + T_XFactor)]
        await ctx.channel.send(T_Return)

    #
    @commands.command(name="gridPrintDebug", aliases=["printGrid", "gridPrint"])
    async def gridPrintDebug(self, ctx):

        for _y in range(HexInterface.theGrid.mySizeY):
            for _x in range(HexInterface.theGrid.mySizeMaxX):
                T_Send = ""
                T_Send = "The hex at position " + \
                         str(HexInterface.theGrid.myGrid[int(_y + (_x * (_y+1)))].myPrimaryBiome)

                if HexInterface.theGrid.myGrid[int(_y + (_x * (_y+1)))].myRiver[0] < -1:
                    T_Send += " it has a river"

                else:
                    T_Send += " it does not have a river"

                await ctx.channel.send(T_Send)
