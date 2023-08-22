'''
B) Return Seat Configuration

In Part B, in addition to what you implemented in Part A, you need to return the new seat configuration after allocating seats for the whole group if possible. If it is not possible to allocate enough seats for the entire group, you should return 'X'.

**Important Note:** Starting from the leftmost seat, please allocate the first empty seats and do not skip any empty seats. You will be graded based on these solutions. For example, if you want to allocate seats for 3 characters in the seat configuration ```OO|OX|OX```, you should allocate the first three empty seats from the left. The correct solution would be ```SS|SX|OX```. ```SS|OX|SX``` will not be accepted as an answer.

You should implement a function called ```get_the_solution(num_of_chars, seat_config)``` that takes two arguments as follows:
- ```num_of_chars``` : number of characters in the group (int)
- ```seat_config``` : current seat configuration of the movie theater (string)

If it is possible to find enough seats for the entire group, your function should return the solution. To denote that you have allocated a seat for a cartoon character, put 'S' in that index. If there is no solution, just return 'X'.

Some examples:
```
>> get_the_solution(7, 'OO|OX|OO|XX|XO|OO')
'SS|SX|SS|XX|XS|SO'
```
```
>> get_the_solution(8, 'OOOO|OXXO|XOXO|OOXX')
'SSSS|SXXS|XSXS|OOXX'
```
```
>> get_the_solution(3, 'O|X|X|O')
'X'                                               # There are no enough available seats.
```

**Hint**: You can use the ```replace(old, new, count)``` function to replace occurrences of a character in a string. After you have determined that there is a solution, you can replace the 'O's with 'S's using this function.

For further information about the replace() function, you can refer to the Python documentation or other relevant resources such as: https://www.geeksforgeeks.org/python-string-replace/


'''

def get_the_solution(num_of_chars, seat_config: str):
    available = 0
    for i in seat_config:
        if i == "O":
            available += 1

    if available >= num_of_chars:
        seat_config = seat_config.replace("O","S",num_of_chars)

    else:
        return "X"

    return seat_config

print(get_the_solution(7, 'OO|OX|OO|XX|XO|OO'))

