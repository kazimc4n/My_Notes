'''
# License Plates (15 pts)

In Turkey, license plates of private vehicles must follow one of the following formats, where X denotes an alphabetic character (A-Z) and 9 denotes a digit:

* Single character: "99 X 9999" or "99 X 99999" or
* Two characters: "99 XX 999" or "99 XX 9999" or
* Three characters: "99 XXX 99" or "99 XXX 999"

Implement a function called `check_lp(plate)` which takes as input a candidate license plate (string named `plate`) and performs the following. First, `check_lp` checks if `plate` is a valid license plate. For a license plate to be valid:

* It must follow one of the 6 valid formats given above (e.g., no extra characters/digits, no missing characters/digits, lengths must be correct, etc.).
* All alphabetic characters must be uppercase.
* First two digits of the license plate correspond to the city code, e.g., Istanbul is 34, Ankara is 06, etc. Valid city codes are between 01 and 81 (both included).

If the license plate is invalid for any reason, `check_lp` should return `-1` (int).

If the license plate is valid, `check_lp` should check if the last part of the license plate (the part that comes after the alphabetic characters) is divisible by 3. If so, `check_lp` should return `True`. Otherwise, `check_lp` should return `False`.

Here are some sample function calls and their outcomes:

```
check_lp("34 EG 72843")   -->    -1
check_lp("92 A 12345")    -->    -1
check_lp("sometext")      -->    -1
check_lp("34 FG 1234")    -->    False
check_lp("35 FG 3612")    -->    True
```
'''
def check_lp(plate):
  ##############################
  ##### Start of your code #####
  ##############################
  x, y, z = plate.split(" ")

  if len(x) != 2 or not x.isdigit() or int(x) < 1 or int(x) > 81:
      return -1

  if len(y) not in [1, 2, 3] or not y.isalpha() or y != y.upper():
      return -1

  if not z.isdigit():
      return -1

  z_int = int(z)

  if len(y) == 1 and len(z) not in [4, 5]:
      return -1
  elif len(y) == 2 and len(z) not in [3, 4]:
      return -1
  elif len(y) == 3 and len(z) not in [2, 3]:
      return -1

  if z_int % 3 == 0:
      return True
  else:
      return False


if __name__ == "__main__":
  # invalid
  print("INVALID PLATE EXAMPLES (all of them should be -1): ")
  print("C1 DD 123", "-->", check_lp("C1 DD 123"))  # city code not numeric
  print("133 DD 123", "-->",
        check_lp("133 DD 123"))  # city code not between 1 and 81
  print("92 A 12345", "-->",
        check_lp("92 A 12345"))  # city code not between 1 and 81
  print("14 ABCD 123", "-->", check_lp("14 ABCD 123"))  # format problem
  print("14 A1D 123", "-->",
        check_lp("14 A1D 123"))  # middle part is not alphabetic
  print("14 ABc 123", "-->",
        check_lp("14 ABc 123"))  # middle part is not fully uppercase
  print("30 A 12345667", "-->",
        check_lp("30 A 12345667"))  # length of last part is incorrect
  print("30 A 123", "-->",
        check_lp("30 A 123"))  # length of last part is incorrect
  print("30 AA 11", "-->",
        check_lp("30 AA 11"))  # length of last part is incorrect
  print("30 AA 11111", "-->",
        check_lp("30 AA 11111"))  # length of last part is incorrect
  print("30 XYZ 1234", "-->",
        check_lp("30 XYZ 1234"))  # length of last part is incorrect
  print("30 XYZ 9", "-->",
        check_lp("30 XYZ 9"))  # length of last part is incorrect
  print("30 XYZ A2", "-->",
        check_lp("30 XYZ A2"))  # last part contains alphabetic character

  # valid
  print("====================================")
  print("VALID PLATE EXAMPLES: ")
  print(check_lp("12 A 3456"))  # True
  print(check_lp("12 B 12345"))  # True
  print(check_lp("14 CC 123"))  # True
  print(check_lp("34 DD 1234"))  # False
  print(check_lp("60 ABC 22"))  # False
  print(check_lp("61 DEF 777"))  # True


##############################
  ##### End of your code #####
  ##############################


