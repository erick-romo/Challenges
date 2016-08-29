#OPENING A FILE
#
# text_file = open("test.txt", "r")
#
# new_text=text_file.readlines()
#
# for line in new_text:
#         print("line %s: %s" %(x, line))
#         x += 1
#
#
# for line in new_text:
#         if "John" in line:
#             print(line[(line.index("John")):(line.index("John)+6")])
#
# print(new_text)
# text_file.close()

#WRITING A FILE

listOflines = ["This is the second line\n", "This is the third line\n", "This is the fourth line\n"]

new_text = text_file.writelines("This is the first Line\n")
new_text = text_file.writelines(listOflines)

text_file.close()
