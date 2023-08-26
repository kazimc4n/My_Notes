'''
Tuple Search

You are given a list of tuples, where each tuple contains the name (a string) and score (an integer) of a player who participated in a game. The score represents the points earned by the player in the game. You are also given a name (a string) as input.

Write a function called ```calculate_total_score``` that takes the *list of tuples* and a *name* as input, and calculates the total score of the player with the given name. The function should return the total score as an integer. If the name does not exist in the list, return 0.


Examples:


```
calculate_total_score([("Alice", 10), ("Bob", 20)], "Bob") → 20
```

```
calculate_total_score([("Alice", 10), ("Bob", 20), ("Charlie", 30)], "Dave") → 0
```


```
calculate_total_score([("Alice", 10), ("Bob", 20), ("Charlie", 30), ("Dave", 40), ("Alice", 15)], "Alice") → 25
```
'''
def calculate_total_score(tuples, value:int):
    count = 0
    for i in tuples:
        if i[0] == value:
            count += int(i[1])

    return count

print(calculate_total_score([("Alice", 10), ("Bob", 20)], "Bob"))