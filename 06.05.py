#6.5
#rivers
rivers = {
    'nile': 'egypt',
    'amazon': 'america',
    'moskva': 'russia'
}
#print cycle
for river, country in rivers.items():
    message = f"The {river.title()} runs through {country.title()}."
    print(message)
#print cycle only river names
mesg = "\nThe rivers in the list are:"
print(mesg)
for river in rivers.keys():
    smesg = f"{river.title()}"
    print(smesg)
#print country names
mesg = "\nThe countries in the list are:"
print(mesg)
for country in rivers.values():
    smesg = f"{country.title()}"
    print(smesg)