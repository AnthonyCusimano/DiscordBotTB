from random import randrange

from discord.ext import commands


# rolls dice man
class DiceRolls(commands.Cog):
    """lole"""

    #
    @commands.command(name="d3")
    async def d3(self, ctx):
        await ctx.channel.send(randrange(1, 3))

    #
    @commands.command(name="d4")
    async def d4(self, ctx):
        await ctx.channel.send(randrange(1, 4))

    #
    @commands.command(name="d5")
    async def d5(self, ctx):
        await ctx.channel.send(randrange(1, 5))

    # TODO have D6 return the results on each individual die
    @commands.command(name="d6")
    async def d6(self, ctx, _DC=1):
        # result of all our die rolls
        # T_Test = int(_DC)
        T_Return = 0
        # TODO for some reason DiceCallCheck can fail if using the default value for _DC
        # treating number of dice as an int
        for x in range(int(_DC)):
            T_Return += randrange(1, 6)
        await ctx.channel.send(T_Return)

    # fudge dice
    @commands.command(name="df")
    async def df(self, ctx, _DC=4):
        T_Return = int(0)
        T_Die = 0
        for x in range(int(_DC)):
            T_Die = randrange(1, 6)
            if T_Die > 4:
                T_Return += 1
            elif T_Die < 3:
                T_Return -= 1
        await ctx.channel.send(T_Return)

    #
    @commands.command(name="d7")
    async def d7(self, ctx):
        await ctx.channel.send(randrange(1, 7))

    #
    @commands.command(name="d8")
    async def d8(self, ctx):
        await ctx.channel.send(randrange(1, 8))

    #
    @commands.command(name="d10")
    async def d10(self, ctx, _DC=1):
        try:
            if not _DC:
                T_DC = 1
            else:
                T_DC = int(_DC)

            if T_DC < 1:
                raise TypeError
            # total result of all die rolls
            T_Return = ""
            # each roll
            T_ReturnCurrent = 0
            T_ReturnTotal = 0
            for x in range(T_DC):
                T_ReturnCurrent = randrange(1, 10)
                T_ReturnTotal += T_ReturnCurrent
                T_Return += str(T_ReturnCurrent)
                # not putting a coma after the final die
                if x != T_DC - 1:
                    T_Return += ", "
            if T_DC > 1:
                # bold for visual clarity
                # sending more info back for multiple dice
                await ctx.channel.send("The total is: **" + str(T_ReturnTotal) + "** : " + T_Return)
            else:
                await ctx.channel.send(T_Return)
        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    # exalted style successes
    # TODO I forget if 0's are crit successes in exalted LOLE
    @commands.command(name="d10s")
    async def d10f(self, ctx, _DC=1):
        T_Return = 0
        T_ReturnTotal = 0
        T_Die = 0
        # _DC = DiceCallCheck(_DC)
        for x in range(int(_DC)):
            T_Die = randrange(1, 10)
            if T_Die > 6:
                T_Return += 1

        T_ReturnS = str("{} successes").format(T_Return)
        await ctx.channel.send(T_ReturnS)

    #
    @commands.command(name="d16")
    async def d16(self, ctx):
        await ctx.channel.send(randrange(1, 16))

    #
    @commands.command(name="d20")
    async def d20(self, ctx):
        await ctx.channel.send(randrange(1, 20))

    #
    @commands.command(name="d24", _DC=1)
    async def d24(self, ctx):
        await ctx.channel.send(randrange(1, 24))

    #
    @commands.command(name="d30")
    async def d30(self, ctx):
        await ctx.channel.send(randrange(1, 30))

    #
    @commands.command(name="d100")
    async def d100(self, ctx):
        await ctx.channel.send(randrange(1, 100))

    # lole
    # returns a D6 roll + a D8 roll
    @commands.command(name="di")
    async def di(self, ctx):
        # result of all our die rolls
        T_Return = randrange(1, 6)
        T_Return += randrange(1, 8)
        await ctx.channel.send(T_Return)

    # core error handler for this cog
    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please send a real number for number of dice")
