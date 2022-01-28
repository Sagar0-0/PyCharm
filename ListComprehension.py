x = 3
y = 3
z = 3
print([[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, 1 + z) if i + j + k != n])
