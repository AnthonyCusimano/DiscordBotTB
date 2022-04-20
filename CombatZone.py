

#
class CombatZone:

    #
    def __init__(self, _parent=0):
        self.myParentZone = _parent
        self.myChildZones = []
        self.creaturesWithin = []

