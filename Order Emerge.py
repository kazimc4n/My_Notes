'''
Order Emerging Out of Randomness

1. (**7 pts**) Generate a million random pairs of numbers between 0 and 1. A certain ratio of pairs, x and y, will adhere to the following condition:

> x\*x + y\*y <= 1

For example:

> x = 0.1, y = 0.2 adheres to the condition because 0.1\*0.1 + 0.2\*0.2 (=0.05) <= 1
>
> x = 0.9, y = 0.8 does not adhere to the condition because 0.9\*0.9 + 0.8\*0.8 (=1.45) > 1

Find the ratio of the number of pairs that adhere to the condition over all pairs. Implement your answer in "q2.py" under  `compute_ratio()`.

2. (**3 pts**) Amazingly, the ratio that you found in the first part converges to π/4. Use that information to calculate the approximate value of π and then compare it to the value of π in the math module (`math.pi`). Report your error as the absolute difference between the two values. Implement your solution in "q2.py" under `compute_error()`.

Sample execution for Parts 1 and 2 combined (note that your output can be somewhat different, since you are generating random numbers):

```
Ratio: 0.785868
Absolute difference: 0.001879346410206928
```
'''

import math
import random
def compute_ratio():
    ##############################
    ##### Start of your code #####
    ##############################
    count_inside = 0
    num_samples = 1000000
    for _ in range(num_samples):
        x = random.random()
        y = random.random()

        if x * x + y * y <= 1:
            count_inside += 1

    ratio = count_inside / num_samples
    return ratio

    ##############################
    ##### End of your code #####
    ##############################


def compute_error(ratio):
    ##############################
    ##### Start of your code #####
    ##############################
    abs_diff = abs(math.pi - ratio)

    return abs_diff

    ##############################
    ##### End of your code #####
    ##############################


if __name__ == "__main__":
    ratio = compute_ratio()
    abs_diff = compute_error(ratio)
    print('Ratio:', ratio)
    print('Absolute difference', abs_diff)
