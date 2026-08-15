#1 Accept a number from the user and convert the input to an integer
number = int(input("Enter a number: "))

# Loop through the numbers 1 to 10
for i in range(1, 11):
    # Calculate the product of the user's number and the current value of i
    multiple = number * i

    # Create a formatted string for one row of the multiplication table
    # :2   -> right-align the number in a field 2 characters wide
    # ^3   -> center the multiplier in a field 3 characters wide
    # :3   -> right-align the product in a field 3 characters wide
    table = f"{number:2} x {i:^3} = {multiple:3}"

    # Display the formatted multiplication table row
    print(table)

#2 Print the numbers from 1 to 10 using while loop
numb = 1
while numb <= 10:
    print(numb)
    numb += 1