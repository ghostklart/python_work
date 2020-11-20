pizzas = []
pizzas.append('margarita')
pizzas.append('peperonni')
pizzas.append('quatro formagi')
#print(pizzas)
my_pizzas = pizzas[:]
friend_pizzas = pizzas [:]
#print(my_pizzas)
#print(friend_pizzas)
my_pizzas.append('carbonara')
friend_pizzas.append('ballognese')
#first string
print("My favorites pizzas are:")
for mpizza in my_pizzas:
	print(mpizza.title())
#second string
print("My friend's favorite pizzas are:")
for mfpizza in friend_pizzas:
	print(mfpizza.title())