#testing code in order to remember while cycle
prompt = "Hi, user! Say something to me and I'll repeat it back to you."
prompt += "\nType 'quit' to end it: "
message = "" #starting the cycle, important
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print("Ending...")
    print(message)


