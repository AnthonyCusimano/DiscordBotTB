from discord.ext import commands

from HexGrid import HexGrid


#
class HexInterface(commands.Cog):

    theGrid = HexGrid()

    #
    @commands.command(name="HexStartup")
    async def HexStartup(self, ctx):
        # currently unneeded cus HexGrid calls this in it's constructor
        # HexGrid.initGrid()
        await ctx.channel.send("currently unused sorry bud!")

    #
    @commands.command(name="movePCs", aliases=["moveOnHex", "moveParty"])
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
    @commands.command(name="getCurrentPosition", aliases=["getOurCurrentPosition", "getPCCurrentPosition",
                                                          "currentPosition"])
    async def getCurrentPosition(self, ctx):
        await ctx.channel.send("The PCs are at hex: " + str(HexInterface.theGrid.playerPosition[0]) + ", " +
                               str(HexInterface.theGrid.playerPosition[1]))


    #
    @commands.command(name="getHexType", aliases=["hexType"])
    async def getHexType(self, ctx):

        T_XFactor = HexInterface.theGrid.playerPosition[0] * 2.0
        T_YFactor = HexInterface.theGrid.playerPosition[1] * 2.0 * HexInterface.theGrid.mySizeMaxX

        await ctx.channel.send(HexInterface.theGrid[T_XFactor + T_YFactor].myPrimaryBiome)

    #
    @commands.command(name="getCurrentHexInfo", aliases=["currentHexInfo"])
    async def getCurrentHexInfo(self, ctx):

        T_XFactor = HexInterface.theGrid.playerPosition[0] * 2.0
        T_YFactor = HexInterface.theGrid.playerPosition[1] * 2.0 * HexInterface.theGrid.mySizeMaxX

        T_Return = "The PCs are at hex: " + str(HexInterface.theGrid.playerPosition[0]) + ", " +\
                   str(HexInterface.theGrid.playerPosition[1])

        T_Return += "\nThe current hex is a: " +\
                    str(HexInterface.theGrid.myGrid[int(T_YFactor + T_XFactor)].myPrimaryBiome)

        # if HexInterface.theGrid.myGrid[int(T_YFactor + T_XFactor)].myRiver[0] == -1:
        #    T_Return += ", This hex has no notable traversable river"
        # T_Return += '\n' + HexInterface.theGrid.printRiverInfo(HexInterface.theGrid.myGrid[int(T_YFactor + T_XFactor)])

        T_Return += "\nthe hex's colour is: " + HexInterface.theGrid.myGrid[int(T_YFactor + T_XFactor)].myColour

        # T_currentHexAddress = HexInterface.theGrid.myGrid[int(T_YFactor + T_XFactor)]
        await ctx.channel.send(T_Return)

    #
    @commands.command(name="gridPrintDebug", aliases=["printGrid", "gridPrint"])
    async def gridPrintDebug(self, ctx):

        T_Send = ""

        for _y in range(HexInterface.theGrid.mySizeY):
            for _x in range(HexInterface.theGrid.mySizeMaxX):
                T_Formula = (_y * HexInterface.theGrid.mySizeY) + _x
                print(T_Formula)
                T_Send += "The hex at position " + \
                          str(HexInterface.theGrid.myGrid[T_Formula].myPrimaryBiome)

                if HexInterface.theGrid.myGrid[T_Formula].isExplored:
                    T_Send += "\nthe hex is explored"

                else:
                    T_Send += "\nthe hex is not explored"

                if HexInterface.theGrid.myGrid[T_Formula].myRiver[0] > -1:
                    T_Send += " it has a river"

                else:
                    T_Send += " it does not have a river"

                T_Send += '\n'

        await ctx.channel.send(T_Send)
