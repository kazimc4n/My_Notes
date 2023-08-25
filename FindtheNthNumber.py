'''

## Q1: Find the nth number (2 pts)

> 1, 2, 5, 15, 41, 112, 310, ...

Consider the number pattern above. Assume the first 3 elements are given. Rest of the terms are calculated according to some hidden formula.

You first need to find out the hidden mathematical formula of the sequence. Then, write a recursive function named `find_nth_number()` that takes an integer `n` as input and returns the `n`th element of the sequence.

Start indexing the sequence from 1. That is, 1 is the 1st element, 2 is the 2nd element, 5 is the 3rd element. And if n is less than 1, return -1.

**Example outputs:**
```
print(find_nth_number(0)) # -1
print(find_nth_number(1)) # 1
print(find_nth_number(2)) # 2
print(find_nth_number(3)) # 5
print(find_nth_number(4)) # 15
print(find_nth_number(5)) # 41
print(find_nth_number(6)) # 112
print(find_nth_number(7)) # 310
```

**Hint:** The pattern is a weighted sum over the last 3 elements. That means, only multiplication and addition operations are used in the formula.
'''
def find_nth_number(n):
    if n == 0:
        return -1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 5
    else:
        return ((2 * find_nth_number(n-1)) + (1 * find_nth_number(n-2)) + 3 * find_nth_number(n-3))

print(find_nth_number(6))


