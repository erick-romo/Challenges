word = raw_input("Enter a word, any word: ")

wordList = word.split(" ")
wordCount = wordList.count(" ")
print wordList
# print "You have these many duplicate letters: ", wordList.count(" ")

if count > 1:
    print "You have duplicates."
    print "Your duplicates are: %s"
else:
    print "You don't have any duplicates"
