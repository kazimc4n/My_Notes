'''
Q1: List Average Below Threshold

Write a function called ```average_below_threshold``` that takes a *list of integers* as input, along with a *threshold value*, and returns the average of all the values in the list that are **strictly less than the given threshold**. Round the result down to the nearest integer using integer division. If there are no values less than the threshold, return 0.

Sample executions:

```
average_below_threshold([1, 2, 3, 4, 100], 1) → 0
```

```
average_below_threshold([1, 1, 5, 5, 10, 8, 7], 5) → 1
```

```
average_below_threshold([10, 15, 8, 20, 12, 5, 18, 3, 7], 10) → 5
```
'''
def average_below_threshold(s,target):
    count = 0
    num = 0
    for i in s:
        if i < target:
            count += i
            num += 1
    if num == 0:
        return 0
    count /= num
    return int(count)

print(average_below_threshold([10, 15, 8, 20, 12, 5, 18, 3, 7], 10))

