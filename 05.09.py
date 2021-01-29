#5.9
#list of users
users = []
#users.append('admin')
#users.append('damir')
#users.append('sergey')
#users.append('dimitriy')
#users.append('ilya')
#special message

if users:
    for user in users:
        if user == 'admin':
            hmesg = f"Hello {user.upper()}, would you like to see the status report?"
            print(hmesg)
        else:
            hmesg = f"Welcome back {user}!"
            print(hmesg)
else:
    smesg = "We need to find some users!" 
    print(smesg)

