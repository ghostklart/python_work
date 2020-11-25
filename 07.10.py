#7.10
#vacation
responses = {}
prompt_0 = "\nWhat is your name? "
prompt_1 = "Where would you like to spend your vacation? "
#qmsg for question message
qmsg = "\nIf you would like to stop the program, please type: 'quit' (without quotes)."
print(qmsg)

polling_active = True

while polling_active:
    name = input(prompt_0)
    country = input(prompt_1)
    if name == 'quit':
        print("Quitting program. Thank you for your assistance!")
        polling_active = False
        break
    elif country == 'quit':
        print("Quitting program. Thank you for your assistance!")
        polling_active = False
        break
    responses[name] = country
    rmsg = "Would you like to let other person respond? (yes/no) "
    #repeat variable for put result
    repeat = input(rmsg)
    if repeat == 'quit':
        polling_active = False
        print("Quitting program. Thank you for your assistance!")
        break
    elif repeat == 'no':
        polling_active = False
    elif repeat == 'yes':
        polling_active = True
    else:
        emsg = "Error, stopping..."
        print(emsg)
        break
smsg = "\nPolling over, here are the results:\n"
print(smsg)
for name, country in responses.items():
    rmsg = f"{name.title()} would like to visit {country.title()}."
    print(rmsg)
