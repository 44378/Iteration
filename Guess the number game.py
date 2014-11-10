#Jack Scaife
#10/11/14
#Guess the number game V1.1

#Imports generally placed at the start of the program
import random
random_number = random.randint(1,100)
#

Guess_number = 0

progress = False

while progress == False :
    guess = int(input("Please input a guess of what the generated number is: "))
    if guess < 1 or guess > 100 :
        print ("This is not within the required range.")
    else :
        Guess_number = Guess_number + 1
        if guess == random_number :
            print("You guessed the correct number of {0} in {1} guesses.".format(random_number,Guess_number))
            progress = True
        else :
            if guess > random_number :
                print("This guess is higher than the actual number.")
            else :
                print("This guess is lower than the actual number.")
