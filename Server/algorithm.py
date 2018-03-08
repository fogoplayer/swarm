virtualLot = [];
#define spot objects
bk = {}
a3 = {"nextSpot": None} #TODO: I'm still figuring out what to do here
b0 = {"nextCell": [1,1], "occupantId": None}
b1 = {"nextCell": [1,2], "occupantId": None}
b2 = {"nextCell": [0,3], "occupantId": None}
b3 = {"nextCell": [1,3], "occupantId": None}
c0 = {"nextCell": [1,0], "occupantId": None}
c1 = {"nextCell": [2,0], "occupantId": None}
c2 = {"nextCell": [2,3], "occupantId": None}
c3 = {"nextCell": [1,3], "occupantId": None}
d0 = {"nextCell": [2,0], "occupantId": None}
d1 = {"nextCell": [3,0], "occupantId": None}
d2 = {"nextCell": [3,3], "occupantId": None}
d3 = {"nextCell": [2,3], "occupantId": None}
e0 = {"nextCell": [3,0], "occupantId": None}
e1 = {"nextCell": [4,0], "occupantId": None}
e2 = {"nextCell": [4,3], "occupantId": None}
e3 = {"nextCell": [3,3], "occupantId": None}
f0 = {"nextCell": [4,0], "occupantId": None}
f3 = {"nextCell": [4,3], "occupantId": None}

def initializeLot:
        #Create the virtual lot
        virtualLot = [
                [bk,    bk,     a3,     bk],  #a(0)
                [b0,    b1,     b2,     b3],  #b(1)
                
                [c0,    c1,     c2,     c3],  #c(2)
                [d0,    d1,     d2,     d3],  #d(3)
                [e0,    e1,     e2,     e3],  #e(4)
                [f0,    bk,     bk,     f3],  #f(5)
            ]
        
        for i in range(0,6):
                print(virtualLot[i]);