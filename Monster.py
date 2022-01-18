

#
class Monster:

    # default / blank constructor
    def __init__(self):
        self.myName = ""
        self.myAbilityScoreModifiers = [0, 0, 0, 0, 0, 0]

    #
    def __init__(self, _modifiers, _name):
        self.myName = _name
        self.myAbilityScoreModifiers = _modifiers.copy()

    # copy constructor
    # def __init__(self, _monster):
    #    self.myName = _monster.name
    #    self.myAbilityScoreModifiers = _monster.myAbilityScoreModifiers.copy()
