import numpy as np

# Original array (replace this with your actual array)
original_array = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])

# Target image size
target_height = 1602
target_width = 1200

# Calculate the required padding for each dimension
pad_height = max(0, target_height - original_array.shape[0])
pad_width = max(0, target_width - original_array.shape[1])

# Add padding to the array
padded_array = np.pad(original_array, ((0, pad_height), (0, pad_width)), mode='constant', constant_values=0)
print(padded_array.shape)

print("Original array:\n", original_array)
print("Padded array:\n", padded_array)
