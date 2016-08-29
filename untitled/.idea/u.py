# write a table program. the program should ask a user to input a number and display the product of that number from 1 to 50.
# basically, create a multiplication chart.

number = input("Please enter a number: ")

for x in range (1, 51):
    print "%s x %s = %s" % (number, x, (number * x))