'''import numpy as np
a=[1,2,3,4,5]
arr=np.array(a)
print(arr)

# take size of array from user
size = int(input("Enter the size of the array: "))

# create an empty array of given size
arr = [0] * size

# insert elements into the array
for i in range(size):
    arr[i] = int(input("Enter element " + str(i+1) + ": "))

# print the array in the form of size of array
print("Array of size", size, "is:", arr)'''

import numpy as np
a=[[2,4],[3,6]]
arr=np.array(a)
print("dimensions",arr.shape)