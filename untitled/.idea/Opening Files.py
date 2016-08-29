print("Have you been here before?")
choice = input().lower()

if 'y' == choice == 'yes':
        print("What's your name?")
        returnUserName = input()

        for line in read_text:
            if returnUserName in Line:
                print(line)
else:
        print ("Hello user! What is your name?")
        while True:
            try:
                username = str(input())
                break
            except:
                print("I didn't recognize that name, can you repeat?")


print("Okay, %s tell me a little about yourself..." %username)

hometown = input("Where are you from?")
age = input("%s, that's coool! How old are you?" %hometown)

new_text = text_file.write([userName, hometown, age])

text_file.close()