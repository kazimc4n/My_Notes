'''
# Bamboo Height
[The bamboo is the fastest growing plant in the world, but exactly how fast does it grow?](https://cozyearth.com/blogs/news/how-bamboo-grows)

A new bamboo shoot emerges and reaches its full height at a record-breaking speed. According to Guinness World Records, some species of bamboo can grow up to 88.6968 cm in a single day. That means it grows almost 3.6957 cm every hour! In general, it takes a bamboo shoot 60 days to reach its adult height.

1. (**5 pts**) Your first task is to write a function to report the height of a bamboo shoot as it grows. Report the result according to the given number of days and hours since it started growing.

```
bamboo_height(days, hours)
```

where `days` can take integer values from 0 until 60, [0, 60), and `hours` can take integer values from 0 until 24, [0, 24). Use the statistics provided above for the growth, i.e. 88.6968 cm per day, 3.6957 cm per hour.

2. (**5 pts**) Next, write a function to report the bamboo growth in requested intervals, for example, every `6 hours`, using your implementation of `bamboo_height` from the first part.

```
bamboo_growth(freq)
```

`freq` is a string in the form of "x hours" or "xx hours" or "x days" or "xx days", where x is a digit (xx is two digits).

* If `freq` is of the form "x hours" or "xx hours", then `hours` is between 0 and 24, [0, 24). In this case, you should print the growth in a single day (up to, but not including hour number 24).
* If `freq`is of the form "x days" or "xx days", then `days` is between 0 and 60, [0, 60). In this case, you should print the growth until the end of 60 days (up to, but not including day number 60).

```
Bamboo growth every 4 hours:
Hour 0: 0.00 cm
Hour 4: 14.78 cm
Hour 8: 29.57 cm
Hour 12: 44.35 cm
Hour 16: 59.13 cm
Hour 20: 73.91 cm
```

```
Bamboo growth every 10 days:
Day 0: 0.00 cm
Day 10: 886.97 cm
Day 20: 1773.94 cm
Day 30: 2660.90 cm
Day 40: 3547.87 cm
Day 50: 4434.84 cm
```

3. (**5 pts**) Write a function to report when exactly the bamboo plant will be at a certain height.
Your function should return the time in days and hours that are needed to reach that height:
```
num_days, num_hours = bamboo_quando_quando(height)
```

Report the days as an integer and hours as a floating point number:
> It takes 15 days and 22.07 hours to reach the height of 1412 cm.

Note that when hours reach 24, it should be considered 1 day. So, hours should not be >= 24 in your answer.
'''

def bamboo_height(days, hours):
    height = 0
    if (0 <= days < 60) and (0 <= hours < 24):
        height = 88.6968 * days + 3.6957 * hours
    return format(height,".2f")

print(bamboo_height(12,20))


def bamboo_growth(freq: int, day_hour: str):
    result = ""

    if day_hour == "hours":
        for i in range(0, 24, freq):
            result += "Hour {}: {}\n".format(i, bamboo_height(0, i))
    elif day_hour == "days":
        for i in range(0, 60, freq):
            result += "Days {}: {}\n".format(i, bamboo_height(i, 0))

    return result

print(bamboo_growth(10,"days"))

def bamboo_quando_quando(height):
    num_days = height // 88.6968
    num_hours = (height - (num_days * 88.6968)) / 3.6957
    num_hours = format(num_hours,".2f")

    return "It takes {} days and {} hours to reach the height of {} cm.".format(int(num_days),num_hours,height)

print(bamboo_quando_quando(1412))