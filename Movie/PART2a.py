"""
## PART 2: Find Seats for the Subgroups (75 pts)

In Part 2, the cartoon group wants to sit together but they are aware of the fact that finding adjacent seats for the whole group is a bit challenging. That is why they decide to split into k subgroups, with each subgroup having an equal number of cartoon characters, and they will look for adjacent seats for these subgroups separately. You can assume that they will split equally.

Assuming they are split into k equal subgroups, each subgroup wants to find seats for themselves while considering some conditions. We define two conditions as following:

- **Condition 1**: The members of **each subgroup should sit in the same seat slot** *without separated by a corridor*. Different subgroups can also sit in the same seat slot if there are enough seats available.

  Some example cases:
  - There are 6 cartoon characters in the group. They are split into 2-2-2 subgroups, and the seat configuration is ```OOOO|XOXO```.  The solution is ```SSSS|XXSS```.
  - There are 6 cartoon characters in the group. They are split into 2-2-2 subgroups, and the seat configuration is ```OOO|XXO|OOX```. The first subgroup can sit in the first seat slot (the leftmost one), and the second subgroup can sit in the last seat slot (the rightmost one). However, there are no available seats for the last subgroup. In this case, there is no solution.

- **Condition 2**: The members of **each subgroup should sit next to each other** *without separated by a corridor or other people*.
  Some example cases:
  - There are 6 cartoon characters in the group. They are split into 2-2 subgroups, and the seat configuration is ```OOOO|XXOO```. The solution is ```SSSS|XXSS```.
  - There are 6 cartoon characters in the group. They are split into 2-2-2 subgroups, and the seat configuration is ```OOOO|XOXO```. Although two subgroups can sit in the first slot, the third subgroup can't since they cannot sit adjacently in the second seat slot. There is no solution.
A) Consider Condition 1, Return YES or NO.

For Part A, given the number of cartoon characters in the group, subgroups and seats in one slot and the current seat configuration of the cinema, you will check if you can allocate seats for every subgroup considering **Condition 1**.

To achieve this, you should implement a function called ```is_there_a_solution_C1(num_of_chars, num_of_subgroups, num_seats_in_a_slot, seat_config)``` that takes two arguments as follows:
- ```num_of_chars``` : number of characters in the group (int)
- ```num_of_subgroups``` : number of groups that they want to split into (int)
- ```num_seats_in_a_slot``` : number of seats in one slot (int)
- ```seat_config``` : current seat configuration of the cinema (string)

If it is possible to find place for every subgroup, your function should return 'YES'. Otherwise, return 'NO'.

Some examples:
```
>> is_there_a_solution_C1(6, 3, 2, 'OO|OX|OO|XX|XO|OO')
'YES'                                                    # The solution is 'SS|OX|SS|XX|XO|SS'
```
```
>> is_there_a_solution_C1(8, 4, 4, 'OOOO|OXXO|XOXO')
'YES'                                                    # The solution is 'SSSS|SXXS|XSXS'
```
```
>> is_there_a_solution_C1(10, 2, 6, 'OOOOOO|OOOXXO|XXOOXO')
'NO'                                                    # Only one subgroup can sit in the first seat slot
```
"""
def is_there_a_solution_C1(num_of_chars: int, num_of_subgroups: int, num_seats_in_a_slot: int, seat_config: str):
    chars_per_subgroup = num_of_chars // num_of_subgroups
    available_seats = 0

    seat_slots = seat_config.split("|")

    for slot in seat_slots:
        available_seats += slot.count("O") // chars_per_subgroup

    return "YES" if available_seats >= num_of_subgroups else "NO"

result = is_there_a_solution_C1(10, 2, 6, 'OOOOOO|OOOXXO|XXOOXO')

print(result)
