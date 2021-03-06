# Prbably only being used until Nik commits server files
# (But I don't get how python handles multiple files sooooooo)
import time
import math
import algorithm as a

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
        return str(self.getOccupantID())
    
    def getIsLane(self):
        return self.isLane
        
# Occupant Class-----------------------------------------------------------------
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
        
    def __repr__(self):
        return str(self.isGoing())

def initializeLot(array):
        '''Takes an array representing a test lot and populates the virtualLot'''
        arrayIndex = 0
        index = 0
        global virtualLot
        global occupants
        occupants = []
        virtualLot = [
                [Spot(None , [None]       ,False , None), Spot(None , [None] ,True , None), Spot(None , [[1,2]]      ,True , None),  Spot(None , [None]       ,False , None)],
                [Spot([1,1], [[2,0]]      ,True , None), Spot([1,2], [[1,0]],False , None), Spot([0,2], [[1,1],[1,3]],True , None),  Spot([1,3], [[2,3]]      ,True , None)],
                [Spot([1,0], [[3,0],[2,1]],True , None), Spot([2,0], [None] ,False , None), Spot([2,3], [None]       ,False , None), Spot([1,3], [[3,3],[2,2]],True , None)],
                [Spot([2,0], [[4,0],[3,1]],True , None), Spot([3,0], [None] ,False , None), Spot([3,3], [None]       ,False , None), Spot([2,3], [[4,3],[3,2]],True , None)],
                [Spot([3,0], [[5,0],[4,1]],True , None), Spot([4,0], [None] ,False , None), Spot([4,3], [None]       ,False , None), Spot([3,3], [[5,3],[4,2]],True , None)],
                [Spot([4,0], [None]       ,True , None), Spot(None , [None] ,False , None), Spot(None , [None]       ,False , None), Spot([4,3], [None]       ,True , None)]
        ]
        for y in virtualLot:
            for x in y:
                if x.getParent() != None:
                    if (array[arrayIndex]):
                            x.setOccupantID(index)
                            occupants += [Occupant("blue", "sedan", x.getParent())]
                            index += 1
                    else:
                            x.setOccupantID(None)
                    arrayIndex += 1
                    
        '''for y in virtualLot:
            printString = ""
            for x in y:
                printString += x.toString()
            print printString'''


# Test suite---------------------------------------------------------------------
lotsExecuted = 0.0


# Generate lots to put into the algorithm
def test(array):
    if len(array) < 18:
        time.sleep(.001)
        test(array + [True])
        test(array + [False])
    else:
        # if array is complete, execute algorithm
        runAlgorithm(array)
        # time.sleep(1)


# Run lots generated by test()
def runAlgorithm(array):
    initializeLot(array)
    a.main(virtualLot, occupants)
    # Print out % completion through all permutations and the list of parking space states
    global lotsExecuted
    lotsExecuted += 1
    print(str(format((lotsExecuted/262144.0 * 100.0), '.6f')) + "%\t Combination " + str(lotsExecuted) + "\t" + str(array) + "\n")


# Run test suite
def runTest():
    startTime = time.time()
    test([])
    endTime = time.time()
    print('Time Elapsed: ' + str(endTime - startTime) + " sec (" + str((endTime - startTime)/60) + " min)")
