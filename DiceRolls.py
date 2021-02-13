from random import randrange

from discord.ext import commands


# rolls dice man
class DiceRolls(commands.Cog):
    """lole"""

    #
    @commands.command(name="d2", aliases=["coinFlip", "flipACoin"])
    async def d2(self, ctx, _DC=1):
        try:
            if _DC < 1:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 2)
                T_Total += T_Current
                T_Return += str(T_Current)
                #
                if x != _DC - 1:
                    T_Return += ", "

            if _DC > 1:
                await ctx.channel.send("The total is: **" + str(T_Total) + "** : " + T_Return)

            else:
                await ctx.channel.send(T_Return)

        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    #
    @commands.command(name="d3")
    async def d3(self, ctx, _DC=1):
        try:
            if _DC < 1:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 3)
                T_Total += T_Current
                T_Return += str(T_Current)
                #
                if x != _DC - 1:
                    T_Return += ", "

            if _DC > 1:
                await ctx.channel.send("The total is: **" + str(T_Total) + "** : " + T_Return)

            else:
                await ctx.channel.send(T_Return)

        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    #
    @commands.command(name="d4")
    async def d4(self, ctx, _DC=1):
        try:
            if _DC < 1:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 4)
                T_Total += T_Current
                T_Return += str(T_Current)
                #
                if x != _DC - 1:
                    T_Return += ", "

            if _DC > 1:
                await ctx.channel.send("The total is: **" + str(T_Total) + "** : " + T_Return)

            else:
                await ctx.channel.send(T_Return)

        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    #
    @commands.command(name="d5")
    async def d5(self, ctx, _DC=1):
        try:
            if _DC < 1:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 5)
                T_Total += T_Current
                T_Return += str(T_Current)
                #
                if x != _DC - 1:
                    T_Return += ", "

            if _DC > 1:
                await ctx.channel.send("The total is: **" + str(T_Total) + "** : " + T_Return)

            else:
                await ctx.channel.send(T_Return)

        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    #
    @commands.command(name="d6")
    async def d6(self, ctx, _DC=1):
        try:
            if _DC < 1:
                raise TypeError
            T_Return = ''

            # result of all our die rolls
            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 6)
                T_Total += T_Current
                T_Return += str(T_Current)
                #
                if x != _DC - 1:
                    T_Return += ", "

            if _DC > 1:
                await ctx.channel.send("The total is: **" + str(T_Total) + "** : " + T_Return)

            else:
                await ctx.channel.send(T_Return)

        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    # fudge dice
    # TODO LOLE
    @commands.command(name="df")
    async def df(self, ctx, _DC=4):
        try:
            if _DC < 1:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Suc = 0
            for x in range(int(_DC)):
                T_Current = randrange(1, 6)
                if T_Current > 4:
                    T_Suc += 1
                elif T_Current < 3:
                    T_Suc -= 1
                T_Return += str(T_Current)
                T_Return += ' '
            await ctx.channel.send("**" + str(T_Suc) + "** success : " + T_Return)
        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    #
    @commands.command(name="d7")
    async def d7(self, ctx, _DC=1):
        try:
            if _DC < 1:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 7)
                T_Total += T_Current
                T_Return += str(T_Current)
                #
                if x != _DC - 1:
                    T_Return += ", "

            if _DC > 1:
                await ctx.channel.send("The total is: **" + str(T_Total) + "** : " + T_Return)

            else:
                await ctx.channel.send(T_Return)

        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    #
    @commands.command(name="d8")
    async def d8(self, ctx, _DC=1):
        try:
            if _DC < 1:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 8)
                T_Total += T_Current
                T_Return += str(T_Current)
                #
                if x != _DC - 1:
                    T_Return += ", "

            if _DC > 1:
                await ctx.channel.send("The total is: **" + str(T_Total) + "** : " + T_Return)

            else:
                await ctx.channel.send(T_Return)

        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    #
    @commands.command(name="d10")
    async def d10(self, ctx, _DC=1):
        try:
            if _DC < 1:
                raise TypeError
            # total result of all die rolls
            T_Return = ""
            # each roll
            T_ReturnCurrent = 0
            T_ReturnTotal = 0
            for x in range(_DC):
                T_ReturnCurrent = randrange(1, 10)
                T_ReturnTotal += T_ReturnCurrent
                T_Return += str(T_ReturnCurrent)
                # not putting a coma after the final die
                if x != _DC - 1:
                    T_Return += ", "
            if _DC > 1:
                # bold for visual clarity
                # sending more info back for multiple dice
                await ctx.channel.send("The total is: **" + str(T_ReturnTotal) + "** : " + T_Return)
            else:
                await ctx.channel.send(T_Return)
        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    # exalted style successes
    # TODO I forget if 0's are crit successes in exalted LOLE
    # TODO
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
    @commands.command(name="d12")
    async def d12(self, ctx, _DC=1):
        try:
            if _DC < 1:
                raise TypeError
            # total result of all die rolls
            T_Return = ""
            # each roll
            T_ReturnCurrent = 0
            T_ReturnTotal = 0
            for x in range(_DC):
                T_ReturnCurrent = randrange(1, 12)
                T_ReturnTotal += T_ReturnCurrent
                T_Return += str(T_ReturnCurrent)
                # not putting a coma after the final die
                if x != _DC - 1:
                    T_Return += ", "
            if _DC > 1:
                # bold for visual clarity
                # sending more info back for multiple dice
                await ctx.channel.send("The total is: **" + str(T_ReturnTotal) + "** : " + T_Return)
            else:
                await ctx.channel.send(T_Return)
        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    #
    @commands.command(name="d14")
    async def d14(self, ctx, _DC=1):
        try:
            if _DC < 1:
                raise TypeError
            # total result of all die rolls
            T_Return = ""
            # each roll
            T_ReturnCurrent = 0
            T_ReturnTotal = 0
            for x in range(_DC):
                T_ReturnCurrent = randrange(1, 14)
                T_ReturnTotal += T_ReturnCurrent
                T_Return += str(T_ReturnCurrent)
                # not putting a coma after the final die
                if x != _DC - 1:
                    T_Return += ", "
            if _DC > 1:
                # bold for visual clarity
                # sending more info back for multiple dice
                await ctx.channel.send("The total is: **" + str(T_ReturnTotal) + "** : " + T_Return)
            else:
                await ctx.channel.send(T_Return)
        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    #
    @commands.command(name="d16")
    async def d16(self, ctx, _DC=1):
        try:
            if _DC < 1:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 16)
                T_Total += T_Current
                T_Return += str(T_Current)
                #
                if x != _DC - 1:
                    T_Return += ", "

            if _DC > 1:
                await ctx.channel.send("The total is: **" + str(T_Total) + "** : " + T_Return)

            else:
                await ctx.channel.send(T_Return)

        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    #
    @commands.command(name="d20")
    async def d20(self, ctx, _DC=1):
        try:
            if _DC < 1:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 20)
                T_Total += T_Current
                T_Return += str(T_Current)
                #
                if x != _DC - 1:
                    T_Return += ", "

            if _DC > 1:
                await ctx.channel.send("The total is: **" + str(T_Total) + "** : " + T_Return)

            else:
                await ctx.channel.send(T_Return)

        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    #
    @commands.command(name="d24", _DC=1)
    async def d24(self, ctx, _DC=1):
        try:
            if _DC < 1:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 24)
                T_Total += T_Current
                T_Return += str(T_Current)
                #
                if x != _DC - 1:
                    T_Return += ", "

            if _DC > 1:
                await ctx.channel.send("The total is: **" + str(T_Total) + "** : " + T_Return)

            else:
                await ctx.channel.send(T_Return)

        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    #
    @commands.command(name="d30")
    async def d30(self, ctx, _DC=1):
        try:
            if _DC < 1:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 30)
                T_Total += T_Current
                T_Return += str(T_Current)
                #
                if x != _DC - 1:
                    T_Return += ", "

            if _DC > 1:
                await ctx.channel.send("The total is: **" + str(T_Total) + "** : " + T_Return)

            else:
                await ctx.channel.send(T_Return)

        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    #
    @commands.command(name="d100")
    async def d100(self, ctx, _DC=1):
        try:
            if _DC < 1:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 100)
                T_Total += T_Current
                T_Return += str(T_Current)
                #
                if x != _DC - 1:
                    T_Return += ", "

            if _DC > 1:
                await ctx.channel.send("The total is: **" + str(T_Total) + "** : " + T_Return)

            else:
                await ctx.channel.send(T_Return)

        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

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
