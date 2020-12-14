#09.03.py

class User():

    def __init__(self, first_name, last_name, age, nickname):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nickname = nickname

    def describe_user(self):
        imsg = f"""{self.first_name} {self.last_name}'s nickname is: '{
        self.nickname}'. He is {self.age} years old."""
        print(imsg)

    def greet_user(self):
        gmsg = f"""Greetings, dear '{self.nickname}'!"""
        print(gmsg)

user_1 = User('Andy', 'Warholl', 52, 'wandy')
user_2 = User('Alexander', 'Hamilton', 16, 'alex')
user_3 = User('Daniel', 'Humphrey', 15, 'gossip_girl')

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()