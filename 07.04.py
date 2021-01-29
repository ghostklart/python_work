while True:
    dmsg = "Please, type your topping. \nType 'quit' to end the procedure: "
    toppings = []
    topping = input(dmsg)
    if topping == 'quit':
        print(f"Your pizza will contain: {toppings}.")
        break
    else:
        toppings.append(topping)
        smsg = f"{topping.title()} were added to cart."
        print(smsg)

