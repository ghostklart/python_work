#5.8
#list of users
users = []
users.append('admin')
users.append('damir')
users.append('sergey')
users.append('dimitriy')
users.append('ilya')
#special message
for user in users:
    if user == 'admin':
        hmesg = f"Hello {user.upper()}, would you like to see the status report?\n"
        print(hmesg)
    else:
        hmesg = f"Hello {user.title()}, thank you for logging in again!\n"
        print(hmesg)

