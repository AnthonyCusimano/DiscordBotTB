

#
class Creature:

    #
    def __init__(self, _name, _modifiers, _hitpoints):
        self.myName = _name
        self.myAbilityScoreModifiers = _modifiers.copy()
        self.myHitPoints = _hitpoints
