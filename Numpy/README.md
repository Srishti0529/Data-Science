# NumPy - README

## Overview

NumPy (Numerical Python) is a Python library used for **fast numerical computing** and **multidimensional array operations**.
It is the **foundation of Data Science, Machine Learning, and Scientific Computing** in Python.

---

## Why Use NumPy

* Faster than Python lists
* Supports multidimensional arrays
* Mathematical operations on arrays
* Less memory usage
* Vectorized operations (no loops)
* Broadcasting support

---

## Installation

```bash
pip install numpy
```

---

## Import NumPy

```python
import numpy as np
```

---

## Creating Arrays

### 1D Array

```python
a = np.array([1,2,3,4])
```

### 2D Array

```python
a = np.array([[1,2,3],[4,5,6]])
```

### Zeros / Ones

```python
np.zeros((2,2))
np.ones((3,3))
```

---

## Array Attributes

```python
a.shape     # dimensions
a.size      # total elements
a.dtype     # data type
a.ndim      # number of dimensions
```

---

## Mathematical Operations

```python
a + b
a - b
a * b
a / b
np.sqrt(a)
np.sum(a)
np.mean(a)
```

---

## Indexing & Slicing

```python
a[0]
a[0:3]
a[0,1]
```

---

## Reshaping Arrays

```python
a.reshape(2,3)
a.flatten()
```

---

## Vectorization

NumPy performs operations **without loops**

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

c = a * b
```

Output:

```
[4 10 18]
```

---

## Broadcasting

NumPy automatically expands smaller arrays

```python
a = np.array([1,2,3])
b = 2

a * b
```

Output:

```
[2 4 6]
```

---

## Random Functions

```python
np.random.rand(3)
np.random.randint(1,10,5)
```

---

## Useful Functions

```python
np.max(a)
np.min(a)
np.sort(a)
np.unique(a)
```

---

## NumPy vs Python List

| NumPy       | List          |
| ----------- | ------------- |
| Fast        | Slow          |
| Fixed type  | Mixed type    |
| Less memory | More memory   |
| Vectorized  | Loop required |

---

## Use Cases

* Data Science
* Machine Learning
* Deep Learning
* Scientific Computing
* Image Processing
* Statistics

---

## Example

```python
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)
print(a * b)
```

---

## Summary

* NumPy = numerical computing library
* Core object = ndarray
* Fast array operations
* Supports vectorization & broadcasting
* Used in Data Science & ML

---