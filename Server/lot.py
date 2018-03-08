virtualLot = [
                [{"blank": "                          "}, {"blank": "                          "}, {"nextCell": None, "blank": "        "}, {"blank": "                          "}                                     ],
                [{"nextCell": [1,1], "occupantId": None}, {"nextCell": [1,2], "occupantId": None}, {"nextCell": [0,3], "occupantId": None}, {"nextCell": [1,3], "occupantId": None}],
                [{"nextCell": [1,0], "occupantId": None}, {"nextCell": [2,0], "occupantId": None}, {"nextCell": [2,3], "occupantId": None}, {"nextCell": [1,3], "occupantId": None}],
                [{"nextCell": [2,0], "occupantId": None}, {"nextCell": [3,0], "occupantId": None}, {"nextCell": [3,3], "occupantId": None}, {"nextCell": [2,3], "occupantId": None}],
                [{"nextCell": [3,0], "occupantId": None}, {"nextCell": [4,0], "occupantId": None}, {"nextCell": [4,3], "occupantId": None}, {"nextCell": [3,3], "occupantId": None}],
                [{"nextCell": [4,0], "occupantId": None}, {"blank": "                          "}, {"blank": "                          "}, {"nextCell": [4,3], "occupantId": None}]
        ];
        
def initializeLot(array):
        '''Takes an array representing a test lot and populates the virtualLot'''
        arrayIndex = 0
        index = 0;
        for y in virtualLot:
                for x in y:
                        print(x.has_key("nextCell"));
                        if x.has_key("nextCell") and (x["nextCell"] != None):
                                if (array[arrayIndex]):
                                        x["occupantId"] = index;
                                else:
                                        x["occupantId"] = None;
                                arrayIndex += 1;
                                index += 1;
                        print(str(x) + " " + str(arrayIndex) + " " + str(index))

initializeLot([False,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,False, True])
for i in range(0,6):
        print(virtualLot[i]);
