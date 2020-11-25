def describe_city(city = 'moscow', country = 'russia'):
    rmsg = f"{city.title()} is the capital of {country.title()}."
    print(rmsg)


describe_city(city = 'rome')
describe_city(country = 'france')
describe_city(city = 'madrid', country = 'spain')