import Codebreaker as code
from random import choice
from random import randint 
from time import time

options = ["a", "s", "d", "f", "g", "h"]
printGuesses = True


def genPattern(possiblePins):
    newPattern = ""
    while len(newPattern)<4:newPattern = newPattern + possiblePins[randint(0, 5)]
    return newPattern


def createGuess(groups): 
    guess = []
    groupSlots = [ list(groups[0]), [0, 1], list(groups[1]), [2, 3] ]
    
    for i in range (2):
        selected = groupSlots[2*i].pop(randint(0, len(groupSlots[2*i])-1))
        guess.insert(groupSlots[2*i+1].pop(randint(0, 1)), selected)
        selected = groupSlots[2*i].pop(randint(0, len(groupSlots[2*i])-1))
        guess.insert(groupSlots[2*i+1][0], selected)
    
    strGuess =''
    for n in range(4): strGuess = strGuess+guess[n]
    return strGuess


def makeGuess(guess, solution, attempts):
    last_guess = code.attempt(guess, solution)
    attempts.append([guess, last_guess])
    if (printGuesses): code.printAttempts(attempts)
    return attempts


def baseGuess(group, attempts, solution, index):
    a, b = options[2*index], options[2*index+1]
    guess = a + a + b + b
    attempts = makeGuess(guess, solution, attempts)
    mark = attempts[index][1]

    if mark[0]+mark[1] > 0:     
        if mark[0]==0: # 0 Reds
            if mark[1]==1:group = [group[0] + b, group[1] + a] # 1 White
            elif mark[1]>=2: group = [group[0] + b + b, group[1] + a + a] # 2, 3 or 4 White     
        elif mark[0]==1: # 1 Red
            if mark[1]==0: group = [group[0] + a, group[1] + b] # 0 White
            elif mark[1]>=1: group = [group[0] + a + b, group[1] + a + b] # 1 or 2 White
        elif mark[0]==2: # 2 Red
            if mark[1]==0: group = [group[0] + a + a, group[1] + b + b] # 0 White
            elif mark[1]>=1: group = [group[0] + a + b, group[1] + a + b] # 1 or 2 White         
        elif mark[0]==3: group = [group[0] + a + a, group[1] + b + b] # 3 Red 0 White
        
        # Can alter to check if red > 0 and likewise for white >0. might be shorter.
            
    return group, attempts


def check(guess, pattern, mark):
    red, white= 0, 0
    while(len(guess)<4): guess = guess+" "
    guess=guess[0:4].lower()
    
    if (guess==pattern): return False # Avoids Retrying already guessed patterns.
    else:
        for n in range(0,4):
            if guess[n]==pattern[n]: red = red + 1
        
        letters, guesses = list(pattern), list(guess)
        for i in guesses:
            if letters.count(i)>0:
                letters.remove(i)
                white = white + 1
        
        white = white - red
        if [red, white] == mark:
            return True
        return False
            

def solve(solution):
    attempts = [] # [pattern, [red, white]]
    groups = ['', '']
    colours, index = 0, 0

    while (colours < 4 and index < 3): # Iterates Through Base Guesses.
        groups, attempts = baseGuess(groups, attempts, solution, index)
        colours = colours + attempts[index][1][0] + attempts[index][1][1]
        index += 1

    while (colours <4):
        for guess in attempts:
            if guess[1][0]+guess[1][1] > 1:
                groups = [groups[0] + guess[0][2], groups[1] + guess[0][0]]
        colours = colours + 1
    
    while (attempts[-1][1]!=[4, 0] and len(attempts)<8):
        consistent = False
        
        while not consistent:
            guess = createGuess(groups)
            consistent = True
            for trials in attempts:
                consistent = check(guess, trials[0], trials[1])
                if not consistent: break
        attempts = makeGuess(guess, solution, attempts)
    
    if (len(attempts)==8 and attempts[-1][1]!=[4, 0]): print("The pattern was: " + solution) 
    return attempts
    

def type1():
    runs, success, tries, maxTries = 0, 0, 0, 0

    tests = ['sahg', 'ashg', 'aasa', 'sasa', 'ssss', 'asdf', 'sdfg', 'dfgh', 'hhgg', 'shgg']
    for pats in tests:
        print("\nTest Pattern: " + pats)
        trialAttempts = solve(pats)
        if trialAttempts[-1][1]==[4, 0]: success+=1
        runs+=1
        if len(trialAttempts)>maxTries: maxTries=len(trialAttempts)
        tries = tries + len(trialAttempts)
    return success, tries, maxTries, runs


def type2(total):
    runs, success, tries, maxTries = 0, 0, 0, 0
    start = time()
    while runs<total:
        print("Run: " + str(runs+1))
        pats = genPattern(options) 
        print("Testing: " + str(pats), end='')
        trialAttempts = solve(pats)
        if trialAttempts[-1][1]==[4, 0]: success+=1
        runs+=1
        if len(trialAttempts)>maxTries: maxTries=len(trialAttempts)
        tries = tries + len(trialAttempts)
    end = time()
    rps = total/(end-start)
    print("\nRuns per Second: " + str(rps), end="")
    return success, tries, maxTries


def test(type, total):
    global printGuesses
    printGuesses = False
    if type==1: success, tries, maxTries, total = type1()
    elif type==2: success, tries, maxTries = type2(total)

    print("\nSuccess Rate: " + str(success) + "/" + str(total) +"\nAverage Tries: " + str(tries/total) +"\nMax Tries: " + str(maxTries))


def play():
    pattern = input("Select The pattern for the computer to solve: \n")
    solve(pattern)
    print("Game Over")


def menu():
    print("Welcome:")
    choices = ['Play against the Computer', "Run Tests"]
    for q in range(1, len(choices)+1): print(str(q) + ": " + choices[q-1])
    choice = eval(input(": "))
    if choice==1: play()
    elif choice==2:
        runs, choice = 1000, eval(input("Select test type: "))
        if choice==2: runs = eval(input("Select the number of runs: "))
        test(choice, runs)


if __name__ == '__main__':
    menu()