import time
import math
import lot

i = 0.0

def test(array):
    #if array is not at full size, keep creating branches using recursion
    #1ms delay to prevent lag
    if len(array) < 3:
        time.sleep(.001)
        test(array.append[True]);
        test(array.append[False]);
    else:
        #if array is complete, execute algorithm
        runAlgorithm(array)

def runAlgorithm(array):
    
    #Print out % completion through all permutations and the list of parking space states
    initializeLot(array);
    global i
    i += 1
    print(str(format((i/262144.0 * 100.0), '.6f')) + "%\t" + str(array))

startTime = time.time();
test([]);
endTime = time.time()
print('Time Elapsed: ' + str(endTime - startTime) + " sec (" + str((endTime - startTime)/60) + " min)");