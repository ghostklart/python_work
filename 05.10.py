#5.10
#current_users
current_users = []

current_users.append('damir')
current_users.append('sergey')
current_users.append('dimitriy')
current_users.append('alexey')
current_users.append('ilya')

#new_users
new_users = []

new_users.append('IlyA')
new_users.append('anna')
new_users.append('anastasiya')
new_users.append('tatyana')
new_users.append('serGey')

for new_user in new_users:
    if new_user.lower() not in current_users:
        hmesg = f"Welcome to my portatl {new_user.title()}!"
        print(hmesg)
    elif new_user.lower() in current_users:
        hmesg = f"Dear user, please select another username!"
        print(hmesg)