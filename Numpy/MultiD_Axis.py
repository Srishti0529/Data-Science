import numpy as np

# 2D ARRAY
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr)

print(np.sum(arr, axis=0))  # Sum along rows (down each column)
print(np.sum(arr, axis=1))  # Sum along columns (across each row)

# You can access elements using row and column indices.
# Accessing an element
print(arr[1, 2])  # Row index 1, Column index 2 → Output: 6

# You can also use slicing to extract parts of an array:
print(arr[0:2, 1:3])  # Extracts first 2 rows and last 2 columns
# output:[[2 3] [5 6]]


# 3D ARRAY
arr3D = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
    ])

# Output of arr3D.shape is → (depth, rows, columns)
print(arr3D.shape)  # Output: (2, 2, 3) 

# Accessing elements in 3D:

# First sheet, second row, third column
print(arr3D[0, 1, 2])  # Output: 6
print(arr3D[:, 0, :])   # Get the first row from both sheets

# Get all rows of the first column
first_col = arr3D[:,:, 0]
print(first_col)  # Output: [[ 1  4] [ 7 10]]


# Get the first row from each "sheet" in a 3D array
first_rows = arr3D[:, 0, :]
print(first_rows)
# output:[[1 2 3][7 8 9]]
