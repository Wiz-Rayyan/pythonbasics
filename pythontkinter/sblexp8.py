import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Shape and size
print("Shape of arr1:", arr1.shape)
print("Shape of arr2:", arr2.shape)
print("Size of arr2:", arr2.size)

# Reshaping array
reshaped_arr = arr2.reshape(3, 2)
print("Reshaped Array:\n", reshaped_arr)

# Transpose of array
transposed_arr = arr2.T
print("Transposed Array:\n", transposed_arr)

# Element-wise operations
arr3 = np.array([10, 20, 30, 40, 50])
sum_arr = arr1 + arr3
print("Element-wise Sum:", sum_arr)

# Slicing
sliced_arr = arr1[1:4]
print("Sliced Array:", sliced_arr)

# Mean, Max, and Min
print("Mean of arr1:", np.mean(arr1))
print("Max of arr1:", np.max(arr1))
print("Min of arr1:", np.min(arr1))
