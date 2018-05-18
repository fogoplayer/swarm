from multiprocessing import Manager


# Spot Class
class Spot:
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
    d = {'lot': [], 'occupants': []}
    print("Name: " + __name__)
    print("Name is 'Server.manager': " + str(__name__))
    manager = Manager()
    d = manager.dict()
    d['lot'] = [
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
    d['occupants'] = []


def getLot():
    if d['lot'] is not None:
        print("d['lot'] = " + str(d['lot']))
        return d['lot']
    else:
        print("d['lot'] has nothing in it")
        return


def setLot(lot):
    d['lot'] = lot


def getOccupants():
    if d['occupants'] is not None:
        print("d['occupants'] = " + str(d['occupants']))
        return d['occupants']
    else:
        print("d['occupants'] has nothing in it")
        return


def setOccupants(occupants):
    d['occupants'] = occupants
