from random import randrange
from random import choice

from discord.ext import commands

# magic user spells
# remember everyone starts with Read Magic so reroll on
LOTFPCoreMU1Spells = ["Bookspeak", "Charm Person", "Comprehend Languages / Obscure Languages", "Detect Magic",
                     "Detect Magic", "Enlarge / Reduce", "Faerie Fire", "Feather Fall", "Floating Disc",
                     "Hold Portal", "Identify", "Light / Darkness", "Magic Aura / Obscure Aura", "Magic Missile",
                     "Mending", "Message", "Shield", "Sleep", "Spider Climb", "Summon", "Unseen Servant"]

DND3P5CoreWZ1Spells = []

DND5CoreWZ1Spells = ["Alarm", "Burning Hands", "Charm Person", "Chromatic Orb", "Color Spray", "Comprehend Languages",
                    "Detect Magic", "Disguise Self", "Expeditious Retreat", "False Life", "Feather Fall",
                    "Find Familiar", "Fog Cloud", "Grease", "Identify", "Illusory Script", "Jump", "Longstrider",
                    "Mage Armor", "Magic Missile", "Protection from Evil and Good", "Ray of Sickness", "Shield",
                    "Silent Image", "Sleep", "Tasha's Hideous Laughter", "Tenser's Floating Disk", "Thuderwave",
                    "Unseen Servant", "Witch Bolt"]

DND5CoreSC1Spells = ""


#
class SpellBookGenerators(commands.Cog):

    # Potentially want option to customize how many spells the player gets, w/ the RAW 3 + Read Magic being default
    @commands.command(name="LOTFPMUSpellBook", aliases=["LamentationsMUSB"])
    async def LOTFPMUSpellBook(self, ctx):
        # Everyone starts with this
        T_Return = "Read Magic, "
        T_DupProt = []
        for i in range(3):
            T_DupProt.append(choice(LOTFPCoreMU1Spells))

        while T_DupProt[0] == T_DupProt[1] or T_DupProt[0] == T_DupProt[2]:
            T_DupProt[0] = choice(LOTFPCoreMU1Spells)

        while T_DupProt[1] == T_DupProt[2]:
            T_DupProt[1] = choice(LOTFPCoreMU1Spells)

        for i in range(3):
            T_Return += T_DupProt[i]
            if i < 3:
                T_Return += ", "
        await ctx.channel.send(T_Return)

    #
    @commands.command(name="DnD5WZSpellBook", aliases=["5eWzSpellBook", "5eWizardSpellBook", "5thWizardSpellBook"])
    async def DnD5WZSpellBook(self, ctx):
        T_Return = ""
        T_DupProt = []
        for i in range(6):
            T_DupProt.append(choice(DND5CoreWZ1Spells))
        for i in range(6):
            T_Return += T_DupProt[i]
            if i < 6:
                T_Return += ", "
        await ctx.channel.send(T_Return)
