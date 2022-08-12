from random import choice, randint
# TODO DB time
colourShades = ["pale", "light", "", "dark", "blackened"]

colours = ["green", "purple", "yellow", "black", "red", "blue"]

inanimateCharges = ["moon", "lightning bolt"]
mammalCharges = ["lion", "wolf", "dog"]
aquaticCharges = ["squid", "trout"]
toolCharges = ["sword", "shovel", "dagger", "spear"]
modularSideCharges = ["star", "snowflake"]
treeCharges = ["evergreen tree", "oak tree"]

# TODO field & design changes


# TODO
class HeraldryGenerator:

    #
    def __init__(self):
        """"""""

    def createField(self):
        T_Return = "on a "

        T_Return += choice(colourShades) + " "

        T_Return += choice(colours)
        T_Return += " "

        T_Return += "Field."

        return T_Return

    #
    def createCharge(self):
        T_Return = choice(colours)
        T_Return += " "

        T_ChargeType = randint(0, 5)

        if T_ChargeType == 0:
            T_Return += choice(inanimateCharges)
        elif T_ChargeType == 1:
            T_Return += choice(mammalCharges)
        elif T_ChargeType == 2:
            T_Return += choice(aquaticCharges)
        elif T_ChargeType == 3:
            T_Return += choice(toolCharges)
        elif T_ChargeType == 2:
            T_Return += choice(modularSideCharges)
        elif T_ChargeType == 5:
            T_Return += choice(treeCharges)

        T_Return += " "
        return T_Return

    def createHeraldry(self):
        T_Return = self.createCharge()
        T_Return += self.createField()

        return T_Return
