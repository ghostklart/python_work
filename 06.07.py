#6.7
#favorite languages
favorite_langauges = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
#people to pass the test
ppl_tst = [
    'sergey',
    'sarah',
    'phil',
    'damir',
    'andrey'
]
#cycle to check
for ppl in ppl_tst:
    if ppl in favorite_langauges.keys():
        wmsg = f"{ppl.title()}, thank you for participating!"
        print(wmsg)
    else:
        smsg = f"Dear {ppl.title()}, please take our poll!"
        print(smsg)