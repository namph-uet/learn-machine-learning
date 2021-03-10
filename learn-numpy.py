import numpy as np

number_2D = np.array([[4,5,6], [7,8,9]])
print(number_2D)
print(number_2D.shape)
print('----------------------------')

#first row
print('first row: ')
print(number_2D[0])

#last row
print('last row:')
print(number_2D[-1])

#first column
print('first column:')
print(number_2D[:, 0])

#last column
print('last column:')
print(number_2D[:, -1])

#middle column of the matrix 
print('middle column:')

awesome = np.array([
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 4, 5, 8, 9, 0],
    [2, 9, 7, 8, 0, 4, 5],
    [9, 6, 4, 9, 3, 7, 2],
])

print(awesome[:, 1])

#Access the array in the matrix
print(awesome[1:3, 2:4])
print(awesome[0,1])

#Boardcasting

numbers_1D = np.array([1,2,3])
print('------------------------------------')
print(numbers_1D, ' + 3 = ', numbers_1D + 3)
print(numbers_1D, ' -3 3 = ', numbers_1D - 3)
numbers_1D_range = np.arange(10)
print(numbers_1D_range, ' * 10 =', numbers_1D_range * 10)

print('boardcasting with 2D matrix')
numbers_2D_ones = np.ones((10,10))
print(numbers_2D_ones)
print(numbers_2D_ones, ' * 10 = ', numbers_2D_ones * 10)

#Addition 2 arrays of different dimensions
print('Addition 2 arrays of different dimensions')
x = np.array([
    [6,9,10],
    [15,18,20],
])
y = np.array([
    [2],
    [4]
])

#could not be broadcast together with shapes (2,3) (2,)
z = np.array([1,2])
#print(x + z)
