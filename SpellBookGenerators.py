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
    @commands.command(name="LOTFPMUSpellBook", aliases=["LamentationsMUSB"])
    async def LOTFPMUSpellBook(self, ctx):
        # Everyone starts with this
        T_Return = "Read magic, "
        T_DupProt = []
        for i in range(3):
            T_DupProt.append(choice(LOTFPCoreMUSpells))

        while T_DupProt[0] == T_DupProt[1] or T_DupProt[0] == T_DupProt[2]:
            T_DupProt[0] = choice(LOTFPCoreMUSpells)

        while T_DupProt[1] == T_DupProt[2]:
            T_DupProt[1] = choice(LOTFPCoreMUSpells)

        for i in range(3):
            T_Return += T_DupProt[i]
            T_Return += ", "
        await ctx.channel.send(T_Return)
