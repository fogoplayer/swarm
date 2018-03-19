#main function

virtualLot=[];
occupants=[]

def mainFunction(vLot, occ):
    global virtualLot
    global occupants
    virtualLot = vLot
    occupants = occ
    newLot = virtualLot
    
    #Move all cars to their default states, starting at exit point
    moveTreeToDefaultStates([0,2])

def moveTreeToDefaultStates(coordinates):
    x = coordinates[1]
    y = coordinates[0]
    if(virtualLot[y,x].getOccupantID != None):
        moveCar(y,x);
        #TODO Add recursion

def moveCar(childY,childX):
    child = virtualLot[childY,childX]
    parentCoordinates = child.getParent()
    parentY = parentCoordinates[0]
    parentX = parentCoordinates[1]
    if virtualLot[parentY,parentX].getOccupantID == None:
        virtualLot[parentY,parentX].setOccupantID(child.getOccupantID)
        #TODO detect if two cars are trying to get to the same spot
    