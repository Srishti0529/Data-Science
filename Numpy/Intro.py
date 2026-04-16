# COMPARING SPEED OF LIST AND NUMPY ARRAY

import numpy as np  # Importing NumPy library and naming it as np
import time  # Importing time module to measure execution speed

# -----------------------------
# PART 1: Using normal Python lists
# -----------------------------

size = 1_000_000  # Creating size = 1,000,000 (1 million elements)

# Making two lists: list1 = [0, 1, 2, ... 999999] and list2 = same
list1 = list(range(size))
list2 = list(range(size))

# Measure time for Python list addition
start = time.time()  # Start the stopwatch

# Add each element of list1 with list2 using a loop (zip)
# Example: If list1 = [1,2,3] and list2 = [4,5,6] → result = [5,7,9]
result = [x + y for x, y in zip(list1, list2)]

end = time.time()  # Stop the stopwatch

print("Python list addition time:", end - start)


# -----------------------------
# PART 2: Using NumPy arrays
# -----------------------------

# Convert normal Python lists into NumPy arrays
# Example: arr1 looks like [0 1 2 ... 999999] but is stored in a faster format
arr1 = np.array(list1)
arr2 = np.array(list2)

start = time.time()  # Start timing NumPy addition

# Vectorized addition: NumPy adds entire arrays at once internally in C
# Example: arr1 + arr2 for [1 2 3] + [4 5 6] → [5 7 9]
result = arr1 + arr2

end = time.time()  # End time

print("NumPy array addition time:", end - start)


# Zip EXPLAINATION
list_1 = [2, 3, 4]
list_2 = [4, 5, 6]
list(zip(list_1, list_2))
# [(2,4),(3,5),(4,6)]


# NUMPY ARRAY
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
# Output: [1 2 3 4 5]
# This is a 1-dimensional NumPy array (like a list but faster)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
# For 2D array the columns in all the rows must be equal
# Output:
# [[1 2 3]
#  [4 5 6]]
# This is a 2-dimensional array (matrix with 2 rows and 3 columns)

print("Type:", type(arr1))
# Output: Type: <class 'numpy.ndarray'>
# This tells you that arr1 is a NumPy array (ndarray)

print("Shape:", arr2.shape)
# Output: Shape: (2, 3)
# Means: arr2 has 2 rows and 3 columns


# MEMORY EFFICIENCY
import sys

# sys is a built-in Python module that provides access to system-level information and functions that Python uses while running your program.

list_data = list(range(1000))
numpy_data = np.array(list_data)

print("Python list size:", sys.getsizeof(list_data) * len(list_data), "bytes")
print("NumPy array size:", numpy_data.nbytes, "bytes")

# VECTORIZATION
# Python list (loop-based)
list_3=[1,2,3,4,5,6,7,8,9]
start = time.time()
list_squares = [x ** 2 for x in list_3]
end = time.time()
print("Time taken :",end-start)

# NumPy (vectorized)
arr3=np.array(list_3)
start = time.time()
numpy_squares = arr3 ** 2
end = time.time()
print("Time taken :",end-start)

