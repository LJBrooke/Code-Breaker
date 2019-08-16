# Code-Breaker

Just a fun little project I embarked on after being intrigued by playing this game. The code here was just built
to satisfy my curiosity, I have no plans to do anything with it, as such the code is not commented and there has 
only been a cursory thought about structuring it in a sensible manner.

While I was cracking someone elses code, I realized that what I was essentially doing is creating lists of possible
pins for each slot. Then randomly selecting the pins. I was intrigued and decided to see if I could create an algorithm
to solve the game.

The final solution I built involves a consistency check after the random selection. This ensures that the algorithm 
can actually gain information from it's previos guesses.
