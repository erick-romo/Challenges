#<---string methods--->
string = "This is a string"

# ".count() returns the number of ocurances of a given character in a string. Takes one argument and is case sensitive. The retrun is an int."
print(string.count("v"))

# ".index() returns the index of a character within a string. Takes one argument and is case sensitive. Returns an int."
print(string.index("s"))

#Returns string as all caps"
print(string.upper())

#"Caps the first letter of the first word"
print(string.capitalize())

#"Caps the first letter of the first word"
print(string.capitalize())

# Swaps the casing of a string
print(string.swapcase())

print(','.join(string))

filename = "sample.jpg.lala"

newFileName = (filename.split("."))[2]
print newFileName

#or

print(filename.replace('_', ' '))

#you'll usually use join on a list because list has some strings. Join makes more sense to do with lists.

#<------List Methods-------->

NewList = ["one", "two", "three", "four"]

NewList.append("five")
print(NewList)

SecList = ["six", "Seven", "Eight"]

NewList.extend(SecList)
print(NewList)

#you could do a plus sign as well.

NewList.insert(0, "zero")
print(NewList)

NewList.remove("six")
print(NewList)

NewList.pop(5)
print(NewList)

#with remove you have to know the value and with popo you have to know the postion.

NumList = [1, 2, 3, 4]

#sorts alphabetically and numerically
NewList.sort()
NumList.sort()

print(NewList)
print(NumList)

#opposite of sort is reverse. It doesn't reverse the order, it reverses the way the list looks at that moment.

NumList.reverse()


#<-------Dictionary Methods------->

NewDiction = {"one": 1, "two": 2, "three": 3, "four": 4}

NewDiction['five'] = 5
print(NewDiction)


print(NewDiction.keys())

print(NewDiction.values())

print(NewDiction.items())

NewDiction.pop('six')
print(NewDiction)

NewDiction.popitem()
print(NewDiction)

print(NewDiction.get("one"))

