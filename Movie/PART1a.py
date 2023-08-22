'''

- Movie Theater

In this problem set, you will use *conditional statements*, *string operations*, and *functions* to help Tom, Jerry, and their group of cartoon friends find cinema seats in a movie theater.

Tom, Jerry, and their friends are going to watch a movie in the only cinema in the city. The cinema has seats arranged in a single row with small corridors separating the slots of seats. Each slot of seats is separated by a corridor and contains the same number of seats.

## String Representation of the Movie Theater
Cinema seats and corridors will be denoted by different characters:
- ```'O'``` denotes an empty seat,
- ```'X'``` denotes an occupied seat,
- ```'|'``` denotes a corridor.
- ```'S'``` denotes seats that are allocated for cartoon characters from Tom and Jerry's group.

#### Examples:
- 6 empty seats separated by 2 corridors:
```
 OO|OO|OO
```
- 6 seats, first two and the last two are occupied, separated by a corridor:
```
 XXO|OXX
```
Notice that each seat slot has equal number of seats.


## PART 1: Find Seats for the Group (25 pts)

In Part 1, there are no special conditions when allocating seats for the members of the cartoon group. Whenever an empty seat ```'O'``` is encountered, it should be immediately allocated to one of the group members.



### A) Return YES or NO

For Part A, given the number of cartoon characters in the group and the current seat configuration of the movie theater, you need to check if there is an available seat configuration for the group.

To achieve this, you should implement a function called ```is_there_a_solution(num_of_chars, seat_config)``` that takes two arguments as follows:
- ```num_of_chars``` : number of characters in the group (int)
- ```seat_config``` : current seat configuration of the movie theater (string)

If it is possible to find enough seats for the whole group, your function should return 'YES'. Otherwise, it should return 'NO'.



Some examples:
```
>> is_there_a_solution(7, 'OO|OX|OO|XX|XO|OO')
'YES'                                              # The solution is 'SS|SX|SS|XX|XS|SO'
```
```
>> is_there_a_solution(8, 'OOOO|OXXO|XOXO|OOXX')
'YES'                                              # The solution is 'SSSS|SXXS|XSXS|OOXX'
```
```
>> is_there_a_solution(3, 'O|X|X|O')
'NO'                                               # There are no enough available seats.

'''

def is_there_a_solution(num_of_chars, seat_config):
    available = 0
    for i in seat_config:
        if i == "O":
            available += 1

    if available >= num_of_chars:
        return "yes"
    else:
        return "No"

print(is_there_a_solution(3, 'O|X|X|O'))