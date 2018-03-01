import time
import math

i = 0.0

def test(array):
    if len(array) < 18:
        time.sleep(.001)
        test(array + ['T']);
        test(array + ['F']);
    else:
        runAlgorithm(array)

def runAlgorithm(array):
    global i
    i += 1
    print(str(format((i/262144.0 * 100.0), '.6f')) + "%\t" + str(array))

startTime = time.time();
test([]);
endTime = time.time()
print('Time Elapsed: ' + str(endTime - startTime) + " sec (" + str((endTime - startTime)/60) + " min)");