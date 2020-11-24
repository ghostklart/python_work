#06.10.py
#favorite_numbers
#copy-paste 06.02.py
# creating ppl's list
favorite_ppl = []
favorite_ppl.append('sergey')
favorite_ppl.append('dimitriy')
favorite_ppl.append('damir')
favorite_ppl.append('rinat')
favorite_ppl.append('ilya')
#creating the dictionary which is linked to list
favorite_numbers = {}
favorite_numbers[favorite_ppl[0]] = [56, 22, 33]
favorite_numbers[favorite_ppl[1]] = [24, 12, 40]
favorite_numbers[favorite_ppl[2]] = [94, 33, 90]
favorite_numbers[favorite_ppl[3]] = [27, 5, 96]
favorite_numbers[favorite_ppl[4]] = [44, 6, 9]

#print(favorite_numbers)

for name, numbers in favorite_numbers.items():
	fname = name.title()
	message = f"{fname} favorite numbers are:"
	print(message)
	for number in numbers:
		print("\t" + str(number))