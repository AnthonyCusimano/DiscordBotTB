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

    # TODO turbo broken lole
    @commands.command(name="getCurrentHexInfo", aliases=["currentHexInfo"])
    async def getCurrentHexInfo(self, ctx):
        # TODO try Y*2*X = Y &&&&& X*2
        T_XFactor = HexInterface.theGrid.playerPosition[0] * 2.0
        T_YFactor = HexInterface.theGrid.playerPosition[1] * 2.0 * HexInterface.theGrid.mySizeMaxX

        T_currentHexAddress = HexInterface.theGrid.myGrid[int(T_YFactor + T_XFactor)]
        # await ctx.channel.send("The current hex is a: " +
        #                        str(HexInterface.theGrid.myGrid[T_currentHexAddress].myPrimaryBiome))
