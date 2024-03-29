from discord.ext import commands
# from random import randrange
from random import *

# FormTavernName
import NameGenerators


#
class TavernGenerator(commands.Cog):

    #
    def __init__(self):
        self.mySize = 0

    #
    def getMyRoomsAvailable(self):
        if self.mySize == 1:
            # rooms available low
            return randrange(0, 3)

        elif self.mySize == 2:
            return randrange(0, 5)

        elif self.mySize == 3:
            return randrange(1, 6)

        elif self.mySize == 4:
            return randrange(3, 14)

        elif self.mySize == 5:
            return randrange(6, 22)

        elif self.mySize == 6:
            return randrange(10, 30)

    # 
    def getMyBreakfast(self):
        return choice(NameGenerators.mealOne)

    #
    def getMyDinner(self):
        T_DinnerQuality = randint(1,12)

        if T_DinnerQuality < 10:
            return choice(NameGenerators.mealTwo)

        else:
            return choice(NameGenerators.mealThree)

    #
    @commands.command(name="TavernFull", aliases=["TavernComplete"])
    async def TavernFull(self, ctx):
        T_Name = NameGenerators.FormTavernName()
        # TODO think about mySize
        self.mySize = randrange(1, 6)
        await ctx.channel.send((T_Name + " Has " + str(self.getMyRoomsAvailable()) + " rooms available"))
        await ctx.channel.send("For breakfast they are serving " + self.getMyBreakfast())
        await ctx.channel.send("For lunch and dinner they are serving " + self.getMyDinner())
