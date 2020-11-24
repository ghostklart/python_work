#06.11.py
#cities
cities = {
	'moscow': {
		'country': 'russia',
		'population': 11_920_000,
		'fact': 'kremlin'
	},
	'tokyo': {
		'country': 'japan',
		'population': 9_273_000,
		'fact': 'keio plaza'	
	},
	'new york': {
		'country': 'usa',
		'population': 8_399_000,
		'fact': 'statue of liberty'
	}
}
#print(cities)
for city, info in cities.items():
	cit = city.title()
	message = f"Important information about {cit} is:"
	print(message)
	coun = info['country']
	popul = info['population'] 
	fac = info['fact']
	coun_sen = f"\tis located in {coun.title()}"
	popul_sen = f"\n\t{popul} people lives there"
	fac_sen = f"\n\ticonic place is: {fac.title()}"
	imsg = f"{coun_sen}{popul_sen}{fac_sen}"
	print(imsg)

