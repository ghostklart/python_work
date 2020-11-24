#06.08.py
#create list
pets = []
#create pets
pet = {
	'name': 'lucker',
	'animal_type': 'dog',
	'owner': 'tony',
	'age': 2
}
pets.append(pet)
#2
pet = {
	'name': 'lazyboy',
	'animal_type': 'turtle',
	'owner': 'courtney',
	'age': 1
}
pets.append(pet)
#3
pet = {
	'name': 'charlie',
	'animal_type': 'cat',
	'owner': 'damir',
	'age': 7	
}
pets.append(pet)
#list
for pet in pets:
	pname = pet['name']
	tanimal = pet['animal_type']
	aown = pet['owner']
	aage = pet['age']
	message = f"{pname.title()}'s owner is {aown.title()}. It's a {tanimal} which is {aage} years old."
	print(message)