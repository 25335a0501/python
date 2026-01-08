#2D Array Operations Using Numpy Module
import numpy as np
arr=np.array([10,20,30],[40,50,60])
print("Array:",arr)
print("Element at index 2:",arr[2])
arr[2]=60
print("Element after changing at index 2:",arr[2])
print("Sliced Array(1 to 4):",arr[1:4])
fancy_items=[0,2]
fancy_elements=arr[fancy_items]
print("Fancy Indexing[0,2]:",fancy_elements)
