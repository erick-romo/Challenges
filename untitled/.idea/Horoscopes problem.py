from horoscopes import *

def zodiacSign():
    print"{}"

    try:
        zodiacSign = input("What is your zodiac sign? ").capitalize()
        while zodiacSign in horoscopes.keys():
             print(horoscopes[zodiacSign]["yearly"])


    except:
         print("Try again. Please check your spelling.")

zodiacSign()

#Naeem's code:

from horoscopes import *

while True:
        try:
            horoscope = horoscope [input("Please enter zodiac sign: ")].capitaliza()]
            break
        except KeyError :
            print("Invalid Entry")

        return horoscope

print(horoscopeLookUp()['weekly'])