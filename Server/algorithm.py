#main function
import random

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
    for y in newLot:
            printString = ""
            for x in y:
                printString += x.toString()
            print printString

    return newLot


def tellAllCarsToGo():
    for occupant in occupants:
        occupant.setGoing(True)


def algorithm():
    print 'begin algorithm'                                                     #Debug print
    contestedDestinations = findContestedDestinations()
    if(len(contestedDestinations) == 0):
        #TODO Push new lot
        print "All clear!"
    else:
        for dest in contestedDestinations:
            pickWinner(dest)
        #algorithm()
    
def findContestedDestinations():
    currentDestinations = []
    contestedDestinations = []
    for occupant in occupants:
        if occupant.isGoing() and (occupant.getDestination() not in currentDestinations) and (occupant.getDestination() not in contestedDestinations):
            currentDestinations.append(occupant.getDestination())
        elif occupant.isGoing() and (occupant.getDestination() in currentDestinations and (occupant.getDestination() not in contestedDestinations)):
            contestedDestinations.append(occupant.getDestination())
    return contestedDestinations

def pickWinner(destination):
    print 'Picking Winner: ' + str(destination)                                 #debug print
    contestants = virtualLot[destination[0]][destination[1]].getChildren()
    
    #Remve contestants who aren't going
    contestant = 0
    while contestant < (len(contestants)):
        if not returnOccupant(contestants[contestant]).isGoing():
            contestants.pop(contestant)
        else:
            contestant += 1
    
    #Run the 3 tests
    print 'Running tests: ' + str(contestants)                                  #debug print
    contestants = waitCriteria(contestants)
    if len(contestants) > 1:
        contestants = inLaneCriteria(contestants)
    elif len(contestants) > 1:
        contestants = coinFlipCriteria(contestants)
    return contestants

def waitCriteria(contestants):
    print 'Wait: ' + str(contestants)                                           #debug print
    record = 0
    i = 0
    while(i < len(contestants)):
        print str(returnOccupant(contestants[i]).getWaitedForNCars()) + " <? " + str(record)
        if returnOccupant(contestants[i]).getWaitedForNCars() < record:
            contestants.pop(i)
            i -= 1
        i += 1
    return contestants

def inLaneCriteria(contestants):
    print 'Lane: ' + str(contestants)                                           #debug print
    i=0
    while i < len(contestants):
        y = contestants[i][0]
        x = contestants[i][1]
        if not virtualLot[y][x].getIsLane():
            contestants.remove(contestants[i])
        else:
            i += 1
    return contestants
    
def coinFlipCriteria(contestants):#This is still an actual coin flip
    print 'Flip' + str(contestants)                                             #debug print
    i = random.randint(0,len(contestants)-1)
    return contestants[i]

def returnOccupant(array):
    # takes the virtualLot coordinates passed to it, gets the occupant Id, and uses that to find the occupant in the occupant array
    return occupants[virtualLot[array[1]][array[1]].getOccupantID()]