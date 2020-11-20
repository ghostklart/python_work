#5.5
#colors 3

alien_color = 'red'
#status message
statmsg = "Your points:"

point1 = 5
point2 = 10
point3 = 15

if alien_color == 'green':
    points = point1
    print(f"{statmsg} {points}!")
elif alien_color == 'yellow':
    points = point2
    print(f"{statmsg} {points}!")
else:
    points = point3
    print(f"{statmsg} {points}!")