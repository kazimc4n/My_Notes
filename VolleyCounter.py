'''
## CEV Champions League Finals (20 pts)

Vakifbank and Eczacibasi, two popular volleyball teams are going to play the CEV finals match. You have been tasked to write a Python function to determine the winner of the game.

Here are some preliminary info about volleyball:

- **Rule 1:** Volleyball matches are played in sets, typically best-of-five (i.e., the first team to win 3 sets wins the match).
- **Rule 2:** Each set is played to a specific number of points, typically 25 points, but may vary depending on the level of play or specific competition rules.
- **Rule 3:** Teams must win a set by a margin of at least 2 points. If both teams have the same number of points (e.g., 24-24), the set continues until one team has a lead of at least 2 points.
- **Rule 4:** In case of a tie in sets (2-2), the final set is played. It is a shorter set, typically 15 points, but again may vary depending on the margin of at least 2 points.
- **Rule 5:** The team that wins the required number of sets first (typically 3 out of 5) wins the match.


You need to write a function `play_set()`, which should take a string parameter `points` as input. The string `points` consists of uppercase letters 'V' and 'E', where 'V' denotes a point scored by Vakifbank and 'E' denotes a point scored by Eczacibasi. **The length of the points might be longer than required, you need to process it from left to right, and finish your iteration when the set is over.**

Your function should return the points of each team for that set, and the current sets of each team, both in the order of Vakifbank-Eczacibasi. **Note that you should treat the 5th set differently (see Rule 4 from above).**

When the game ends, i.e. when one of the teams wins 3 sets, return the final score, and reset your variables. See below for example testcases.


Example:
```
# 1st game, 1st set
points = 'VVEEEVEVEVEVVEVEEVEVEEVVVEEVEEEVVVVEEVVEVVVEEVEEVEVVEVEVVEEV'
V_pts, E_pts, V_sets, E_sets = play_set(points)
print(V_pts, E_pts, V_sets, E_sets) -> (27, 25, 1, 0)

# 1st game, 2nd set
points = 'EEEEVEEVVVEEEEVVVEEEVEVEVEVEEEVEVEVVEEVEEEEVVVEVEVEEVEVEV'
V_pts, E_pts, V_sets, E_sets = play_set(points)
print(V_pts, E_pts, V_sets, E_sets) -> (16, 25, 1, 1)

# 1st game, 3rd set
points = 'VEVVEVEVEVEVVVEEVVVEVEVVVEVEVEVEVEVVEVEVVEVVEVVEVEVEVVVEVE'
V_pts, E_pts, V_sets, E_sets = play_set(points)
print(V_pts, E_pts, V_sets, E_sets) -> (25, 16, 2, 1)

# 1st game, 4th set
points = 'EEEEEEEEEEVVVVVVVVVVEEEEEVVVVVEEEEVVVVVEEVEVEEVVVEVEEEVEVEVE'
V_pts, E_pts, V_sets, E_sets = play_set(points)
print(V_pts, E_pts, V_sets, E_sets) ->  (26, 28, 2, 2)

# 1st game, 5th set
points = 'VVVVEEEEVVVVEEEEVVVVEEEEVEVEVEVEVEVEVVEEEEVVVEVEVVEEVVVEVVVV'
V_pts, E_pts, V_sets, E_sets = play_set(points)
print(V_pts, E_pts, V_sets, E_sets) -> (20, 18, 3, 2)

# 2nd game, 1st set
points = 'VVEEEVEVEVEVVEVEEVEVEEVVVEEVEEEVVVVEEVVEVVVEVVEVEVVEVE'
V_pts, E_pts, V_sets, E_sets = play_set(points)
print(V_pts, E_pts, V_sets, E_sets) -> (25, 21, 1, 0)

```


### Hints:
- The length of the points might be longer than required, you need to process it from left to right, and finish your iteration when the set is over.
- Note that you should treat the 5th set differently (see Rule 4 from above).
- Note that not each game has to end in 5 sets. 3-0 or 3-1 are also valid scores.
- Think of which variables you need to set as global, and which as local.

'''


# You can define your global variables here
##########################
### START OF YOUR CODE ###
##########################

##########################
###  END OF YOUR CODE  ###
##########################


# Implement your function here
def play_set(points):
    ##########################
    ### START OF YOUR CODE ###
    ##########################
    global V_sets, E_sets
    V_pts, E_pts = 0, 0

    isSetFinished = False

    for point in points:
        if point == 'V':
            V_pts += 1
        elif point == 'E':
            E_pts += 1

        if V_sets == 2 and E_sets == 2:
            if abs(V_pts - E_pts) >= 2 and (V_pts >= 15 or E_pts >= 15):
                isSetFinished = True
        else:
            if abs(V_pts - E_pts) >= 2 and (V_pts >= 25 or E_pts >= 25):
                isSetFinished = True

        if isSetFinished:
            break

    if V_pts > E_pts:
        V_sets += 1
    else:
        E_sets += 1

    if V_sets == 3 or E_sets == 3:
        last_Vakif_sets, last_Eczaci_sets = V_sets, E_sets
        V_sets, E_sets = 0, 0
        return V_pts, E_pts, last_Vakif_sets, last_Eczaci_sets

    return V_pts, E_pts, V_sets, E_sets

    ##########################
    ###  END OF YOUR CODE  ###
    ##########################


if __name__ == '__main__':
    # You can test your code with these sample testcases
    # Run tests_q2.py file for more testcases

    # 1st game, 1st set
    points = 'VVEEEVEVEVEVVEVEEVEVEEVVVEEVEEEVVVVEEVVEVVVEEVEEVEVVEVEVVEEV'
    V_pts, E_pts, V_sets, E_sets = play_set(points)
    print(V_pts, E_pts, V_sets, E_sets)  # (27, 25, 1, 0)

    # 1st game, 2nd set
    points = 'EEEEVEEVVVEEEEVVVEEEVEVEVEVEEEVEVEVVEEVEEEEVVVEVEVEEVEVEV'
    V_pts, E_pts, V_sets, E_sets = play_set(points)
    print(V_pts, E_pts, V_sets, E_sets)  # (16, 25, 1, 1)
