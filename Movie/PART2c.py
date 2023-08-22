'''
### C) Consider Condition 2, Return YES or NO.

For Part C, given the number of cartoon characters in the group, subgroups and seats in one slot and the current seat configuration of the cinema, you will check if you can allocate seats for every subgroup considering **Condition 2**.

To achieve this, you should implement a function called ```is_there_a_solution_C2(num_of_chars, num_of_subgroups, num_seats_in_a_slot, seat_config)``` that takes two arguments as follows:
- ```num_of_chars``` : number of characters in the group (int)
- ```num_of_subgroups``` : number of groups that they want to split into (int)
- ```num_seats_in_a_slot``` : number of seats in one slot (int)
- ```seat_config``` : current seat configuration of the cinema (string)

If it is possible to find place for every subgroup, your function should return 'YES'. Otherwise, return 'NO'.

Some examples:
```
>> is_there_a_solution_C2(6, 3, 2, 'OO|OX|OO|XX|XO|OO')
'YES'                                                    # The solution is 'SS|OX|SS|XX|XO|SS'.
```
```
>> is_there_a_solution_C2(8, 4, 4, 'OXXO|OXXO|OOOO')
'NO'                                                    # Only two subgroups can sit in the 3rd seat slot.
```
```
>> is_there_a_solution_C2(12, 3, 6, 'OOOOOO|OOXXO|XOOOOX')
'NO'                                                    # Only two subgroup can sit at the 1st and 3rd slot.
```
'''

def is_there_a_solution_C2(num_of_chars, num_of_subgroups, num_searts_in_a_slot, seat_config):
    chars_per_subgroup = num_of_chars // num_of_subgroups
    available_seats = 0

    seat_slots = seat_config.split("|")

    for slot in seat_slots:
        if "O" * chars_per_subgroup in slot:
            available_seats += 1
#conditions
    if available_seats >= num_of_subgroups:
        return "YES"
    else:
        return "NO"
