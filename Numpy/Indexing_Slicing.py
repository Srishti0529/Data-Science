import numpy as np

# Indexing (Same as Python Lists)
arr = np.array([10, 20, 30, 40])
print(arr[0])  # 10
print(arr[-1]) # 40

# Slicing (Extracting Parts of an Array)
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])  # [20 30 40] (slice from index 1 to 3)
print(arr[:3])   # [10 20 30] (first 3 elements)
print(arr[::2])  # [10 30 50] (every 2nd element)

# NOTE:Slicing returns a view, not a copy! Changes affect the original array.**
sliced = arr[1:4]
sliced[0] = 999
print(arr)  # [10 999 30 40 50]

# Fancy Indexing & Boolean Masking

# Fancy Indexing (Select Multiple Elements)
arr = np.array([10, 20, 30, 40, 50])
idx = [0, 2, 4]  # Indices to select
print(arr[idx])  # [10 30 50]

# Boolean Masking (Filter Data)
arr = np.array([10, 20, 30, 40, 50])
mask = arr > 25  # Condition: values greater than 25
print(arr[mask])  # [30 40 50]
