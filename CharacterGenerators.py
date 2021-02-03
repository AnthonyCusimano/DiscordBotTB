from random import randrange

from discord.ext import commands


class CharacterGenerators(commands.Cog):
    print("LOLE")

    @commands.command(name="LamentationsCharacter", aliases=["Lamentations", "LOTFP"])
    async def LamentationsCharacter(self, ctx):
        # alphabetical
        # 7th attribute is starting money
        T_Attributes = [0, 0, 0, 0, 0, 0, 0]
        T_Rolls = []
        for i in range(7):
            for j in range(3):
                T_Rolls.append(randrange(1, 6))
                T_Attributes[i] += T_Rolls[-1]

        T_Attributes[6] *= 10
        T_Return = "Charisma:           **{cha}**:        {cha1}, {cha2}, {cha3}" \
                   "\nConstitution:     **{con}**:    {con1}, {con2}, {con3}" \
                   "\nDexterity:        **{dex}**:        {dex1}, {dex2}, {dex2}" \
                   "\nIntelligence:     **{int}**:     {int1}, {int2}, {int3}" \
                   "\nStrength:         **{str}**:         {str1}, {str2}, {str3}" \
                   "\nWisdom:           **{wis}**:         {wis1}, {wis2}, {wis3}" \
                   "\nStarting money:   {mon}".format(cha=T_Attributes[0], cha1=T_Rolls[0], cha2=T_Rolls[1],
                                                    cha3=T_Rolls[2], con=T_Attributes[1], con1=T_Rolls[3],
                                                    con2=T_Rolls[4], con3=T_Rolls[5], dex=T_Attributes[2],
                                                    dex1=T_Rolls[6], dex2=T_Rolls[7], dex3=T_Rolls[8],
                                                    int=T_Attributes[3], int1=T_Rolls[9], int2=T_Rolls[10],
                                                    int3=T_Rolls[11], str=T_Attributes[4], str1=T_Rolls[12],
                                                    str2=T_Rolls[13], str3=T_Rolls[14], wis=T_Attributes[5],
                                                    wis1=T_Rolls[15], wis2=T_Rolls[16], wis3=T_Rolls[17],
                                                    mon=T_Attributes[6])
        await ctx.channel.send(T_Return)

