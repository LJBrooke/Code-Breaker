def attempt(guess, pattern):
    
    red, white= 0, 0
    while(len(guess)<4): guess = guess+" "
    guess=guess[0:4].lower()
    
    if (guess==pattern):
        print("\nCongratulations! '"+ guess +"' is correct!")
        return [4, 0]
    else:
        for n in range(0,4):
            if guess[n]==pattern[n]: red = red + 1
        
        letters, guesses = list(pattern), list(guess)
        for i in guesses:
            if letters.count(i)>0:
                letters.remove(i)
                white = white + 1
        
        white = white - red
        return [red, white]


def printAttempts(attempts):

    print("\n"+ str(len(attempts)))
    for attempt in attempts: print("Guess: '"+ attempt[0] +"' Reds: "+ str(attempt[1][0]) + " Whites: " + str(attempt[1][1]))
    print()


def play():

    print("Welcome")
    pattern = "bcpg" # Placeholder Pattern
    attempts = []

    guess = input("Pattern: ")[0:4]
    last_guess = attempt(guess, pattern)
    attempts.append([guess, last_guess])

    while (attempts[-1][1]!=[4, 0] and len(attempts)<8):
        printAttempts(attempts)
        guess = input("Pattern: ")[0:4]
        last_guess = attempt(guess, pattern)
        attempts.append([guess, last_guess])
    
    printAttempts(attempts)
    print("Game Over")


if __name__ == '__main__':
    play()