#main function

virtualLot = []
newLot = []
occupants = []


def mainFunction(vLot, occ):
    global virtualLot
    global occupants
    global newLot
    virtualLot = vLot
    occupants = occ
    newLot = virtualLot
    
    # Move all cars to their default states, starting at exit point
    tellAllCarsToGo()
    algorithm()
    print ""
    for y in newLot:
            printString = ""
            for x in y:
                printString += x.toString()
            print printString

    return newLot


def tellAllCarsToGo():
    for spot in occupants:
        if spot.occupantID != None:
            spot.setGoing(True)


def algorithm():
    contestedDestinations = allClear()
    if(len(contestedDestinations) == 0):
        #TODO Push new lot
        print "All clear!"
    else:
        for dest in contestedDestinations:
            pickWinner(dest)
        algorithm()


def allClear():
    currentDestinations = []
    contestedDestinations = []
    for spot in occupants:
        if spot.isGoing() and (spot.getDestination() not in occupants) and (spot.getDestination not in contestedDestinations):
            currentDestinations.append(spot.getParent())
    print "Contested Destinations: " + str(contestedDestinations)
    return contestedDestinations


def pickWinner(destination):
    contestants = virtualLot[destination[0]][destination[1]].getChildren()
    
    waitCriteria(contestants)
    '''inLaneCriteria(contestants)
    coinFlipCriteria(contestants)'''


def waitCriteria(contestants):
    for contestant in contestants:
        print    # Stub

    
def returnOccupant(array):
    # takes the virtualLot coordinates passed to it, gets the occupant ID, and uses that to find the occupant in the occupant array
    return occupants[virtualLot[array[0]][[array[1]]].getOccupantId()]
