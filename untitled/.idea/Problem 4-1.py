sentence = raw_input("Please enter a sentence: ")
wordList = sentence.split(" ")

wordRemove = raw_input("Which word would you like to replace in the sentence: ")
if wordRemove in wordList:
    replacer = raw_input("what word would you like to replace it with?: ")
    index = wordList.index(wordRemove)

    wordList.insert(index, replacer)
    wordList.pop(index)
    print(("".join)wordList)
else:
    print ('That word is not in the sentence.')

print wordList


# sentenceSplit.insert((sentenceSplit.index(wordToReplace.lower())), replacementWord)
# sentenceSplit.pop((sentenceSplit.index(wordToReplace.lower())))