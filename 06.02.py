#6.2
#favorite numbers
#favorite_numbers = {
#    'sergey': 56,
#    'dimitriy': 24,
#    'damir': 94,
#    'rinat': 27,
#    'ilya': 44
#}
# creating ppl's list
favorite_ppl = []
favorite_ppl.append('sergey')
favorite_ppl.append('dimitriy')
favorite_ppl.append('damir')
favorite_ppl.append('rinat')
favorite_ppl.append('ilya')
#checkingf the list code
#print(favorite_ppl)
#creating the dictionary which is linked to list
favorite_numbers = {}
favorite_numbers[favorite_ppl[0]] = 56
favorite_numbers[favorite_ppl[1]] = 24
favorite_numbers[favorite_ppl[2]] = 94
favorite_numbers[favorite_ppl[3]] = 27
favorite_numbers[favorite_ppl[4]] = 44
#creating message outputs
smesg = f"{favorite_ppl[0].title()}'s favorite number is: {favorite_numbers[favorite_ppl[0]]}."
print(smesg)
smesg = f"{favorite_ppl[1].title()}'s favorite number is: {favorite_numbers[favorite_ppl[1]]}."
print(smesg)
smesg = f"{favorite_ppl[2].title()}'s favorite number is: {favorite_numbers[favorite_ppl[2]]}."
print(smesg)
smesg = f"{favorite_ppl[3].title()}'s favorite number is: {favorite_numbers[favorite_ppl[3]]}."
print(smesg)
smesg = f"{favorite_ppl[4].title()}'s favorite number is: {favorite_numbers[favorite_ppl[4]]}."
print(smesg)

