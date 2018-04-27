import math

latFactor = 364267.2
lonFactor = math.cos(42.3461949) * 363058.08
hor = []
vert = []

def createLot(lat, lon):
    global hor
    global vert
    
    #Lat gets smaller from L to R
    hor += [lon]
    hor += [hor[len(hor)-1] + (22                 / lonFactor)]
    hor += [hor[len(hor)-1] + (19 + 4.5 / 2 / 12) / lonFactor]
    hor += [hor[len(hor)-1] + (19 + 4.5 / 2 / 12) / lonFactor]
    hor += [hor[len(hor)-1] + (22                 / lonFactor)]
    
    #Vertical lot starts from vLot[1], not 0
    #Lon get smaller from T to B
    vert += [lat]
    vert += [vert[0] + (22                 / lonFactor)]
    vert += [vert[len(vert)-1] - (10 + 4.5 / 2 / 12) / latFactor]
    vert += [vert[len(vert)-1] - (10 + 4.5 / 2 / 12) / latFactor]
    vert += [vert[len(vert)-1] - (10 + 4.5 / 2 / 12) / latFactor]
    vert += [vert[len(vert)-1] - (10 + 4.5 / 2 / 12) / latFactor]

    print hor
    print vert

def distBetween(lat1, lon1, lat2, lon2):
    print "Latitude distance: " + str(latFactor*(lat1-lat2))
    latDist = latFactor*(lat1-lat2)
    print "Longitude distance: " + str(lonFactor*(lon1-lon2))
    lonDist = lonFactor*(lon1-lon2)
    print math.sqrt(math.pow( latDist, 2) + math.pow( lonDist, 2))
    print
    
def getVlotCoordinates(lat,lon):
    v = -1
    h = -1
    for i in range(0,len(vert)-1):
        if lat < vert[i]:
            v = i
            
    for i in range(0,len(hor)-1):
        if lat < hor[i]:
            v = i
            
    return [v, h]

createLot(42.3461563,-83.491915);
#TODO why is the distance so bad?