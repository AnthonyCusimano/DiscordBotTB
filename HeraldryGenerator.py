from random import choice, randint
# TODO DB time
colourShades = ["pale", "light", "", "dark", "blackened"]

colours = ["green", "purple", "yellow", "black", "red", "blue"]
# probably just make it str() and have "many" show up toward the end
# cultural numbers
chargeNumbers = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "many"]

inanimateCharges = ["moon", "lightning bolt", "star*"]
mammalCharges = ["lion", "wolf", "dog"]
aquaticCharges = ["squid", "trout", "snail shell", "clam shell", "seagull"]
toolCharges = ["sword", "shovel", "dagger", "spear", "shield"]
winterCharges = ["snowflake*", "evergreen tree"]
treeCharges = ["oak tree", "palm tree"]
# TODO unused
avianCharges = ["eagle"]
epicCharges = ["kraken", "dragon", "direwolf"]

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
        T_Colour = choice(colours)

        T_ChargeType = randint(0, 5)

        T_Charge = " "
        if T_ChargeType == 0:
            T_Charge += choice(inanimateCharges)
        elif T_ChargeType == 1:
            T_Charge += choice(mammalCharges)
        elif T_ChargeType == 2:
            T_Charge += choice(aquaticCharges)
        elif T_ChargeType == 3:
            T_Charge += choice(toolCharges)
        elif T_ChargeType == 4:
            T_Charge += choice(winterCharges)
        elif T_ChargeType == 5:
            T_Charge += choice(treeCharges)
        print(T_ChargeType)
        print(T_Charge)

        # T_Charge = choice(modularSideCharges)
        T_Sides = ""

        # sides check
        if T_Charge[-1] == '*':
            # removing the identifier for multiple sides
            T_Charge = T_Charge[0:-1]
            T_Siderando = randint(3, 11)
            T_Sides += " " + str(T_Siderando) + " sided"

        T_Return = T_Colour + T_Sides + T_Charge + " "
        return T_Return

    def createHeraldry(self):
        T_Return = self.createCharge()
        T_Return += self.createField()

        return T_Return
