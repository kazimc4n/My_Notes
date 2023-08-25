'''
## Count substring

Write a **recursive** function called `count_substring(s, target)`. The function should return the number of times target string appears as a substring in s.

For example, if the input strings are `s = "hellohello"` and `target = "ell"`, the function should return 2, because the substring "ell" appears twice in "hellohello".

**Example outputs:**
```
print(count_substring("hellohello", "ell")) # -> 2
print(count_substring("aaaa", "aa")) # -> 3
print(count_substring("abababab", "aba")) # -> 3
print(count_substring("abababab", "cc")) # -> 0
```
'''
def count_substring(s, target):
    count = 0

    if s[:len(target)] == target:
        count = 1

    if len(s) < len(target):
        return 0

    return count + count_substring(s[1:],target)

print(count_substring("abababab", "aba")) # -> 3
