import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr2 = np.array([2, 6, 1, 38, 9, 0, 6, 5, 3, 2])

# Mean → average value
print(np.mean(arr1))
# Output: 5.5

# Standard Deviation → how spread the data is
print(np.std(arr1))
# Output: 2.8722813232690143

# Variance → square of standard deviation
print(np.var(arr1))
# Output: 8.25

# Minimum value
print(np.min(arr1))
# Output: 1

# Maximum value
print(np.max(arr1))
# Output: 10

# Sum of all elements
print(np.sum(arr1))
# Output: 55

# Product of all elements
print(np.prod(arr1))
# Output: 3628800

# Median → middle value after sorting
print(np.median(arr1))
# Output: 5.5

# Index of minimum value
print(np.argmin(arr1))
# Output: 0  (because 1 is at index 0)

# 50th percentile (same as median)
print(np.percentile(arr1, 50))
# Output: 5.5

# Index of maximum value
print(np.argmax(arr1))
# Output: 9 (10 is at index 9)

# Correlation coefficient between arr1 and arr2
print(np.corrcoef(arr1, arr2))
"""
Output:
[[ 1.         -0.06749068]
 [-0.06749068  1.        ]]

Meaning: correlation is -0.067 (almost no relation)
"""

# Unique values in array
print(np.unique(arr1))
# Output: [ 1 2 3 4 5 6 7 8 9 10 ]

# Difference between consecutive elements
print(np.diff(arr1))
# Output: [1 1 1 1 1 1 1 1 1]

# Cumulative sum
print(np.cumsum(arr1))
# Output: [ 1  3  6 10 15 21 28 36 45 55]

# Generate 5 numbers between 0 and 10 (inclusive)
print(np.linspace(0, 10, 5))
# Output: [ 0.   2.5  5.   7.5 10. ]

# Natural logarithm of each element
print(np.log(arr1))
# Output: [0.         0.6931 1.0986 ... 2.3025]

# Exponential (e^x)
print(np.exp(arr1))
# Output: very large numbers (e^1, e^2, e^3 ...)
