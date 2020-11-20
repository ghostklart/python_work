#list of phones
phones = []
#using append function
phones.append('iphone')
phones.append('oneplus')
phones.append('samsung')
phones.append('huawei')
print(phones)
#using sort function
print(sorted(phones))
print(sorted(phones,reverse=True))
#using del function
del phones[3]
print(phones)
#using pop function
print(phones)
popped_phone = phones.pop()
print(phones)
#using insert function
phones.insert(2,popped_phone)
print(phones)
#using len function
counter = len(phones)
print(counter)
#using reverse function
phones.reverse()
print(phones)
#using sort function
phones.sort()
print(phones)
phones.sort(reverse=True)
print(phones)
# remove
expensive = 'iphone'
phones.remove(expensive)
print(phones)