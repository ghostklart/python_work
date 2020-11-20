#4.12
#foods.py
my_foods = ['pizza','falafel','carrot cake']
friends_foods = my_foods[:]
friends_foods.append('soup')

print("My favorite foods are:")
for mfood in my_foods:
	print(mfood)

print("\nMy friends favorite foods are:")
for ffood in friends_foods:
	print(ffood)