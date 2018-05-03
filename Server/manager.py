from multiprocessing import Process, Manager
from main import Spot

def f(d):
    d[1] += '1'
    d['2'] += 2

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

p1 = Process(target=f, args=(d,))
p2 = Process(target=f, args=(d,))
p1.start()
p2.start()
p1.join()
p2.join()

print("kjlnhwefkljnhsdflknjsglkhseflkjnhsrgolknhseglknhsgrlknhsrglokh")