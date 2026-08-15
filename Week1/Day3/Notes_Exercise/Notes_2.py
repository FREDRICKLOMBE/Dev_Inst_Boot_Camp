
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end=' ')
    print()