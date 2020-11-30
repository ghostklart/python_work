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
#needed to edit the function, so it uses the copy of the original list without
#modifying it. thats a bummer...
def send_messages(messages_list, sent_messages):
    while messages_list:
        current_message = messages_list.pop()
        smsg = f"Sending: '{current_message}'"
        print(smsg)
        sent_messages.append(current_message)

#showing all messages
show_messages()

#specifying the copy of the list
send_messages(messages_list[:], sent_messages)

print("Sending complete\n")

print("Results:")

#rmsg = "\nNot sent items:"
#print(rmsg)
#for lmsg in messages_list:
#    print(lmsg)

rmsg = "\nSent items:"
print(rmsg)
for sent_msg in sent_messages:
    print(sent_msg)

print("\nChecking tasks results:")
print(messages_list)
print(sent_messages)