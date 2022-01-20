from Creature import Creature


#
class Monster (Creature):

    #
    def __init__(self, _name, _modifiers=[0, 0, 0, 0, 0, 0]):
        #
        Creature.__init__(_name, _modifiers)
