MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%
'''

""" Step 1 & 2: Transforming the String into a 2D List """
# Processing Columns
new_matrix = []

rows = MATRIX_STR.strip().splitlines()
print(rows)

for row in rows:
    new_matrix.append(list(row))

print(new_matrix)

""" Step 3: Filtering Alpha Characters """
temp_string = ""

for row in range(len(new_matrix)):
    for col in range(len(new_matrix[row])):

        if new_matrix[row][col].isalpha():
            temp_string = temp_string + (new_matrix[row][col])

print(temp_string)