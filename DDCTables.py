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
            T_Return = T_Return.format(occupation="Cooper", weapon="Crowbar (as club)", tradeGood="barrel")
        elif T_Roll == 15:
            T_Return = T_Return.format(occupation="Costermonger", weapon="Knife (as dagger)", tradeGood="fruit")
        elif T_Roll == 16:
            T_Return = T_Return.format(occupation="Cutpurse", weapon="Dagger", tradeGood="Small chest")
        elif T_Roll == 17:
            T_Return = T_Return.format(occupation="Ditch digger", weapon="Shovel (as staff)",
                                       tradeGood="Fine dirt, 1 lb.")
        elif T_Roll == 18:
            T_Return = T_Return.format(occupation="Dock worker", weapon="Pole (as staff)", tradeGood="1 late RPG book")
        elif T_Roll == 19:
            T_Return = T_Return.format(occupation="Dwarven apothecarist",
                                       weapon="Cudgel (as staff)", tradeGood="Steel vial")
        elif T_Roll == 20:
            T_Return = T_Return.format(occupation="Dwarven blacksmith",
                                       weapon="Hammer (as club)", tradeGood="Mithril, 1 oz.")
        elif T_Roll == 21:
            T_Return = T_Return.format(occupation="Dwarven chest-maker",
                                       weapon="Chisel (as dagger)", tradeGood="Wood, 10 lbs.")
        elif T_Roll == 22:
            T_Return = T_Return.format(occupation="Dwarven herder", weapon="Staff",
                                       tradeGood="Sow\n (if the party includes more than one farmer or herder, "
                                                 "randomly determine the second and subsequent farm animals for "
                                                 "each duplicated profession with 1d6: "
                                                 "(1) sheep, (2) goat, (3) cow, (4) duck, (5) goose, (6) mule")
        elif T_Roll == 23 or T_Roll == 24:
            T_Return = T_Return.format(occupation="Dwarven miner", weapon="pick (as club)", tradeGood="lantern")
        elif T_Roll == 25:
            T_Return = T_Return.format(occupation="Dwarven mushroom-farmer", weapon="Shovel (as staff)",
                                       tradeGood="Sack")
        elif T_Roll == 26:
            T_Return = T_Return.format(occupation="Dwarven rat-catcher", weapon="Club", tradeGood="Net")
        elif T_Roll == 27 or T_Roll == 28:
            T_Return = T_Return.format(occupation="Dwarven stonemason", weapon="Hammer",
                                       tradeGood="Fine stone, 10 lbs.")
        elif T_Roll == 29:
            T_Return = T_Return.format(occupation="Elven artisan", weapon="Staff", tradeGood="Clay, 1 lb.")
        elif T_Roll == 30:
            T_Return = T_Return.format(occupation="Elven barrister", weapon="Quill (as dart)", tradeGood="Book")
        elif T_Roll == 31:
            T_Return = T_Return.format(occupation="Elven chandler", weapon="Scissors (as dagger)",
                                       tradeGood="Candles, 20")
        elif T_Roll == 32:
            T_Return = T_Return.format(occupation="Elven falconer", weapon="Dagger", tradeGood="Falcon")
        elif T_Roll == 33 or T_Roll == 34:
            T_Return = T_Return.format(occupation="Elven forester", weapon="Staff", tradeGood="Herbs, 1 lb.")
        elif T_Roll == 35:
            T_Return = T_Return.format(occupation="Elven glassblower", weapon="Hammer (as club)",
                                       tradeGood="Glass beads")
        elif T_Roll == 36:
            T_Return = T_Return.format(occupation="Elven navigator", weapon="Shortbow", tradeGood="Spyglass")
        elif T_Roll == 37 or T_Roll == 38:
            T_Return = T_Return.format(occupation="Elven sage", weapon="Dagger", tradeGood="Parchment and quill pen")
        elif 48 > T_Roll > 38:
            T_Return = T_Return.format(occupation="Farmer", weapon="Pitchfork (as spear)",
                                       tradeGood="Hen\n(if the party includes more than one farmer or herder, "
                                                 "randomly determine the second and subsequent farm animals for "
                                                 "each duplicated profession with 1d6: "
                                                 "(1) sheep, (2) goat, (3) cow, (4) duck, (5) goose, (6) mule")
        elif T_Roll == 48:
            T_Return = T_Return.format(occupation="Fortune-teller", weapon="Dagger", tradeGood="Tarot deck")
        elif T_Roll == 49:
            T_Return = T_Return.format(occupation="Gambler", weapon="Club", tradeGood="Dice")
        elif T_Roll == 50:
            T_Return = T_Return.format(occupation="Gongfarmer", weapon="Trowel (as dagger)",
                                       tradeGood="Sack of night soil")
        elif T_Roll == 51 or T_Roll == 52:
            T_Return = T_Return.format(occupation="Grave digger", weapon="Shovel (as staff)", tradeGood="Trowel")
        elif T_Roll == 53 or T_Roll == 54:
            T_Return = T_Return.format(occupation="Guild beggar", weapon="Sling", tradeGood="Crutches")
        elif T_Roll == 55:
            T_Return = T_Return.format(occupation="Halfling chicken butcher", weapon="Hand axe",
                                       tradeGood="Chicken meat, 5 lbs.")
        elif T_Roll == 56 or T_Roll == 57:
            T_Return = T_Return.format(occupation="Halfling dyer", weapon="Staff", tradeGood="Fabric, 3 yards")
        elif T_Roll == 58:
            T_Return = T_Return.format(occupation="Halfling glovemaker", weapon="Awl (as dagger)",
                                       tradeGood="Gloves, 4 pairs")
        elif T_Roll == 59:
            T_Return = T_Return.format(occupation="Halfling gypsy", weapon="Sling", tradeGood="Hex doll")
        elif T_Roll == 60:
            T_Return = T_Return.format(occupation="Halfling haberdasher", weapon="Scissors (as dagger)",
                                       tradeGood="Fine suits, 3 sets")
        elif T_Roll == 61:
            T_Return = T_Return.format(occupation="Halfling mariner", weapon="Knife (as dagger)",
                                       tradeGood="Sailcloth, 2 yards")
        elif T_Roll == 62:
            T_Return = T_Return.format(occupation="Halfling moneylender", weapon="Short sword",
                                       tradeGood="5 gp, 10 sp, 200 cp")
        elif T_Roll == 63:
            T_Return = T_Return.format(occupation="Halfling trader", weapon="Short sword", tradeGood="20 sp")
        elif T_Roll == 64:
            T_Return = T_Return.format(occupation="Halfling vagrant", weapon="Club", tradeGood="Begging bowl")
        elif T_Roll == 65:
            T_Return = T_Return.format(occupation="Healer", weapon="Club", tradeGood="Holy water, 1 vial")
        elif T_Roll == 66:
            T_Return = T_Return.format(occupation="Herbalist", weapon="Club", tradeGood="Herbs, 1 lb.")
        elif T_Roll == 67:
            T_Return = T_Return.format(occupation="Herder", weapon="Staff",
                                       tradeGood="Herding dog\n (if the party includes more than one farmer or "
                                                 "herder, randomly determine the second and subsequent farm animals "
                                                 "for each duplicated profession with 1d6:"
                                                 "(1) sheep, (2) goat, (3) cow, (4) duck, (5) goose, (6) mule)")
        elif T_Roll == 68 or T_Roll == 69:
            T_Return = T_Return.format(occupation="Hunter", weapon="Shortbow", tradeGood="Deer pelt")
        elif T_Roll == 70:
            T_Return = T_Return.format(occupation="Indentured servant", weapon="Staff", tradeGood="Locket")
        elif T_Roll == 71:
            T_Return = T_Return.format(occupation="Jester", weapon="Dart", tradeGood="Silk clothes")
        elif T_Roll == 72:
            T_Return = T_Return.format(occupation="Jeweler", weapon="Dagger", tradeGood="Gem worth 20 gp")
        elif T_Roll == 73:
            T_Return = T_Return.format(occupation="Locksmith", weapon="Dagger", tradeGood="Fine tools")
        elif T_Roll == 74:
            T_Return = T_Return.format(occupation="Mendicant", weapon="Club", tradeGood="Cheese drip")
        elif T_Roll == 75:
            T_Return = T_Return.format(occupation="Mercenary", weapon="Longsword", tradeGood="Hide armor")
        elif T_Roll == 76:
            T_Return = T_Return.format(occupation="Merchant", weapon="Dagger", tradeGood="4 gp, 14 sp, 27 cp")
        elif T_Roll == 77:
            T_Return = T_Return.format(occupation="Miller/baker", weapon="Club", tradeGood="Flour, 1 lb.")
        elif T_Roll == 78:
            T_Return = T_Return.format(occupation="Minstrel", weapon="Dagger", tradeGood="Ukulele")
        elif T_Roll == 79:
            T_Return = T_Return.format(occupation="Noble", weapon="Longsword", tradeGood="Gold ring worth 10 gp")
        elif T_Roll == 80:
            T_Return = T_Return.format(occupation="Orphan", weapon="Club", tradeGood="Rag doll")
        elif T_Roll == 81:
            T_Return = T_Return.format(occupation="Ostler", weapon="Staff", tradeGood="Bridle")
        elif T_Roll == 82:
            T_Return = T_Return.format(occupation="Outlaw", weapon="Short sword", tradeGood="Leather armor")
        elif T_Roll == 83:
            T_Return = T_Return.format(occupation="Rope maker", weapon="Knife (as dagger)", tradeGood="Rope, 100’")
        elif T_Roll == 84:
            T_Return = T_Return.format(occupation="Scribe", weapon="Dart", tradeGood="Parchment, 10 sheets")
        elif T_Roll == 85:
            T_Return = T_Return.format(occupation="Shaman", weapon="Mace", tradeGood="Herbs, 1 lb.")
        elif T_Roll == 86:
            T_Return = T_Return.format(occupation="Slave", weapon="Club", tradeGood="Strange-looking rock")
        elif T_Roll == 87:
            T_Return = T_Return.format(occupation="Smuggler", weapon="Sling", tradeGood="Waterproof sack")
        elif T_Roll == 88:
            T_Return = T_Return.format(occupation="Soldier", weapon="Spear", tradeGood="Shield")
        elif T_Roll == 89 or T_Roll == 90:
            T_Return = T_Return.format(occupation="Squire", weapon="Longsword", tradeGood="Steel helmet")
        elif T_Roll == 91:
            T_Return = T_Return.format(occupation="Tax collector", weapon="Longsword", tradeGood="100 cp")
        elif T_Roll == 92 or T_Roll == 93:
            T_Return = T_Return.format(occupation="Trapper", weapon="Sling", tradeGood="Badger pelt")
        elif T_Roll == 94:
            T_Return = T_Return.format(occupation="Urchin", weapon="Stick (as club)", tradeGood="Begging bowl")
        elif T_Roll == 95:
            T_Return = T_Return.format(occupation="Wainwright", weapon="Club",
                                       tradeGood="Pushcart\nRoll 1d6 to determine what’s in the "
                                                 "cart: (1) tomatoes, (2) nothing, (3) straw, (4) your dead, "
                                                 "(5) dirt, (6) rocks.")
        elif T_Roll == 96:
            T_Return = T_Return.format(occupation="Weaver", weapon="Dagger", tradeGood="Fine suit of clothes")
        elif T_Roll == 97:
            T_Return = T_Return.format(occupation="Wizard’s apprentice", weapon="Dagger", tradeGood="Black grimoire")
        elif T_Roll > 97:
            T_Return = T_Return.format(occupation="Woodcutter", weapon="Handaxe", tradeGood="Bundle of wood")

        return T_Return
