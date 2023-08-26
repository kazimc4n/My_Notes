'''
## Q1: Parent List

If a list contains all the elements of another list at any order, we call that list a *parent list*.

Your task is to implement a Python function that takes in two lists as arguments and determines whether the first list is a parent of the second list. If it is, the function should return True, otherwise it should return False.


```
is_parent_list([1, 2, 3, 4], [1, 3]) --> True
```
```
is_parent_list([1, 1, 2, 1, 2, 3], [1, 1, 1, 2]) --> True
```
```
is_parent_list([1, 2], [1, 2, 3, 4]) --> False

'''
def is_parent_list(a:list,b:list):
    for i in b:
        if i not in a:
            return False
        else:
            a.remove(i)
    return True



print(is_parent_list([1,2,2,3], [1,2,2,2,3]))
