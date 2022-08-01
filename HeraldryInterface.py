from discord.ext import commands

from HeraldryGenerator import HeraldryGenerator


#
class HeraldryInterface(commands.Cog):

    gamer = HeraldryGenerator()

    @commands.command(name="createHeraldry", aliases=["heraldry"])
    async def createHeraldry(self, ctx):
        await ctx.channel.send(self.gamer.createHeraldry())
