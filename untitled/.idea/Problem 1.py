num = int(raw_input("Please enter a number: "))
numTwo = int(raw_input("Please enter a multiple of the number you entered: "))

for num in range(num, numTwo):
    for i in range (num, 1):
        print '%d * %d = ' % (num, 1+1)


Naeem's description:

for x in ragne (1, (multiple + 1))
    print ("%s * %s = %s" %(userInput, x, (userInput*x)))