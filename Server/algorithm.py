#main function

virtualLot=[];
occupants=[]

def mainFunction(vLot, occ):
    global virtualLot
    global occupants
    virtualLot = vLot
    occupants = occ
    newLot = virtualLot
    
    #Move all cars to their default states
    for y in virtualLot:
        for x in virtualLot:
            moveCar()