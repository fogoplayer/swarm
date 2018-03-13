#Prbably only being used until Nik commits server files
#(But I don't get how python handles multiple files sooooooo)
import time
import math

#Occupant Class-----------------------------------------------------------------
class Occupant:
    id = "";
    nextInstruction = "";
    waitedForNCars = 0;
    
    def __init__(self, id):
        self.id = id;

#Lot----------------------------------------------------------------------------
virtualLot = [
                [{"blank": "                          "}, {"blank": "                          "}, {"nextCell": None, "blank": "        "}, {"blank": "                          "}                                     ],
                [{"nextCell": [1,1], "occupantId": None}, {"nextCell": [1,2], "occupantId": None}, {"nextCell": [0,3], "occupantId": None}, {"nextCell": [1,3], "occupantId": None}],
                [{"nextCell": [1,0], "occupantId": None}, {"nextCell": [2,0], "occupantId": None}, {"nextCell": [2,3], "occupantId": None}, {"nextCell": [1,3], "occupantId": None}],
                [{"nextCell": [2,0], "occupantId": None}, {"nextCell": [3,0], "occupantId": None}, {"nextCell": [3,3], "occupantId": None}, {"nextCell": [2,3], "occupantId": None}],
                [{"nextCell": [3,0], "occupantId": None}, {"nextCell": [4,0], "occupantId": None}, {"nextCell": [4,3], "occupantId": None}, {"nextCell": [3,3], "occupantId": None}],
                [{"nextCell": [4,0], "occupantId": None}, {"blank": "                          "}, {"blank": "                          "}, {"nextCell": [4,3], "occupantId": None}]
        ];
occupants = []

def initializeLot(array):
        '''Takes an array representing a test lot and populates the virtualLot'''
        arrayIndex = 0
        index = 0;
        for y in virtualLot:
                for x in y:
                        if x.has_key("nextCell") and (x["nextCell"] != None):
                                if (array[arrayIndex]):
                                        x["occupantId"] = index;
                                else:
                                        x["occupantId"] = None;
                                arrayIndex += 1;
                                index += 1;
                        print(str(x) + " " + str(arrayIndex) + " " + str(index))

#Test suite---------------------------------------------------------------------
lotsExecuted = 0.0;

#Generate lots to put into the algorithm
def test(array):
    if len(array) < 3:
        time.sleep(.001)
        test(array + [True]);
        test(array + [False]);
    else:
        #if array is complete, execute algorithm
        runAlgorithm(array)

#Run lots generated by test()
def runAlgorithm(array):
    initializeLot(array);
    #Print out % completion through all permutations and the list of parking space states
    global lotsExecuted;
    i = lotsExecuted
    i += 1
    #print(str(format((i/262144.0 * 100.0), '.6f')) + "%\t" + str(array))

#Run test suite
def runTest():
    startTime = time.time();
    test([]);
    endTime = time.time();
    #print('Time Elapsed: ' + str(endTime - startTime) + " sec (" + str((endTime - startTime)/60) + " min)");