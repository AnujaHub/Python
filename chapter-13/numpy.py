import numpy as np

# 1. Create arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# 2. Basic operations
print("Array + 5:", arr + 5)
print("Array * 2:", arr * 2)

# 3. Useful array info
print("Shape:", matrix.shape)
print("Size:", matrix.size)
print("Data type:", arr.dtype)

# 4. Built-in functions
print("Zeros:\n", np.zeros((2,2)))
print("Ones:\n", np.ones((2,2)))
print("Identity:\n", np.eye(3))
print("Random:\n", np.random.rand(2,3))

# 5. Math operations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

# 6. Indexing and slicing
print("Second element:", arr[1])
print("First row of matrix:", matrix[0])
print("Element at (1,2):", matrix[1,2])
