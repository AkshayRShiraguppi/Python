
"""
Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the
user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed
correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many
“cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track
of the number of guesses the user makes throughout teh game and tell the user at the end.
Say the number generated by the computer is 1038. An example interaction could look like this:
  Welcome to the Cows and Bulls Game!
  Enter a number:
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...
"""

import random

def cowbull(gennum,unum):
    cowbull = [0,0]
    for i in range(len(gennum)):
        if gennum[i] == unum[i]:
            cowbull[0] += 1
        else:
            cowbull[1] +=1 
    return cowbull

if __name__ == "__main__":
    count = 0
    play = True
    gennum = str(random.randint(1000,9999))
    while play:
        unum = input('Enter number: ')
        cowbullcount = cowbull(gennum,unum)
        count += 1
        print('Cows are ' + str(cowbullcount[0]) + ', Bulls are ' + str(cowbullcount[1]))
        print('generated num is: ' + gennum)
    if cowbullcount[0] == 4:
        play = False
    else:
        print('wrong')
