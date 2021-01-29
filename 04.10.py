cubes = [value**3 for value in range(1,11)]

print(cubes)

message = "The first three items in the list are:"
print(message)
for cube in cubes[:3]:
	print(cube)

message1 = "The first three items from the middle of the list are:"
print(message1)
for cube in cubes[4:7]:
	print(cube)

message2 = "The last three items in the list are:"
print(message2)
for cube in cubes[7:11]:
	print(cube)

