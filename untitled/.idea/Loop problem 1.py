# # Write a program that gets an integer from the user. Count from 0 to that number. Use a for loop to do it.
#
# # number = input("Please enter any number: ")
# #
# # for x in range (number+1):
# #     print x
#
# # write a program that gets an integer from the user and counts from 1 to that number, but uses "*" to represent that number.
#
# number = input("Please enter any number: ")
#
#
# for x in range (1, number+1):
#     print ("bae " * x)
#
#     userInput = input("What is your full name? ")  # Ask the user for their full name.
#     nameList = userInput.split()  # split the user's full name (.split)see next line
#     # nameList = ["Thomas", "Twine"]
#     vowels = ["a", "e", "i", "o", "u"]  # list the vowels

userInput = raw_input("What is your full name? ") #Ask the user for their full name.
nameList = userInput.split() #split the user's full name (.split)see next line
#nameList = ["Thomas", "Twine"]
vowels = ["a", "e", "i", "o", "u"] # list the vowels

for name in nameList:
    vowelCounter = 0  # counter is set to 0, we reset it for the last name.

    for letter in range(len(name)):  # (for the _ number of iteration, length of name);
        # ex. Thomas Twine
        if name[letter] in vowels:  # (letter at the _ numbr index position, you can index a string)
                vowelCounter += 1


fullName = input("What is your full name?: ")

vowels = ['a', 'e', 'i', 'o', 'u']
nameList = fullNamesplit()

    for name in nameList:
        vowelCounter = 0
        for letter in name:
            if letter in vowels:
                vowelCounter += 1

print("There are %s vowels in \"%s\"" % (vowelCounter, name.title()))