glist = []
glist.append('sergey')
glist.append('mikhail')
glist.append('dmitriy')
#print(glist)

message = 'Thank you for coming to my dinner,'

nmesg = "will not be coming today!"
print(f"{glist[1].title()} {nmesg}")

glist[1] = 'alexey'
#print(glist)

fmesg = f"{message} {glist[0].title()}!"
print(fmesg)

fmesg = f"{message} {glist[1].title()}!"
print(fmesg)

fmesg = f"{message} {glist[2].title()}!"
print(fmesg)

amesg = "More people will attend my dinner today!"
print(amesg)

glist.insert(0,'tanya')
glist.insert(2,'sasha')
glist.append('daria')

#print(glist)

fmesg = f"{message} {glist[0].title()}!"
print(fmesg)

fmesg = f"{message} {glist[2].title()}!"
print(fmesg)

fmesg = f"{message} {glist[5].title()}!"
print(fmesg)

