from multiprocessing import Process, Manager
from main import Spot

#if __name__ == '__main__':
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

def getLot():
    return d['lot']
    
def setLot(lot):
    d['lot'] = lot
    
def getOccupants():
    return d['occupants']
    
def setOccupants(occupants):
    d['occupants'] = occupants