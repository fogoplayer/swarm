virtualLot = [
                [{}                                     , {}                                     , {"nextCell": None}                     , {}                                     ],
                [{"nextCell": [1,1], "occupantId": None}, {"nextCell": [1,2], "occupantId": None}, {"nextCell": [0,3], "occupantId": None}, {"nextCell": [1,3], "occupantId": None}],
                [{"nextCell": [1,0], "occupantId": None}, {"nextCell": [2,0], "occupantId": None}, {"nextCell": [2,3], "occupantId": None}, {"nextCell": [1,3], "occupantId": None}],
                [{"nextCell": [2,0], "occupantId": None}, {"nextCell": [3,0], "occupantId": None}, {"nextCell": [3,3], "occupantId": None}, {"nextCell": [2,3], "occupantId": None}],
                [{"nextCell": [3,0], "occupantId": None}, {"nextCell": [4,0], "occupantId": None}, {"nextCell": [4,3], "occupantId": None}, {"nextCell": [3,3], "occupantId": None}],
                [{"nextCell": [4,0], "occupantId": None}, {}                                     , {}                                     , {"nextCell": [4,3], "occupantId": None}]
        ];
        
def initializeLot(array):
        arrayIndex = 0
        index = 0;
        for y in virtualLot:
                for x in y:
                        print(x);
                        #TODO If statement is never entered
                        if x.has_key('nextCell') and (x.nextCell != None):
                                if (array[arrayIndex]):
                                        x.occupantId = index;
                                arrayIndex += 1;
                                index += 1;
                        print(str(x) + " " + str(arrayIndex) + " " + str(index))

initializeLot([True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,False])
for i in range(0,6):
        print(virtualLot[i]);