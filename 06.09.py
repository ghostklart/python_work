#06.09.py
#favorite_places
favorite_places = {
	'michael': ['eifel tower','liberty statue','kremlin'],
	'tony': ['mcDonalds'],
	'tom': ['musical studio','nasa']
}
#process
for name, places in favorite_places.items():
	nname = name.title()
	message = f"{nname.title()}'s favorite place is:"
	print(message)
	for place in places:
		print("\t" + place.title())

