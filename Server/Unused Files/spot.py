#Spot Class
class Spot:
    parent = None
    occupantId = None
    children = []
    isLane = False
    
    def __init__(self, parent, children, lane, occupantId):
        self.parent = parent
        self.occupantId = occupantId
        self.children = children
        self.isLane = lane
        
    def getParent(self):
        return self.parent
        
    def getChildren(self):
        return self.children
        
    def setOccupantId(self, occupant):
        self.occupantId = occupant
        
    def getOccupantId(self):
        return self.occupantId
        
    def toString(self):
        return "Parent: " + str(self.parent) + " Children:" + str(self.children) + " Occupant:" + str(self.occupantId) + "\t"
        
    def getIsLane(self):
        return self.isLane