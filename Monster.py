from Creature import Creature


#
class Monster (Creature):

    #
    def __init__(self, _name="", _modifiers=[0, 0, 0, 0, 0, 0], _hitpoints=1):
        #
        Creature.__init__(self, _name, _modifiers, _hitpoints)
