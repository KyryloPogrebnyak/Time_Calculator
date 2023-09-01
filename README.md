# Time_Calculator
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/GECHMxxT)
# Create a Time Calculator


1. Function named (add_time) takes in two required parameters and one optional parameter:
   - a start time in the 12-hour clock format (ending in AM or PM)
   -  a duration time that indicates  the  number of hours and minutes
   -  (optional) a starting day of the week, case insensitive
  
2. The function add the duration time to the start time and return the result.
3. If the result will be the next day, it show (next day) after the time. If the result will be more than one day later, it show (n days later) after the time, where "n" is the number of days later.
4. If the function is given the optional starting day of the week parameter, then the output display the day of the week of the result. The day of the week in the output appear after the time and before the number of days later.
5. Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results:
 
```
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```
