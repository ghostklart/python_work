#adding prompts for messages
prompt_0 = "Please, specify your message: "
#end

#creating a list of messages
messages_list = []
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

show_messages()