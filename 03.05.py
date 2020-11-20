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


