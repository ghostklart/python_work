#adding prompts for messages
prompt_0 = "Please, specify your message: "
#end

#creating a list of messages
messages_list = []
sent_messages = []
#

#adding messages to list with prompts
def add_message():
    message = input(prompt_0)
    messages_list.append(message)

add_message()
add_message()
add_message()

#
def show_messages():
    for message in messages_list:
        print(message.title())

#adding sent messages function
def send_messages():
    while messages_list:
        current_message = messages_list.pop()
        smsg = f"Sending: '{current_message}'"
        print(smsg)
        sent_messages.append(current_message)

for lmsg in messages_list:
    send_messages()
print("Sending complete\n")

print("Results:")

rmsg = "\nNot sent items:"
print(rmsg)
for lmsg in messages_list:
    print(lmsg)

rmsg = "\nSent items:"
print(rmsg)
for sent_msg in sent_messages:
    print(sent_msg)