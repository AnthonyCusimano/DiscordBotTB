from discord.ext import commands

from Time import Time

tim = Time()


#
class TimeInterface(commands.Cog):

    #
    @commands.command(name="whatTimeIsIt", aliases=["time", "timeOfDay"])
    async def whatTimeIsIt(self, ctx):

        T_Post = "The current in game time is "
        # T_Post += str(tim.timeOfDay[0]) + ":" + str(tim.timeOfDay[1])
        T_Post += tim.timeOfDayToString()
        await ctx.channel.send(T_Post)

    #
    @commands.command(name="whatMonthIsIt", aliases=["month"])
    async def whatMonthIsIt(self, ctx):

        T_Post = "The current month is "
        T_Post += tim.getMonthName()

        await ctx.channel.send(T_Post)
