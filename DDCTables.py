import random

#
class DDCTables:

    #
    def luckTable(self):
        T_Roll = random.randrange(1, 31)
        T_Return = ""
        if T_Roll == 1:
            T_Return = "Harsh winter: all attack rolls"
        elif T_Roll == 2:
            T_Return = "The bull: melee attack rolls"
        elif T_Roll == 3:
            T_Return = "Fortunate date: Missile fire attack rolls"
        elif T_Roll == 4:
            T_Return = "Raised by wolves: Unarmed attack rolls"
        elif T_Roll == 5:
            T_Return = "Conceived on horseback: Mounted attack rolls"
        elif T_Roll == 6:
            T_Return = "Born on the battlefield: Damage rolls"
        elif T_Roll == 7:
            T_Return = "Path of the bear: Melee damage rolls"
        elif T_Roll == 8:
            T_Return = "Hawkeye: Missile fire damage rolls"
        elif T_Roll == 9:
            T_Return = "Pack hunter: Attack and damage rolls for 0-level starting weapon"
        elif T_Roll == 10:
            T_Return = "Born under the loom: Skill checks (including thief skills)"
        elif T_Roll == 11:
            T_Return = "Fox’s cunning: Find/disable traps"
        elif T_Roll == 12:
            T_Return = "Four-leafed clover: Find secret doors"
        elif T_Roll == 13:
            T_Return = "Seventh son: Spell checks"
        elif T_Roll == 14:
            T_Return = "The raging storm: Spell damage"
        elif T_Roll == 15:
            T_Return = "Righteous heart: Turn unholy checks"
        elif T_Roll == 16:
            T_Return = "Survived the plague: Magical healing\n" \
                       "(If a cleric, applies to all healing the cleric performs. If not a cleric, applies to all " \
                       "magical healing received from other sources)"
        elif T_Roll == 17:
            T_Return = "Lucky sign: Saving throws"
        elif T_Roll == 18:
            T_Return = "Guardian angel: Savings throws to escape traps"
        elif T_Roll == 19:
            T_Return = "Survived a spider bite: Saving throws against poison"
        elif T_Roll == 20:
            T_Return = "Struck by lightning: Reflex saving throws"
        elif T_Roll == 21:
            T_Return = "Lived through famine: Fortitude saving throws"
        elif T_Roll == 22:
            T_Return = "Resisted temptation: Willpower saving throws"
        elif T_Roll == 23:
            T_Return = "Charmed house: Armor Class"
        elif T_Roll == 24:
            T_Return = "Speed of the cobra: Initiative"
        elif T_Roll == 25:
            T_Return = "Bountiful harvest: Hit points (applies at each level)"
        elif T_Roll == 26:
            T_Return = "Warrior’s arm: Critical hit tables\n" \
                       "(Luck normally affects critical hits and fumbles. On this result, the " \
                       "modifier is doubled for purposes of crits or fumbles)"
        elif T_Roll == 27:
            T_Return = "Unholy house: Corruption rolls"
        elif T_Roll == 28:
            T_Return = "The Broken Star: Fumbles\n"\
                       "(Luck normally affects critical hits and fumbles. On this result, the " \
                       "modifier is doubled for purposes of crits or fumbles)"
        elif T_Roll == 29:
            T_Return = "Birdsong: Number of languages"
        elif T_Roll == 30:
            T_Return = "Wild child: Speed (each +1/-1 = +5’/-5’ speed)"

        return T_Return
