#Create the virtual lot
virtualLot = [
        ['X',   'X',    0,      'x' ],  #a(0)
        [0,     0,      0,      0   ],  #b(1)
        
        [0,     0,      0,      0   ],  #c()
        [0,     0,      0,      0   ],  #d
        [0,     0,      0,      0   ],  #e
        [0,     'X',    'X',    0   ],  #f
    ]
    
#define spot objects
blank = {}
a2 = {"nextSpot": null} #TODO: I'm still figuring out what to do here
b0 = {"nextCell": virtualLot[1]
#Define the spot class
class spot:
    def __init__(self, row, col, nextCell, occupantId):
        self.row = row;
        self.col = col;
        self.nextCell = nextCell;
        self.occupantId = occupantId;