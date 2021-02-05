from random import randrange
from random import choice

from discord.ext import commands

# magic user spells
# remember everyone starts with Read Magic so reroll on
LOTFPCoreMUSpells = ["Bookspeak", "Charm Person", "Comprehend Languages / Obscure Languages", "Detect Magic",
                     "Detect Magic", "Enlarge / Reduce", "Faerie Fire", "Feather Fall", "Floating Disc",
                     "Hold Portal", "Identify", "Light / Darkness", "Magic Aura / Obscure Aura", "Magic Missile",
                     "Mending", "Message", "Shield", "Sleep", "Spider Climb", "Summon", "Unseen Servant"]


#
class SpellBookGenerators(commands.Cog):

    #
    @commands.command(name="LOTFPSpellBook", aliases=["LamentationsSB"])
    async def LOTFPSpellBook(self, ctx):
        T_Return = "Read magic, "
        for i in range(3):
            T_Return += choice(LOTFPCoreMUSpells)
            T_Return += ", "
        await ctx.channel.send(T_Return)
