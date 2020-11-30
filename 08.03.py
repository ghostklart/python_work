def make_shirt(size, text):
    rmsg = f"You have ordered a {size} size shirt with '{text}' print!"
    print(rmsg)
prompt_0 = "What size are you: "
prompt_1 = "What text would you like to have printed on: "
size = input(prompt_0)
text = input(prompt_1)
make_shirt(size, text)
