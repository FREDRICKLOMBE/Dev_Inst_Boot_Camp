""" 🌟 Challenge 1: Sorting """

#Get comma-separated words from the user.
words = input("Enter words separated by commas: ")

#Split the string into a list.
words = words.split(",")

#Sort the words in alphabetical order.
words.sort()

#Join the sorted words with commas.
result = ",".join(words)
print(result)


""" 🌟 Challenge 2: Longest Word """

#Define a function that returns the longest word in a sentence.
def longest_word(sentence):
    words = sentence.split()
    longest = ""

    #Keep punctuation as part of each word.
    for word in words:
        #Only replace with a longer word to keep the first word in a tie.
        if len(word) > len(longest):
            longest = word

    return longest


#Print the results for the given examples.
print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))
