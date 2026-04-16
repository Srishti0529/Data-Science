import numpy as np

# Random value 2D matrix of size 3*3
arr_1 = np.random.randint(0, 100, size=(3, 3))
# randint means Random Integer.
print(arr_1)

# COnvert array of floats to integer
floats = np.array([1.1, 2.2, 3.3])
arr_2 = floats.astype(np.int32)
print(arr_2)

# Extract even numbers from matrix usinf fancy indexing
array = np.array([1, 2, 3, 4, 5, 6])
arr_3 = array[array % 2 == 0]
print(arr_3)

# Reshape 1D array os size 9 to 2D of 3*3
dim_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr_4 = dim_1.reshape((3, 3))
print(arr_4)

# Bollean masking to extract number greater than 50
array = np.array(
    [
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        62,
        63,
        64,
        65,
        66,
        67,
        68,
        69,
        70,
    ]
)
mask = array > 50
print(array[mask])
