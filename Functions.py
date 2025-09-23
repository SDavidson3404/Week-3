def alarm(guess, password):
    if guess == password:
        return True
    else:
        return False

userGuess = input("Please enter a guess: ")

if alarm(userGuess, "3404"):
    print("Congrats, you are the creator, hello creator")
else:
    print("WEE WOO WEE WOO, YOU ARE TRYING TO BREAK IN!")