import numpy as np

print()
arr1= np.array([1, 2, 3])
print("Array, 1-D Matrix: ", arr1)
print("Size: ",arr1.size)
print("Shape: ",arr1.shape)
print()

arr2= np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("MATRIX 3x3: ")
print(arr2)
print("Size: ",arr2.size)
print("Shape: ",arr2.shape)
print()

arr3 = arr1*arr2
print("Arr 1 * Arr 2:")
print(arr3)
print("Size: ",arr3.size)
print("Shape: ",arr3.shape)
print()

arr4 = arr2*5
print("Arr2 * 5:")
print(arr4)
print("Size: ",arr4.size)
print("Shape: ",arr4.shape)
print()

arr5= np.array([
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]],
    [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]
    ]])
print("MATRIX 2-D : ")
print(arr5)
print("Size: ",arr5.size)
print("Shape: ",arr5.shape)
print()