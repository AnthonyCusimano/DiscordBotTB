from random import randrange

from discord.ext import commands


# rolls dice man
class DiceRolls(commands.Cog):
    """lole"""

    #
    @commands.command(name="d2", aliases=["coinFlip", "flipACoin"])
    async def d2(self, ctx, _DC=1):
        try:
            if _DC == 0:
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
    @commands.command(name="d3")
    async def d3(self, ctx, _DC=1):
        try:
            if _DC == 0:
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
    @commands.command(name="d4")
    async def d4(self, ctx, _DC=1):
        try:
            if _DC == 0:
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
    @commands.command(name="d5")
    async def d5(self, ctx, _DC=1):
        try:
            if _DC == 0:
                raise TypeError
            T_Return = ''

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

    #
    @commands.command(name="d6")
    async def d6(self, ctx, _DC=1):
        try:
            if _DC == 0:
                raise TypeError
            T_Return = ''

            # result of all our die rolls
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
    @commands.command(name="ReactionRoll", aliases=["disposition"])
    async def ReactionRoll(self, ctx):
        T_Result = randrange(1, 7) + randrange(1, 7)
        T_Return = "The result of the reaction roll is "
        if T_Result < 3:
            T_Return += "the subject is hostile"
        elif T_Result < 6:
            T_Return += "the subject does not like the party, prone to attack"
        elif T_Result < 10:
            T_Return += "the subject is interested in parlaying with the party peacefully"
        else:
            T_Return += "the subject is interested in cooperation with the party"

        await ctx.channel.send(T_Return)

    #
    @commands.command(name="d6E", aliases=["D6Exlosion"])
    async def d6E(self, ctx, _DC=1):
        try:
            if _DC == 0:
                raise TypeError
            T_Return = ''

            # result of all our die rolls
            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 7)
                while T_Current % 6 == 0:
                    T_Current += randrange(1, 7)
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
    @commands.command(name="df")
    async def df(self, ctx, _DC=4):
        try:
            if _DC == 0:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Suc = 0
            for x in range(int(_DC)):
                T_Current = randrange(1, 7)
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
            if _DC == 0:
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
    @commands.command(name="d8")
    async def d8(self, ctx, _DC=1):
        try:
            if _DC == 0:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 9)
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
            if _DC == 0:
                raise TypeError
            # total result of all die rolls
            T_Return = ""
            # each roll
            T_ReturnCurrent = 0
            T_ReturnTotal = 0
            for x in range(_DC):
                T_ReturnCurrent = randrange(1, 11)
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
    @commands.command(name="d10E")
    async def d10E(self, ctx, _DC=1):
        try:
            if _DC == 0:
                raise TypeError
            # total result of all die rolls
            T_Return = ""
            # each roll
            T_ReturnCurrent = 0
            T_ReturnTotal = 0
            for x in range(_DC):
                T_ReturnCurrent = randrange(1, 11)
                while T_ReturnCurrent % 10 == 0:
                    T_ReturnCurrent += randrange(1, 11)
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
    @commands.command(name="d10s")
    async def d10f(self, ctx, _DC=1):
        try:
            if _DC == 0:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Suc = 0
            for x in range(int(_DC)):
                T_Current = randrange(1, 11)
                if T_Current > 6:
                    T_Suc += 1
                T_Return += str(T_Current)
                T_Return += ' '
            await ctx.channel.send("**" + str(T_Suc) + "** success : " + T_Return)
        except (TypeError, ValueError):
            await ctx.channel.send("Please send a real number for number of dice")

    #
    @commands.command(name="d12")
    async def d12(self, ctx, _DC=1):
        try:
            if _DC == 0:
                raise TypeError
            # total result of all die rolls
            T_Return = ""
            # each roll
            T_ReturnCurrent = 0
            T_ReturnTotal = 0
            for x in range(_DC):
                T_ReturnCurrent = randrange(1, 13)
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
            if _DC == 0:
                raise TypeError
            # total result of all die rolls
            T_Return = ""
            # each roll
            T_ReturnCurrent = 0
            T_ReturnTotal = 0
            for x in range(_DC):
                T_ReturnCurrent = randrange(1, 15)
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
            if _DC == 0:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 17)
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
            if _DC == 0:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 21)
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
    @commands.command(name="d20A", aliases=["D20WithAdvantage, d20Advantage, d20Adv"])
    async def d20A(self, ctx):
        T_ReturnA = randrange(1, 21)
        T_ReturnB = randrange(1, 21)
        if T_ReturnA > T_ReturnB:
            T_ReturnB = "~~" + str(T_ReturnB) + "~~"
        else:
            T_ReturnA = "~~" + str(T_ReturnA) + "~~"

        await ctx.channel.send(str(T_ReturnA) + " " + str(T_ReturnB))

    #
    @commands.command(name="D20DA", aliases=["D20WithDisadvantage", "d20Disadvantage", "d20Dis", "d20DisAdv"])
    async def d20DA(self, ctx):
        T_ReturnA = randrange(1, 21)
        T_ReturnB = randrange(1, 21)
        if T_ReturnA < T_ReturnB:
            T_ReturnB = "~~" + str(T_ReturnB) + "~~"
        else:
            T_ReturnA = "~~" + str(T_ReturnA) + "~~"

        await ctx.channel.send(str(T_ReturnA) + " " + str(T_ReturnB))

    #
    @commands.command(name="d24", _DC=1)
    async def d24(self, ctx, _DC=1):
        try:
            if _DC == 0:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 25)
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
            if _DC == 0:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 31)
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
            if _DC == 0:
                raise TypeError
            T_Return = ''

            T_Current = 0
            T_Total = 0
            # treating number of dice as an int
            for x in range(int(_DC)):
                T_Current = randrange(1, 101)
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
        T_Return = randrange(1, 7)
        T_Return += randrange(1, 9)
        await ctx.channel.send(T_Return)

    # core error handler for this cog
    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please send a real number for number of dice")
