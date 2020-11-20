#5.11
#number in range
numbers = [number for number in range(1,10)]
#checking the list
#print(numbers)
#1st, 2nd, 3rd ... 4th 5th ... th
if numbers:
    for number in numbers:
        if number == 1:
            print(f"{number}st")
        elif number == 2:
            print(f"{number}nd")
        elif number == 3:
            print(f"{number}rd")
        else:
            print(f"{number}th")