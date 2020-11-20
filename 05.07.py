#5.7
#favorite fruits
#initial list
favorite_fruits = []
favorite_fruits.append('orange')
favorite_fruits.append('banana')
favorite_fruits.append('apple')
favorite_fruits.append('kiwi')
favorite_fruits.append('strawberry')
#fruits to check
message = "You really like"
check1 = 'pineapple'
check2 = 'grape'
check3 = 'blueberry'
check4 = 'peach'
check5 = 'orange'
#checkings
if check1 in favorite_fruits:
    dmesg = f"{message} {check1}s!"
    print(dmesg)
if check2 in favorite_fruits:
    dmesg = f"{message} {check2}s!"
    print(dmesg)
if check3 in favorite_fruits:
    dmesg = f"{message} {check3}s!"
    print(dmesg)
if check4 in favorite_fruits:
    dmesg = f"{message} {check4}s!"
    print(dmesg)
if check5 in favorite_fruits:
    dmesg = f"{message} {check5}s!"
    print(dmesg)