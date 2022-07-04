from random import randrange

from discord.ext import commands


# TODO start with 5e DMG process
class DungeonGenerator(commands.Cog):

    # 
    def __init__(self):
        # D10
        sizeSeed = randrange(9)
        # small dungeon
        if sizeSeed < 4:
            self.mySizeSeed = "small"
        # medium dungeon
        elif sizeSeed < 9:
            self.mySizeSeed = "medium"
        # large dungeon
        else:
            self.mySizeSeed = "large"

    #
    @ commands.command(name="randDungeon", aliases=["randomDungeon"])
    async def randDungeon(self, ctx):
        await ctx.channel.send(self.mySizeSeed)
