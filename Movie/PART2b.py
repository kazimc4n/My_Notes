'''
### B) Consider Condition 1, Print Seat Configuration.

In Part B, in addition to what you have implemented in Part A, you will return the new seat configuration after you allocated seats for the whole group if possible. If it is not, you will return 'X'.


To achieve this, you should implement a function called ```get_the_solution_C1(num_of_chars, num_of_subgroups, num_seats_in_a_slot, seat_config)``` that takes two arguments as follows:
- ```num_of_chars``` : number of characters in the group (int)
- ```num_of_subgroups``` : number of groups that they want to split into (int)
- ```num_seats_in_a_slot``` : number of seats in one slot (int)
- ```seat_config``` : current seat configuration of the cinema (string)


If it is possible to find place for the whole group, your function should return the solution. To denote that you have allocated a seat for a cartoon character, put 'S' in that index. If there is no solution, just return 'X'.


Some examples:
```
>> get_the_solution_C1(6, 3, 2, 'OO|OX|OO|XX|XO|OO')
'SS|OX|SS|XX|XO|SS'
```
```
>> get_the_solution_C1(8, 4, 4, 'OOOO|OXXO|XOXO')
'SSSS|SXXS|XSXS'
```
```
>> get_the_solution_C1(10, 2, 6, 'OOOOOO|OOOXXO|XXOOXO')
'X'                                                    # Only one subgroup can sit in the first seat slot
```

**Hint**: You can use ```replace(old,new,count)``` function for this part. After you find out how many subgroups can seat in the current seat slot, you can replace ```O```'s with ```S```'s for that seat slot. Think about handling seat slots separately, and concatenate their results.

For further information about ```replace``` function: https://www.geeksforgeeks.org/python-string-replace/


'''

def get_the_solution_C1(num_of_chars, num_of_subgroups, num_seats_in_a_slot, seat_config):
    chars_per_subgroup = num_of_chars // num_of_subgroups
    available_seats = 0
    new_seat_config = []

    seat_slots = seat_config.split("|")
#for slot
    for slot in seat_slots:
        slot_available_seats = slot.count("O") // chars_per_subgroup
        available_seats += slot_available_seats
        new_slot = slot.replace("O", "S", slot_available_seats * chars_per_subgroup)
        new_seat_config.append(new_slot)
# conditions
    if available_seats >= num_of_subgroups:
        return "|".join(new_seat_config)
    else:
        return "X"
