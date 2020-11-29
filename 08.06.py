def city_country():
	prompt_0 = "Please, name the country: "
	prompt_1 = "Please, name the city: "
	country = input(prompt_0)
	city = input(prompt_1)
	message = f"{city.title()}, {country.title()}."
	print(message)
city_country()