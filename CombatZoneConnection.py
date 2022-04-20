# 0: visual only
# 1: physically connected
# connectionTypes = [0, 1]


#
class CombatZoneConnection:

    #
    def __init__(self, _zoneA=0, _zoneB=0, _type=0):
        self.connectedZones = [_zoneA, _zoneB]
        self.myConnectionType = _type
