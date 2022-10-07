print("GUESSING GAME")

x = str(input("Shall we start the game: \n"))
t=time.time()
tim = 1
while(time == 1):
    if x == "yes":
        lvl = input("Which level would you like to play Basic or Standard?:\n")
        l = lvl.lower()
        while(True):
            if l == "basic":
                name = str(input("Enter your name:"))
                print(
                    "Hello " + name + ",\n In this game I will choose a number between 0 and 100 and you have to guess it")
                a1 = int(input("Your guess is:"))
                import random

                n = random.randint(0, 100)
                number_of_guesses = 1
                print("Number of guesses is limited to only 9 times: ")
                while (number_of_guesses <= 9):
                    guess_number = int(input("Guess the number :\n"))
                    if guess_number < n:
                        print("you enter less number please input greater number.\n")
                    elif guess_number > n:
                        print("you enter greater number please input smaller number.\n ")
                    else:
                        print(number_of_guesses, "no.of guesses you took to finish.")
                        print("You WON!!")
                        break
                    print(9 - number_of_guesses, "no. of guesses left")
                    number_of_guesses = number_of_guesses + 1
                if (number_of_guesses > 9):
                    print("Game Over")
            elif l == "standard":
                import random

                n = random.randint(1, 30)
                name = str(input("Enter your name:"))
                print(
                    "Hello " + name + ",\n In this game I will choose a number between 1 and 30 and you have to guess it")
                a1 = int(input("Your guess is:"))
                print("Great your guess is right \n Wow, you won ;-)") if a1 == n else print(
                    "Oh no, you must try again \n Try again you have 4 more chances to guess")
                if a1 == n:
                    print("Thanks for playing")
                else:
                    a2 = int(input("Your second guess is:"))
                    print("Great your guess is right \n Wow, you won ;-)") if a2 == n else print(
                        "Oh no, you was close \n Try again you have 3 more chances to guess")
                    if a2 == n:
                        print("Thanks for playing")
                    else:
                        a3 = int(input("Your third guess is:"))
                        print("Great your guess is right \n Wow, you won ;-)") if a3 == n else print(
                            "Oh no, you was too close \n Try again you have 2 more chances to guess")
                        if a3 == n:
                            print("Thanks for playing")
                        else:
                            a4 = int(input("Your fourth guess is:"))
                            print("Great your guess is right \n Wow, you won ;-)") if a4 == n else print(
                                "Oh no, you was almost there \n Try again you have 1 more last chance to guess")
                            if a4 == n:
                                print("Thanks for playing")
                            else:
                                a5 = int(input("Your last guess is:"))
                                print("Great your guess is right \n Wow, you won ;-)") if a5 == n else print(
                                    f"Better luck next time and answer was {n}. \n GAME OVER")
    else:
            print("Hope you will come again")
            break
