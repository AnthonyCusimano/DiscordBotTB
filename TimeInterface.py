from discord.ext import commands

from Time import Time

tim = Time()


#
class TimeInterface(commands.Cog):

    #
    @commands.command(name="whatTimeIsIt", aliases=["time"])
    async def whatTimeIsIt(self, ctx):
        # T_Post = "I'm working on it"
        T_Post = str(tim.timeOfDay[0])
        # T_Post = str(TimeInterface.tim.timeOfDay[0])
        await ctx.channel.send(T_Post)
