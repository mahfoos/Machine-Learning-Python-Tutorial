import numpy as np

a = np.array([5, 6, 7])
print(a)
print(a[1])  # Print the first position
print(a.ndim)  # Print dimension of the array

a = np.array([[5, 8], [1, 3], [5, 9]])
print(a.ndim)  # Print dimension of the array
print(a.itemsize)  # default 4 size for integer
print(a.dtype)   # Int 32

a = np.array([[5, 8], [1, 3], [5, 9]], dtype=np.float64)  # convert to float data type
print(a.itemsize)  # Flote item size is 8
print(a.shape)


b = np.zeros((3,4))
print(b)
print()
b = np.ones((3,4))
print(b)


b = np.arange(1,5)  # ranging the numpy  [1,2,3,4,5]
print(b)
print()


a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)
print(a.shape)  # Calculating row and column of the array
print(a.reshape(2,3)) # Change the shape of the array it means change
print(a.ravel()) # Convert to basic array style
print(a.min())  # print minimum value
print(a.max()) # print maximum value
print(a.sum()) # total of the values

print(a.sum(axis=0))  # Sum of the column
print(a.sum(axis=1))  # Sum of the row
print(np.sqrt(a))  # Squre root of the each element
print(np.std(a))  # Standerd deviation of the array

print("###############################")

a = np.array([[5, 6], [7, 8]])
b = np.array([[1,4], [4,5]])

print(a + b)

print("####################################")

a = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])
print(a)
print(a[1,2])
print(a[0:2, 2])