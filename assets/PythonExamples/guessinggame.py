#Guessing game

import random
name = input("Hello player 1 may I have your name please ? ")
computerguess = random.randint(1,10)
guessesleft = 3
print("Hello player " + name + " provide a guess between 1 and 10 please, you have " + str(guessesleft) + " left" )


playerguess = int(input())

guessesleft-=1

while computerguess != playerguess and guessesleft > 0 :
    if playerguess < computerguess:
        print("Your guess " + str(playerguess) +  " is too low try again ! " + str(guessesleft) + " left")

    elif playerguess > computerguess:
        print("Your guess " + str(playerguess) + " is too high try again ! " + str(guessesleft) + " left")

    print("Hello player " + name + " provide a guess between 1 and 10 please")

    playerguess = int(input())
    guessesleft-=1

if playerguess == computerguess:
    print("YEEESSSS That was it the number I was looking for was " + str(computerguess) + " and you had " + str(guessesleft) + " turns left")


else:
    print("Sorry you lose buddy , you have " + str(guessesleft) + " left the number I had in mind was "+ str(computerguess))