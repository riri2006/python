import numpy as np

#created array
arr1 = np.array([1,2,3,4])
arr2 = np.array([2,5,6,1])
#operations on array
print(arr1) 
print(arr1*5) #multiplying array with a number
print(arr1+10) #adding array to any number
print(arr1+arr2) #addition of 2 arrays
print(arr1*arr2) #multiplying 2 arrays
print()
#zero matrix
print(np.zeros((4,4)))
print()
#1s matrix
print(np.ones((3,3)))
print()
#identity matrix 
print(np.eye(3))
print()

#arange- specific gaps m numbers lena just like range in python
print(np.arange(0,100,10))

#linspace - specific number of values print krna which will be equally ditanced from each other
print(np.linspace(1,500,5))

#type:
print(type(np.linspace(1,10,3)))