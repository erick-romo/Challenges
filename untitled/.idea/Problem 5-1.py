# Write a program at generates a random 7 digit number and add all of the prime digits in the number.
#
# Time Limit: 45 minutes
#
# Input - None
# Process - Program must generate a random 7 digit number, then add all of the prime number together.
# Output - The original number and the sum of the prime numbers
import random
randomnumlist = []
primeList = []
nonprime = []

for x in range (7):
    randomNumber = random.randint(0, 9)
    randomnumlist.append(randomNumber)
print randomnumlist

    # randomList.split(" ")
    # print randomList
    
#this is the outher loop
for x in range(1, 10):
#this is the inner loop
    for num in randomnumlist:
        if x % num == 0:
            if x not in nonprime:
                nonprime.append(x)
        else:
            primeList.append(x)

print primeList

# ("This is your list of numbers: %s", %randomList'')

