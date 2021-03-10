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