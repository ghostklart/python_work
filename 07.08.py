#7.8
#sandwiches
sandwich_orders = ['hamburger','meatball sub','bmt','ham and cheese']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    smsg = f"Current sandwich in preparation: {current_sandwich.title()}"
    print(smsg)
    finished_sandwiches.append(current_sandwich.title())
rmsg = "\nThe following sandwiches were prepared:"
print(rmsg)
for sandwich in finished_sandwiches:
    print(sandwich.title())