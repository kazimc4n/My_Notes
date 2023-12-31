'''
Kevin and Stuart want to play the ‘The Minion Game’.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin’s vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
'''

def MinionGame(string):
    s = len(string)
    vowel = 0
    consonant = 0

    for i in range(s):
        if string[i] in "AIOUE":
            vowel += (s - i)
        else:
            consonant += (s - i)

    if vowel < consonant:
        return "Stuart: "+ str(consonant)
    elif consonant < vowel:
        return "Kevin: "+ str(vowel)
    else:
        return "Draw"

print(MinionGame("BANANA"))

