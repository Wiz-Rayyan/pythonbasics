import numpy as np

# 1️⃣ Creating Arrays
arr1 = np.array([1, 2, 3, 4, 5])  # 1D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 3D array

# 2️⃣ Special Arrays
zeros = np.zeros((2, 3))   # 2x3 matrix of zeros
ones = np.ones((3, 2))     # 3x2 matrix of ones
random_arr = np.random.rand(3, 3)  # 3x3 matrix of random values
identity = np.eye(3)       # 3x3 Identity matrix

# 3️⃣ Shape, Size, and Data Type
print("Shape of arr2:", arr2.shape)
print("Size of arr2:", arr2.size)
print("Data type of arr2:", arr2.dtype)

# 4️⃣ Indexing & Slicing
print("Element at index 1 in arr1:", arr1[1])
print("First row of arr2:", arr2[0])
print("Slice of arr1 (1:4):", arr1[1:4])
print("Last column of arr2:", arr2[:, -1])

# 5️⃣ Arithmetic Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Addition:", a + b)
print("Multiplication:", a * b)
print("Square of a:", a ** 2)

# 6️⃣ Reshaping & Flattening
reshaped = arr2.reshape(3, 2)  # Change shape
flattened = arr2.flatten()      # Convert to 1D

# 7️⃣ Matrix Operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
dot_product = np.dot(A, B)  # Matrix multiplication
transposed = A.T  # Transpose

# 8️⃣ Broadcasting
arr_broadcast = np.array([1, 2, 3]) + np.array([[1], [2], [3]])

# 9️⃣ Sorting & Filtering
unsorted = np.array([5, 3, 8, 1])
sorted_arr = np.sort(unsorted)  # Sort array
filtered_arr = unsorted[unsorted > 3]  # Get elements > 3

# 🔟 Statistical Functions
print("Mean:", np.mean(arr1))
print("Max:", np.max(arr1))
print("Min:", np.min(arr1))
print("Sum:", np.sum(arr1))
print("Standard Deviation:", np.std(arr1))
