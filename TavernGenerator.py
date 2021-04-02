from discord.ext import commands

import NameGenerators


class TavernGenerator(commands.Cog):

    @commands.command(name="TavernFull", aliases=["TavernComplete"])
    async def TavernFull(self, ctx):
        T_Name = NameGenerators.FormTavernName()
        await ctx.channel.send(T_Name)
        
