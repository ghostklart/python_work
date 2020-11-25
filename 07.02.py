prompt = "How many people will be attending the dinner today? "
ppl = input(prompt)
number = int(ppl)
if number > 8:
    wmsg = "You will have to wait for 15 minutes."
    print(wmsg)
else:
    smsg = "Please, enjoy your dinner!"
    print(smsg)