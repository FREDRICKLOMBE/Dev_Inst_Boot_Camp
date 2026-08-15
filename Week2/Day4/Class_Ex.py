"""
Ask user for a number 1 - 10
calculate the factorial
create a file named results.texts
Write the n! in this file and add a string 'my result is:'
"""
n = int(input("Enter a number: "))
factorial = 1
for i in range(1,n+1):
    factorial *= i

result = factorial
print(result)

#creating a file
try:
    f = open("results.texts", "w")
    f.write(f"My result is: {result}\n")
finally:
    f.close()