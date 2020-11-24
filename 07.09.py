#7.9
#sandwiches
sandwich_orders = ['hamburger', 'pastrami', 'meatball sub', 'pastrami', 'bmt', 'ham and cheese', 'pastrami']
finished_sandwiches = []
wmsg = "Pastrami sandwich could not be ordered today. Sorry for the inconvinience.\n"
print(wmsg)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    smsg = f"Current sandwich in preparation: {current_sandwich.title()}"
    print(smsg)
    finished_sandwiches.append(current_sandwich.title())
rmsg = "\nThe following sandwiches were prepared:"
print(rmsg)
for sandwich in finished_sandwiches:
    print(sandwich.title())