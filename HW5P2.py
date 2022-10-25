"""The game begins with N matches. Players take turns removing matches one, two, three at a time. The player removing the last match loses.
The first player wins if n=4j, 4j+2 or 4j +3 for some non negative integer j. The second player wins if the remaing cases when n = 4j +1"""

"""Bob = 0
Jon = 0

matches = 5

#function that takes turns for players
while matches > 0:
    Bob = int(matches) - 1
    #when player takes turn matches decrease by one
    matches = Bob
    Jon = int(matches) - 1
    #when player takes turn matches decrease by one
    matches = Jon
    print(Bob)
    print(Jon)"""

#take input for matches

matches = 5

if (matches % 2) == 0:
    print("Player one wins")

else:
    print("Player two wins")