from discord.ext import commands

from Time import Time

tim = Time()


#
class TimeInterface(commands.Cog):

    #
    @commands.command(name="whatTimeIsIt", aliases=["time"])
    async def whatTimeIsIt(self, ctx):

        T_Post = "The current in game time is "
        T_Post += str(tim.timeOfDay[0]) + ":" + str(tim.timeOfDay[1])
        await ctx.channel.send(T_Post)
