import random 

num = random.randint(1,100)
tries = 0 
while True:
    guess = int(input("PLEASE GUESS A NUMBER BETWEEN 1 TO 100 TO START THE GAME :"))


    if num == guess:
        tries +=1
        print(f"YOU ARE RIGHT AND YOU GUESSED THE NUMBER IN {tries} TRIES")
        break

    elif num < guess:
        tries +=1
        print("GO A LITTLE LOWER")

    elif num > guess:

        print("GO A LITTLE HIGHER")

    else:
        tries+=1
        print("YOU ARE WRONG")


