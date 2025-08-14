# Broadcasting
# stretching te size of smaller array so that it matches size of a larger array

# NumPy compares shapes from right to left:
# If dimensions are equal → ✅ OK
# If one dimension is 1 → it can be stretched to match the other
# If dimensions differ and neither is 1 → ❌ Error

a = np.array([1, 2, 3])
print(a + 10)  # [11 12 13]
# The scalar 10 is broadcast to [10, 10, 10]

a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
print(a + b)
# [[11 22 33]
# [14 25 36]]
# b is treated as if it were:
# [[10, 20, 30],
#  [10, 20, 30]]

# a.shape = (3, 1)   # 3 rows, 1 col
# b.shape = (1, 4)   # 1 row, 4 cols
# Broadcast to (3, 4)

# a = np.array([1, 2, 3])
# b = np.array([1, 2])
# a + b  # ❌ ValueError: shapes (3,) and (2,) not aligned




