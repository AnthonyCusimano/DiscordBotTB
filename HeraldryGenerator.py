from random import choice, randint
# TODO DB time
colourShades = ["pale", "light", "dark", "blackened"]

colours = ["green", "purple", "yellow", "black", "red", "blue", "indigo"]
# probably just make it str() and have "many" show up toward the end
# cultural numbers
# chargeNumbers = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "many"]

inanimateCharges = ["moon", "lightning bolt", "star*", "closed gauntleted fist", \
                    "gauntleted fist with it's first finger pointing down", \
                    "gauntleted fist with it's first finger pointing up"]

mammalCharges = ["lion", "wolf", "dog"]
mammalChargeModifiers = ["pouncing", "running"]

aquaticCharges = ["squid", "trout", "snail shell", "clam shell", "seagull"]
toolCharges = ["sword", "shovel", "dagger", "spear", "shield"]
winterCharges = ["snowflake*", "evergreen tree"]
treeCharges = ["oak tree", "palm tree"]

avianCharges = ["eagle", "falcon"]
avianChargeModifiers = ["soaring ", "perched "]

# TODO unused
epicCharges = ["kraken", "dragon"]

# TODO field & design changes


# TODO
# https://awoiaf.westeros.org/index.php/Heraldry
class HeraldryGenerator:

    ourChargeColour = ""

    #
    def __init__(self):
        print("HeraldryGenerator constructor called")

    #
    def createField(self):

        T_Return = ""

        # field modifier
        T_Rando = randint(1, 16)
        # DEBUG
        # T_Rando = 16

        # TODO
        # orle should usually but not always match the charge's colour
        if T_Rando == 16:
            T_Return += "framed by a "

            T_Return += HeraldryGenerator.ourChargeColour
            T_Return += " orle "

        T_Return += "on a "
        T_Rando = randint(1, 4)

        if T_Rando == 4:
            T_Return += choice(colourShades) + " "

        T_ColourChoice = choice(colours)

        while T_ColourChoice == HeraldryGenerator.ourChargeColour:
            print("blocking a bad colour choice, the choices were " + T_ColourChoice + " " +
                  HeraldryGenerator.ourChargeColour)
            T_ColourChoice = choice(colours)

        T_Return += T_ColourChoice + " "

        T_Return += "Field."

        return T_Return

    # TODO
    # currently begins all charges with "A ", even when "An " would be more appropriate
    # also the "A " is spaghetti
    def createCharge(self):
        HeraldryGenerator.ourChargeColour = choice(colours)

        T_ChargeType = randint(0, 6)
        # T_ChargeType = 6

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
        elif T_ChargeType == 6:
            T_Extra = randint(0, 4)
            T_Extra = 4
            if T_Extra == 4:
                T_Charge += "A " + choice(avianChargeModifiers) + HeraldryGenerator.ourChargeColour + " " + choice(avianCharges) + " "
                return T_Charge
            else:
                T_Charge = " " + choice(avianCharges)

        # sides check
        if T_Charge[-1] == '*':
            # removing the identifier for multiple sides
            T_Charge = T_Charge[0:-1]
            T_Sides = str(randint(3, 11)) + " sided "
            T_Return = "A " + T_Sides + HeraldryGenerator.ourChargeColour + " " + T_Charge + " "
            return T_Return

        T_Return = "A " + HeraldryGenerator.ourChargeColour + T_Charge + " "
        return T_Return

    def createHeraldry(self):

        T_Return = self.createCharge()
        T_Return += self.createField()

        return T_Return

    # marshals / colour inversions & quartering
    def createPersonalCoatOfArms(self):
        return "Unused method"
