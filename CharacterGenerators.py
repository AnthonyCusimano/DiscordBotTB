from random import randrange

from discord.ext import commands


class CharacterGenerators(commands.Cog):
    print("LOLE")

    @commands.command(name="LamentationsCharacter", aliases=["Lamentations", "LOTFP"])
    async def LamentationsCharacter(self, ctx):
        # alphabetical
        # 7th attribute is starting money
        T_Attributes = [0, 0, 0, 0, 0, 0, 0]
        for i in range(7):
            for j in range(3):
                T_Attributes[i] += randrange(1, 6)

        T_Attributes[6] *= 10
        T_Return = "Charisma: {cha}\nConstitution: {con}\nDexterity: {dex}\nIntelligence: {int}\nStength: {str}" \
                   "\nWisdom: {wis}\nStarting money: {mon}".format(cha=T_Attributes[0], con=T_Attributes[1],
                                                                   dex=T_Attributes[2], int=T_Attributes[3],
                                                                   str=T_Attributes[4], wis=T_Attributes[5],
                                                                   mon=T_Attributes[6])
        await ctx.channel.send(T_Return)

