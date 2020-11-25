#7.5
#tickets to the cinema
while True:
    prompt = "Please, specify your age to get the ticket price: "
    age = input(prompt)
    if age == 'quit':
        print("Stopping the process!")
        break
    age = int(age)
    if age <= 3:
        price = "Free"
        print(price)
    elif age >=3 and age <= 12:
        price = "$10"
        print(price)
    elif age > 12:
        price = "$15"
        print(price)