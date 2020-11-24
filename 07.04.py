while True:
    dmsg = "Please, type your topping: "
    topping = input(dmsg)
    if topping == 'quit':
        break
    else:
        smsg = f"{topping.title()} were added to cart!"
        print(smsg)