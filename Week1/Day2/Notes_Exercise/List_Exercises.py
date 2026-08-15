#1 Rearranging elements in string using for loop
fruit = 'pineapple'

fruit_1 = ''
for letter in fruit:
    fruit_1 =  letter + fruit_1
print(fruit_1)

#2 Create a list of odd numbers
odd_numbers = []
for num in range(1, 22):
    if num % 2 == 1:
        odd_numbers.append(num)
print(odd_numbers)


#4 Given this list:
list1 = [5, 10, 15, 20, 25, 50, 20]

  #find the value 20 in the list, and if it is present,
print(list1.index(20))

 # replace it with 200. Only update the first occurrence of a value
list1[3] = 200
print(list1)

#5 Unpack the following tuple into 4 variables

a_tuple = (10, 20, 30, 40)

a, b, c, d = a_tuple  #Unpacking the tuple
print(a)
print(b)
print(c)
print(d)

# 1 User input List
length = int(input("Whats your desired list length?"))

user_list = []
# Ask user for the many numbers
for i in range(length):
    numb = input(f"Enter the desired number {i + 1}: ")

    # Append the number to the list
    user_list.append(numb)
print(user_list)


print(user_list['100'])







