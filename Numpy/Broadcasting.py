import numpy as np

# Example: Looping Over Arrays in Python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
result = []

# Using a loop to square each element (slow)
for num in arr:
    result.append(num**2)

print(result)  # Output: [1, 4, 9, 16, 25]

# Vectorization: Fixing the Loop Problem
arr = np.array([1, 2, 3, 4, 5])
result = arr**2  # Vectorized operation
print(result)  # Output: [1 4 9 16 25]

# NOTE: SIMD - Single Instruction Multiple Data makes numpy array calculation faster

# Broadcasting: Scaling Arrays Without Extra Memory
arr = np.array([1, 2, 3, 4, 5])
result = arr + 10  # Broadcasting: 10 is added to all elements
print(result)  # Output: [11 12 13 14 15]

arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20, 30])

result = arr1 + arr2  # Element-wise addition
print(result)  # Output: [11 22 33]

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([1, 2, 3])

result = arr1 + arr2  # Broadcasting arr2 across arr1
print(result)
# Output:
# [[2 4 6]
#  [5 7 9]]

# EXAMPLE
import numpy as np

# Simulating a dataset (5 samples, 3 features)
data = np.array([[10, 20, 30], [15, 25, 35], [20, 30, 40], [25, 35, 45], [30, 40, 50]])

# data =
# [[10 20 30]
#  [15 25 35]
#  [20 30 40]
#  [25 35 45]
#  [30 40 50]]

# Calculating mean for each column (feature)
mean = data.mean(axis=0)
# mean = [20. 30. 40.]

# Calculating standard deviation for each column
std = data.std(axis=0)
# std = [7.07106781 7.07106781 7.07106781]

# Normalizing the data using broadcasting
normalized_data = (data - mean) / std

# Step-by-step values:
# Row 1: (10,20,30) -> [-1.4142 -1.4142 -1.4142]
# Row 2: (15,25,35) -> [-0.7071 -0.7071 -0.7071]
# Row 3: (20,30,40) -> [ 0.      0.      0.    ]
# Row 4: (25,35,45) -> [ 0.7071  0.7071  0.7071]
# Row 5: (30,40,50) -> [ 1.4142  1.4142  1.4142]

print(normalized_data)

# Final printed output:
# [[-1.41421356 -1.41421356 -1.41421356]
#  [-0.70710678 -0.70710678 -0.70710678]
#  [ 0.          0.          0.        ]
#  [ 0.70710678  0.70710678  0.70710678]
#  [ 1.41421356  1.41421356  1.41421356]]
