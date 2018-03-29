#Spot Class
class Spot:
    parent = None
    occupantID = None
    children = []
    isLane = False
    
    def __init__(self, parent, children, lane, occupantID):
        self.parent = parent
        self.occupantID = occupantID
        self.children = children
        self.isLane = lane
        
    def getParent(self):
        return self.parent
        
    def getChildren(self):
        return self.children
        
    def setOccupantID(self, occupant):
        self.occupantID = occupant
        
    def getOccupantID(self):
        return self.occupantID
        
    def toString(self):
        return "Parent: " + str(self.parent) + " Children:" + str(self.children) + " Occupant:" + str(self.occupantID) + "\t"
        
    def getIsLane(self):
        return self.isLane