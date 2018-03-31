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
    print "Lane is " + str(virtualLot[2][2].isLane)
    
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
    for occupant in occupants:
        occupant.setGoing(True)


def algorithm():
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
        print currentDestinations
        if occupant.isGoing() and (occupant.getDestination() not in currentDestinations) and (occupant.getDestination() not in contestedDestinations):
            currentDestinations.append(occupant.getDestination())
        elif occupant.isGoing() and (occupant.getDestination() in currentDestinations and (occupant.getDestination() not in contestedDestinations)):
            contestedDestinations.append(occupant.getDestination())
    print "Contested Destinations: " + str(contestedDestinations)
    return contestedDestinations

def pickWinner(destination):
    #TODO modify so only children who are "going" get added
    contestants = virtualLot[destination[0]][destination[1]].getChildren()
    contestant = 0
    while contestant < (len(contestants)):
        if not returnOccupant(contestants[contestant]).isGoing():
            contestants.pop(contestant)
    contestants = waitCriteria(contestants)
    if len(contestants) > 1:
        contestants = inLaneCriteria(contestants)
    elif len(contestants) > 1:
        contestants = coinFlipCriteria(contestants)
    return contestants

def waitCriteria(contestants):
    '''nCars = []
    for contestant in contestants:
        nCars += [contestant.getWaitedforNCars()]
    record = 0
    i = 0
    while(i < len(nCars)):
        if nCars[i] < record:
            nCars.pop(i)
            contestants.pop(i)
            i -= 1
        i += 1'''
    record = 0
    i = 0
    while(i < len(contestants)):
        print str(returnOccupant(contestants[i]).getWaitedforNCars()) + " <? " + str(record)
        if returnOccupant(contestants[i]).getWaitedforNCars() < record:
            contestants.pop(i)
            i -= 1
        i += 1
    return contestants

def inLaneCriteria(contestants):
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
    i = random.randint(0,len(contestants))
    return contestants[i]

def returnOccupant(array):
    # takes the virtualLot coordinates passed to it, gets the occupant Id, and uses that to find the occupant in the occupant array
    print "Hello " + virtualLot[array[0]][array[1]].toString()                  #HELP Sucessfully returns occupantId as part of user-defiined toString method
    print "Hello " + virtualLot[array[0]][array[1]].getOccupantId()             #HELP Fails to return occupantId as a part of user-defined getOccupantId method
    print "Hello " + virtualLot[array[0]][array[1]].occupantId                  #HELP Fails to return occupantId when directly accessing the attribute of the instance object
    return occupants[virtualLot[array[0]][array[1]].getOccupantId()]            
