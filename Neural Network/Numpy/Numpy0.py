import numpy as np
import time
import sys

# Testing the memory
list = range(1000)  # creating list    # i object = 14 bytes
print(sys.getsizeof(5) * len(list))

array = np.array(1000)  # Creating numpy array  # 1 element 4 bytes
print(array.size * array.itemsize)  # array.itemsize is one element & array.size is total size of array

# Testing the time
SIZE = 1000000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# Python list
start = time.time()
result = [ (x + y) for x, y in zip(l1,l2)]
print("Python list took : ", (time.time() - start) * 1000)

# Numpy
start = time.time()
result = a1 + a2
print("Numpy took: ", (time.time()-start) * 1000)

# Numpy calculations

a1 = np.array([1,2,3])
a2 = np.array([5,4,7])
print(a1 + a2)
print(a1 - a2)
print(a1 * a2)
print(a1 / a2)