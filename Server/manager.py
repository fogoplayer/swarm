from multiprocessing import Manager


# Spot Class
class Spot:
    print("spot")
    parent = None
    occupantID = None
    children = []
    isLane = False

    def __init__(self, parent, children, lane, occupantID):
        self.parent = parent
        self.occupantID = occupantID
        self.children = children
        self.isLane = lane

    def getParent(self):
        return self.parent

    def getChildren(self):
        return self.children

    def setOccupantID(self, occupant):
        self.occupantID = occupant

    def getOccupantID(self):
        return self.occupantID

    def toString(self):
        return str(self.getOccupantID())

    def getIsLane(self):
        return self.isLane


print("Before if __name__ == ""Server.manager....... __name__ = " + __name__)
if __name__ == "Server.manager":
    print("Manager thing running")
    manager = Manager()
    d = {'lot': [], 'occupants': []}
    d = manager.dict()
    print("Name: " + __name__)
    print("Name is 'Server.manager': " + str(__name__))

    Manager.__dict__['lot'] = [
        [Spot(None, [None], False, None), Spot(None, [None], True, None), Spot(None, [[1, 2]], True, None),
         Spot(None, [None], False, None)],
        [Spot([1, 1], [[2, 0]], True, None), Spot([1, 2], [[1, 0]], False, None),
         Spot([0, 2], [[1, 1], [1, 3]], True, None), Spot([1, 3], [[2, 3]], True, None)],
        [Spot([1, 0], [[3, 0], [2, 1]], True, None), Spot([2, 0], [None], False, None),
         Spot([2, 3], [None], False, None), Spot([1, 3], [[3, 3], [2, 2]], True, None)],
        [Spot([2, 0], [[4, 0], [3, 1]], True, None), Spot([3, 0], [None], False, None),
         Spot([3, 3], [None], False, None), Spot([2, 3], [[4, 3], [3, 2]], True, None)],
        [Spot([3, 0], [[5, 0], [4, 1]], True, None), Spot([4, 0], [None], False, None),
         Spot([4, 3], [None], False, None), Spot([3, 3], [[5, 3], [4, 2]], True, None)],
        [Spot([4, 0], [None], True, None), Spot(None, [None], False, None), Spot(None, [None], False, None),
         Spot([4, 3], [None], True, None)]
    ]
    print("vlot initalized........vlot = " + str(Manager.__dict__['lot']))
    Manager.__dict__['occupants'] = []


def getLot():
    print("** GET LOT CALLED **")
    if d['lot'] is not None:
        print("d['lot'] = " + str(Manager.d['lot']))
        return Manager.d['lot']
    else:
        print("d['lot'] has nothing in it")
        return


d = {'lot': [], 'occupants': []}
print("__name__" + __name__)
manager = Manager()
d = manager.dict()
d['lot'] = [
            [Spot(None , [None]       ,False , None), Spot(None , [None] ,True , None), Spot(None , [[1,2]]      ,True , None),  Spot(None , [None]       ,False , None)],
            [Spot([1,1], [[2,0]]      ,True , None), Spot([1,2], [[1,0]],False , None), Spot([0,2], [[1,1],[1,3]],True , None),  Spot([1,3], [[2,3]]      ,True , None)],
            [Spot([1,0], [[3,0],[2,1]],True , None), Spot([2,0], [None] ,False , None), Spot([2,3], [None]       ,False , None), Spot([1,3], [[3,3],[2,2]],True , None)],
            [Spot([2,0], [[4,0],[3,1]],True , None), Spot([3,0], [None] ,False , None), Spot([3,3], [None]       ,False , None), Spot([2,3], [[4,3],[3,2]],True , None)],
            [Spot([3,0], [[5,0],[4,1]],True , None), Spot([4,0], [None] ,False , None), Spot([4,3], [None]       ,False , None), Spot([3,3], [[5,3],[4,2]],True , None)],
            [Spot([4,0], [None]       ,True , None), Spot(None , [None] ,False , None), Spot(None , [None]       ,False , None), Spot([4,3], [None]       ,True , None)]
            ]
d['occupants'] = []

def setLot(lot):
    Manager.__dict__['lot'] = lot


def getOccupants():
    if Manager.__dict__['occupants'].__sizeof__() != 0:
        print("d['occupants'] = " + str(Manager.__dict__['occupants']))
        return Manager.__dict__['occupants']
    else:
        print("d['occupants'] has nothing in it")
        return
    print("getting occupants")
    return d['occupants']


def setOccupants(occupants):
    Manager.__dict__['occupants'] = occupants
