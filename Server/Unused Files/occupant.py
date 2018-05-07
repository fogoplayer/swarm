class Occupant:
    carColor = ""
    carType = ""
    nextInstruction = ""
    destination = []
    going = True
    waitedForNCars = 0
    
    def __init__(self, carColor, carType, dest):
        self.carColor = carColor
        self.carType = carType
        self.destination = dest
    
    def getNextInstruction(self):
        return self.nextInstruction
    
    def setNextInstruction(self, nI):
        self.nextInstruction = nI
        
    def getDestination(self):
        return self.destination
    
    def setDestination(self, dest):
        self.destination = dest
    
    def setGoing(self, tf):
        self.going = tf
    
    def isGoing(self):
        return self.going
        
    def increaseWaitedForNCars(self):
        self.waitedForNCars += 1
        
    def resetWaitedForNCars(self):
        self.waitedForNCars = 0
    
    def getWaitedForNCars(self):
        return self.waitedForNCars
