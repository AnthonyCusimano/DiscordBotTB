import random


#
class DDCTables:

    #
    def __init__(self):
        print("DDC tables module initiated")

    #
    def luckTable(self):
        T_Roll = random.randrange(1, 31)
        T_Return = "Luck table result: "
        if T_Roll == 1:
            T_Return += "Harsh winter: all attack rolls"
        elif T_Roll == 2:
            T_Return += "The bull: melee attack rolls"
        elif T_Roll == 3:
            T_Return += "Fortunate date: Missile fire attack rolls"
        elif T_Roll == 4:
            T_Return += "Raised by wolves: Unarmed attack rolls"
        elif T_Roll == 5:
            T_Return += "Conceived on horseback: Mounted attack rolls"
        elif T_Roll == 6:
            T_Return += "Born on the battlefield: Damage rolls"
        elif T_Roll == 7:
            T_Return += "Path of the bear: Melee damage rolls"
        elif T_Roll == 8:
            T_Return += "Hawkeye: Missile fire damage rolls"
        elif T_Roll == 9:
            T_Return += "Pack hunter: Attack and damage rolls for 0-level starting weapon"
        elif T_Roll == 10:
            T_Return += "Born under the loom: Skill checks (including thief skills)"
        elif T_Roll == 11:
            T_Return += "Fox’s cunning: Find/disable traps"
        elif T_Roll == 12:
            T_Return += "Four-leafed clover: Find secret doors"
        elif T_Roll == 13:
            T_Return += "Seventh son: Spell checks"
        elif T_Roll == 14:
            T_Return += "The raging storm: Spell damage"
        elif T_Roll == 15:
            T_Return += "Righteous heart: Turn unholy checks"
        elif T_Roll == 16:
            T_Return += "Survived the plague: Magical healing\n" \
                       "(If a cleric, applies to all healing the cleric performs. If not a cleric, applies to all " \
                       "magical healing received from other sources)"
        elif T_Roll == 17:
            T_Return += "Lucky sign: Saving throws"
        elif T_Roll == 18:
            T_Return += "Guardian angel: Savings throws to escape traps"
        elif T_Roll == 19:
            T_Return += "Survived a spider bite: Saving throws against poison"
        elif T_Roll == 20:
            T_Return += "Struck by lightning: Reflex saving throws"
        elif T_Roll == 21:
            T_Return += "Lived through famine: Fortitude saving throws"
        elif T_Roll == 22:
            T_Return += "Resisted temptation: Willpower saving throws"
        elif T_Roll == 23:
            T_Return += "Charmed house: Armor Class"
        elif T_Roll == 24:
            T_Return += "Speed of the cobra: Initiative"
        elif T_Roll == 25:
            T_Return += "Bountiful harvest: Hit points (applies at each level)"
        elif T_Roll == 26:
            T_Return += "Warrior’s arm: Critical hit tables\n" \
                       "(Luck normally affects critical hits and fumbles. On this result, the " \
                       "modifier is doubled for purposes of crits or fumbles)"
        elif T_Roll == 27:
            T_Return += "Unholy house: Corruption rolls"
        elif T_Roll == 28:
            T_Return += "The Broken Star: Fumbles\n"\
                       "(Luck normally affects critical hits and fumbles. On this result, the " \
                       "modifier is doubled for purposes of crits or fumbles)"
        elif T_Roll == 29:
            T_Return += "Birdsong: Number of languages"
        elif T_Roll == 30:
            T_Return += "Wild child: Speed (each +1/-1 = +5’/-5’ speed)"

        return T_Return

    #
    def equipmentTable(self):
        T_Roll = random.randrange(1,25)
        T_Return = "\n Your character has a(n): "

        if T_Roll == 1:
            T_Return += "backpack"
        elif T_Roll == 2:
            T_Return += "candle"
        elif T_Roll == 3:
            T_Return += "chain, 10 feet"
        elif T_Roll == 4:
            T_Return += "chalk, 1 piece"
        elif T_Roll == 5:
            T_Return += "chest, empty"
        elif T_Roll == 6:
            T_Return += "crowbar"
        elif T_Roll == 7:
            T_Return += "flask, empty"
        elif T_Roll == 8:
            T_Return += "flint & steel"
        elif T_Roll == 9:
            T_Return += "grappling hook"
        elif T_Roll == 10:
            T_Return += "hammer, small"
        elif T_Roll == 11:
            T_Return += "holy symbol"
        elif T_Roll == 12:
            T_Return += "holy water, 1 vial (A half-pint vial of holy water inflicts 1d4 damage to any un-dead " \
                        "creature, as well as to some demons and devils.)"
        elif T_Roll == 13:
            T_Return += "Iron spike"
        elif T_Roll == 14:
            T_Return += "Lantern"
        elif T_Roll == 15:
            T_Return += "Mirror, hand-sized"
        elif T_Roll == 16:
            T_Return += "oil, 1 flask " \
                        "When ignited and thrown, oil causes 1d6 damage plus fire " \
                        "(DC 10 save vs. Reflex to put out or suffer additional 1d6 damage each round). " \
                        "One flask of oil burns for 6 hours in a lantern."
        elif T_Roll == 17:
            T_Return += "Pole, 10-foot"
        elif T_Roll == 18:
            T_Return += "Rations, per day"
        elif T_Roll == 19:
            T_Return += "Rope, 50’"
        elif T_Roll == 20:
            T_Return += "Sack, large"
        elif T_Roll == 21:
            T_Return += "Sack, small"
        elif T_Roll == 22:
            T_Return += "Thieves’ tools"
        elif T_Roll == 23:
            T_Return += "Torch"
        elif T_Roll == 24:
            T_Return += "Waterskin"

        return T_Return

    #
    def occupationTable(self):
        T_Roll = random.randrange(1, 101)
        T_Return = "\nYour character is a {occupation} in possession of an {weapon} as a weapon as well as {tradeGood}"

        if T_Roll == 1:
            T_Return = T_Return.format(occupation="alchemist", weapon="staff", tradeGood="oil, 1 flask")
        elif T_Roll == 2:
            T_Return = T_Return.format(occupation="animal trainer", weapon="club", tradeGood="pony")
        elif T_Roll == 3:
            T_Return = T_Return.format(occupation="armorer", weapon="hammer (as club)", tradeGood="iron helmet")
        elif T_Roll == 4:
            T_Return = T_Return.format(occupation="astrologer", weapon="dagger", tradeGood="spyglass")
        elif T_Roll == 5:
            T_Return = T_Return.format(occupation="barber", weapon="razor (as dagger)", tradeGood="scissors")
        elif T_Roll == 6:
            T_Return = T_Return.format(occupation="beadle", weapon="staff", tradeGood="holy symbol")
        elif T_Roll == 7:
            T_Return = T_Return.format(occupation="beekeeper", weapon="staff", tradeGood="jar of honey")
        elif T_Roll == 8:
            T_Return = T_Return.format(occupation="blacksmith", weapon="hammer (as club)", tradeGood="steel tongs")
        elif T_Roll == 9:
            T_Return = T_Return.format(occupation="butcher", weapon="cleaver (as axe)", tradeGood="side of beef")
        elif T_Roll == 10:
            T_Return = T_Return.format(occupation="caravan guard", weapon="short sword", tradeGood="Linen, one yard")
        elif T_Roll == 11:
            T_Return = T_Return.format(occupation="cheesemaker", weapon="cudgel (as staff)", tradeGood="stinky cheese")
        elif T_Roll == 12:
            T_Return = T_Return.format(occupation="cobbler", weapon="awl (as dagger)", tradeGood="shoehorn")
        elif T_Roll == 13:
            T_Return = T_Return.format(occupation="confidence artist", weapon="dagger", tradeGood="quality cloak")
        elif T_Roll == 14:
            T_Return = T_Return.format(occupation="confidence artist", weapon="dagger", tradeGood="quality cloak")

        return T_Return
