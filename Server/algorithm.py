#main function

virtualLot=[]
newLot = []
occupants=[]

def mainFunction(vLot, occ):
    global virtualLot
    global occupants
    global newLot
    virtualLot = vLot
    occupants = occ
    newLot = virtualLot
    print "Lane is " + str(virtualLot[2][2].isLane)
    
    #Move all cars to their default states, starting at exit point
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
        #print occupant.getDestination()
        if occupant.isGoing() and (occupant.getDestination() not in currentDestinations) and (occupant.getDestination not in contestedDestinations):
            currentDestinations.append(occupant.getDestination())
        elif occupant.getDestination not in contestedDestinations:
            contestedDestinations.append(occupant.getDestination())
    print "Contested Destinations: " + str(contestedDestinations)
    return contestedDestinations
    
def pickWinner(destination):
    #TODO modify so only children who are "going" get added
    contestants = virtualLot[destination[0]][destination[1]].getChildren()
    inLaneCriteria(contestants)
    '''contestants = waitCriteria(contestants)
    if len(contestants) > 1:                                                    #Needs to evaluate length
        contestants = inLaneCriteria(contestants)
    elif len(contestants) > 1:
        contestants = coinFlipCriteria(contestants)'''
    return contestants
    
def coinFlipCriteria(contestants):                                              #This is still an actual coin flip
    import random
    tries = 0
    while tries < 100:
        tries += 1
        '''coin = random(0, 1)
        if coin == 1:
            print('Heads')
        if coin == 2:
            print ('Tails')'''
    total = tries
    return (total)
        
def waitCriteria(contestants):
    nCars = []
    for contestant in contestants:
        nCars += [contestant.getWaitedforNCars()]
    record = 0
    number = 0
    while(number < len(nCars)):
        if nCars[number] < record:
            nCars.pop(number)
            contestants.pop(number)
            number -= 1
        number += 1
        
def inLaneCriteria(contestants):
    print "Contested Destinations: " + str(contestants)
    newContestants = contestants
    contestant=0
    while contestant < len(contestants):
        y = contestants[contestant][0]
        x = contestants[contestant][1]
        print virtualLot[y][x].getIsLane
        if not virtualLot[y][x].getIsLane():
            newContestants.remove(contestants[contestant])
        else:
            contestant += 1
    print newContestants

def returnOccupant(array):
    #takes the virtualLot coordinates passed to it, gets the occupant ID, and uses that to find the occupant in the occupant array
    return occupants[virtualLot[array[0]][[array[1]]].getOccupantId()]