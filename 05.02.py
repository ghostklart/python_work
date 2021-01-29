#5.2
#1
line1 = "I need to study more."
line2 = "I need to get a good night sleep."

result = line1 == line2
print(f"1st line comparison result is: {result}.")

#2
line1 = "I need to study more."
line2 = "i need to study more."

result = line1.lower() == line2
print(f"2nd line comparison result is: {result}.")

#3
number1 = 11
number2 = 5
number3 = 94

result1 = (number3 > number2)
print(f"94 is bigger than 05: {result1}.")

result2 = (number1 < number3)
print(f"11 is lower than 94: {result2}.")

number4 = 11
result3 = (number4 >= number1)
print(f"1st number is bigger or equals 4th number: {result3}.")

#4
descr1 = 'electric'
descr2 = 'sedan'
#good car as the one i would like to have
gcar = 'tesla'

if descr1 == 'electric' and descr2 == 'sedan':
    print(f"{gcar.title()} is the car of my dreams!")

#or usage
car1 = 'lamborghini'
car2 = 'bugatti'
message = 'You have an exotic sports car!'

#my nfs car is
car = 'lamborghini'

if car == car1 or car == car2:
    print(message)

#5
#lets check what we can find in the list
my_list = ['python','kubernetes','nosql','jenkins']

new_skill = 'C#'

if new_skill not in my_list:
    print("You need to upgrade your programming skills!")

