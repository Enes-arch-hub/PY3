import numpy as np

# 1. Create arrays
numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)
print("First:", numbers[0])
print("Last:", numbers[-1])

# 2. Arithmetic
print("\nArithmetic")
print(numbers + 5)
print(numbers * 2)
print(numbers ** 2)

# 3. Statistics
print("\nStatistics")
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Max:", np.max(numbers))
print("Min:", np.min(numbers))

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nMatrix")
print(matrix)

print("Shape:", matrix.shape)
print("Rows:", matrix.shape[0])
print("Columns:", matrix.shape[1])

print("Element:", matrix[1,2])

scores = np.array([75, 82, 90, 68, 95])

print("\nScores")
print(scores)

# Highest score
print(scores.max())

# Average score
print(scores.mean())

# Passed students
print(scores[scores >= 80])