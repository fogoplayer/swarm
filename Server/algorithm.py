#main function
import random

virtualLot = []
occupants = []

#Main routine of the algorithm
def main(vLot, occ):
    #Initialize variables
    global virtualLot
    global occupants
    virtualLot = vLot
    occupants = occ
    
    #Print inital virtual lot
    for y in virtualLot:
        printString = ""
        for x in y:
            printString += x.toString()
        print printString
    print occupants                                                             #TODO set up occupants to print relevant properties rather than python gibberish
    print
    
    # Move all cars to their default states, then run algorithm
    tellAllCarsToGo()
    algorithm()
    
    #Print new virtual lot
    for y in virtualLot:
        printString = ""
        for x in y:
            printString += x.toString()
        print printString
    print occupants
    print
    print
    
    #return lot and occupants
    return occupants

#Set default state: all cars advance
def tellAllCarsToGo():
    for occupant in occupants:
        occupant.setGoing(True)

#The core algorithm. Executes recursively until everything is good to go
def algorithm():
    contestedDestinations = findContestedDestinations()
    if(len(contestedDestinations) == 0):
        #TODO Push new lot
        print "All clear!"
    else:
        for dest in contestedDestinations:
            pickWinner(dest)
        #algorithm()

#Scans the occupant array for spots that multiple cars are attempting to access
def findContestedDestinations():
    currentDestinations = []
    contestedDestinations = []
    for occupant in occupants:
        if occupant.isGoing() and (occupant.getDestination() not in currentDestinations) and (occupant.getDestination() not in contestedDestinations):
            currentDestinations.append(occupant.getDestination())
        elif occupant.isGoing() and (occupant.getDestination() in currentDestinations and (occupant.getDestination() not in contestedDestinations)):
            contestedDestinations.append(occupant.getDestination())
    return contestedDestinations

#Prioritizes cars jockeying for position
def pickWinner(destination):
    contestants = virtualLot[destination[0]][destination[1]].getChildren()
    
    #Remve contestants who aren't going
    contestant = 0
    while contestant < (len(contestants)):
        if not returnOccupant(contestants[contestant]).isGoing():
            contestants.pop(contestant)
        else:
            contestant += 1
    
    #Run the 3 tests
    contestants = waitCriteria(contestants)
    if len(contestants) > 1:
        contestants = inLaneCriteria(contestants)
    elif len(contestants) > 1:
        contestants = coinFlipCriteria(contestants)
    return contestants

def waitCriteria(contestants):
    record = 0
    i = 0
    while(i < len(contestants)):
        if returnOccupant(contestants[i]).getWaitedForNCars() < record:
            contestants[i].setGoing(False);
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
            returnOccupant(contestants[i]).setGoing(False);
            contestants.pop(i)
        else:
            i += 1
    return contestants

#Picks randomly between competetors
def coinFlipCriteria(contestants):
    index = random.randint(0,len(contestants)-1)
    for i in contestants:
        if (not i == index):
            contestants[i].setGoing(False);
    return contestants[index]

# takes the virtualLot coordinates passed to it, gets the occupant Id, and uses that to find the occupant in the occupant array
def returnOccupant(array):
    return occupants[virtualLot[array[1]][array[0]].getOccupantID()]