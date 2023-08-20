'''
## A Chocolate Enthusiast (15 pts)

Imagine you're a chocolate enthusiast and you've tried different types of chocolate, each of which has a unique ID from 0 to N-1. You want to determine the chocolate type that you've tasted the most frequently. If you've tasted multiple types the same number of times, you want to know the type with the smallest ID.

For example, let's say you've tasted 10 different types of chocolate, each with an ID from 0 to 9, and you've kept track of your tastings in a list:

`chocolate_ids = [1, 5, 2, 5, 9, 1, 1, 5, 2, 2, 2, 5, 0, 0, 3]`

Write a function `most_frequent_chocolate(chocolate_ids, N)` that takes a list of chocolate IDs, `chocolate_ids`, and the maximum ID, `N`, and returns the most frequently tasted chocolate ID.

**Examples:**
```
most_frequent_chocolate([1, 5, 2, 5, 9, 1, 1, 5, 2, 2, 2, 5, 0, 0, 3], 10) # should return 2
```

**Hint**: You can define a new list of length N (to account for the chocolate IDs starting from 0) and keep track of the number of occurrences of each ID in this list.
'''


# Implement your function here
def most_frequent_chocolate(chocolate_ids, N):
    ##########################
    ### START OF YOUR CODE ###
    ##########################

    liste = [0] * N

    for i in chocolate_ids:
        liste[i] += 1

    maxele = max(liste)
    inx = liste.index(maxele)

    return inx

    ##########################
    ###  END OF YOUR CODE  ###
    ##########################


if __name__ == '__main__':
    # You can test your code with these sample testcases
    # Run q1_tests.py file for more testcases

    chocolate_id = most_frequent_chocolate([1, 5, 2, 5, 9, 1, 1, 5, 2, 2, 2, 5, 0, 0, 3], 10)
    print(chocolate_id)  # 2

