def make_shirt(size='L', text='I love Python'):
    rmsg = f"You have ordered a {size.title()} shirt with '{text}' print on it!"
    print(rmsg)


size = input("What size you are (L is default): ")
if size == "":
    size = 'L'
text = input("What text would you like to have printed ('I love Python' is default): ")
if text == "":
    text = 'I Love Python'
make_shirt(size, text)
