from random import randrange

from discord.ext import commands


class CharacterGenerators(commands.Cog):

    #
    @commands.command(name="fd6droplow", aliases=["4d6DropLowest", "4d6Char"])
    async def fd6droplow(self, ctx):
        T_Attributes = []
        T_AttributeMods = [0, 0, 0, 0, 0, 0]
        # compare rolls
        T_Rolls = [0, 0, 0, 0]


        for j in range(4):
            T_Rolls[j] = randrange(1, 6)
        # places lowest roll at the back
        T_Rolls.sort(reverse=True)
        # removes last element
        T_Rolls.pop(-1)
        # TODO ugly
        T_Attributes.append(T_Rolls[0] + T_Rolls[1] + T_Rolls[2])
        print(T_Attributes)
        T_TotalModifier = 0

    #
    @commands.command(name="LamentationsCharacter", aliases=["Lamentations", "LOTFP"])
    async def LamentationsCharacter(self, ctx):
        # alphabetical
        # 7th attribute is starting money
        T_Attributes = [0, 0, 0, 0, 0, 0, 0]
        T_AttributeMods = [0, 0, 0, 0, 0, 0]
        T_Rolls = []
        T_TotalModifier = 0
        for i in range(7):
            for j in range(3):
                T_Rolls.append(randrange(1, 6))
                T_Attributes[i] += T_Rolls[-1]

        # checking modifiers
        for i in range(6):
            if T_Attributes[i] == 3:
                T_TotalModifier -= 3
                T_AttributeMods[i] = -3

            # 4-5
            elif T_Attributes[i] < 6:
                T_TotalModifier -= 2
                T_AttributeMods[i] = -2

            # 6-8
            elif T_Attributes[i] < 9:
                T_TotalModifier -= 1
                T_AttributeMods[i] = -1

            # 9-12
            # still doing this cus I suck lole
            elif T_Attributes[i] < 13:
                T_AttributeMods[i] = 0
            # 13-15
            elif T_Attributes[i] < 16:
                T_TotalModifier += 1
                T_AttributeMods[i] = 1

            # 16-17
            elif T_Attributes[i] < 18:
                T_TotalModifier += 2
                T_AttributeMods[i] = 2

            # not using else here because we skipped 9-12
            elif T_Attributes[i] == 18:
                T_TotalModifier += 3
                T_AttributeMods[i] = 3

        T_Attributes[6] *= 10
        T_Return = "Charisma:           **{cha}**({chaMod}):        {cha1}, {cha2}, {cha3}" \
                   "\nConstitution:     **{con}**({conMod}):    {con1}, {con2}, {con3}" \
                   "\nDexterity:        **{dex}**({dexMod}):        {dex1}, {dex2}, {dex2}" \
                   "\nIntelligence:     **{int}**({intMod}):     {int1}, {int2}, {int3}" \
                   "\nStrength:         **{str}**({strMod}):         {str1}, {str2}, {str3}" \
                   "\nWisdom:           **{wis}**({wisMod}):         {wis1}, {wis2}, {wis3}" \
                   "\nStarting money:   {mon}".format(cha=T_Attributes[0], chaMod = T_AttributeMods[0], cha1=T_Rolls[0],
                                                      cha2=T_Rolls[1], cha3=T_Rolls[2], con=T_Attributes[1],
                                                      conMod=T_AttributeMods[1], con1=T_Rolls[3], con2=T_Rolls[4],
                                                      con3=T_Rolls[5], dex=T_Attributes[2], dexMod=T_AttributeMods[2],
                                                      dex1=T_Rolls[6], dex2=T_Rolls[7], dex3=T_Rolls[8],
                                                      int=T_Attributes[3], intMod=T_AttributeMods[3], int1=T_Rolls[9],
                                                      int2=T_Rolls[10], int3=T_Rolls[11], str=T_Attributes[4],
                                                      strMod=T_AttributeMods[4], str1=T_Rolls[12], str2=T_Rolls[13],
                                                      str3=T_Rolls[14], wis=T_Attributes[5], wisMod=T_AttributeMods[5],
                                                      wis1=T_Rolls[15], wis2=T_Rolls[16], wis3=T_Rolls[17],
                                                      mon=T_Attributes[6])

        if T_TotalModifier < 0:
            T_Return += "\n this character may be rerolled"
        await ctx.channel.send(T_Return)

