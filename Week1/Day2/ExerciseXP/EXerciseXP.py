""" 🌟 Exercise 1: Favorite Numbers """
# Create a set of favorite numbers
my_favorite_number = {2,4,6,8,78,67,45}

#Add two new numbers to the set.
my_favorite_number.update([5, 9])  #Add multiple at once
my_favorite_number.add(10)         #Add one at a time
print(my_favorite_number)

#Remove the last item you added
my_favorite_number.remove(10)
print(my_favorite_number)

#create another list
friend_favorite_number = {2,4,6,8,10,100,57}

#Concatenate the two sets
result = my_favorite_number | friend_favorite_number
print(result)


""" 🌟 Exercise 2: Tuple """
# Given a tuple of integers
my_tuple = (2,4,6,8,10,100,57)

#Try to add more integers to the tuple.
#print(my_tuple.append(4))   #Displays an error

my_tuple = my_tuple + (4,)   #Adding indirectly is supportable
print(my_tuple)