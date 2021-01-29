gmsg = "Please, tell me your number. We will check if it can be devided by 10: "
number = input(gmsg)
number = int(number)
if number % 10 == 0:
    print("The number can be devided!")
else:
    print("It can not be devided with nothing left. Sorry.")

