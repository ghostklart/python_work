#6.7
#multi dictionary
person_0 = {
    'first_name': 'alexander',
    'last_name': 'hamilton',
    'city': 'london',
    'age': 16
}

person_1 = {
	'first_name': 'aaron',
	'last_name': 'burr',
	'city': 'new york',
	'age': 21
}

person_2 = {
	'first_name': 'luke',
	'last_name': 'skywalker',
	'city': 'tatooine',
	'age': 18
}

people = (
	person_0,
	person_1,
	person_2
	)

#print(people)
#for person in people:
#	print(person)

for person in people:
	full_name = person['first_name'] + " " + person['last_name']
	age = person['age']
	location = person['city']
	message = f"{full_name.title()} at the age of {age} lives in {location.title()}."
	print(message)