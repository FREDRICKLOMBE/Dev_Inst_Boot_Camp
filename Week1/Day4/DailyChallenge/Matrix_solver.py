MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

# Step 1: Convert string to 2D list
matrix = []

for row in MATRIX_STR.strip().split("\n"):
    matrix.append(list(row))

# Step 2-4: Read columns and process characters
message = ""
symbol_found = False

for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        char = matrix[row][col]

        if char.isalpha():
            if symbol_found:
                message += " "
                symbol_found = False

            message += char
        else:
            symbol_found = True

# Step 5: Print decoded message
print(message)