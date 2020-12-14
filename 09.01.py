#9.1 restaurants
class Restaurants():

    def __init__(self, rest_name, cuisine_type):
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type    
    
    def describe_restaurant(self):
        smsg = f"Restaurant's info: {self.rest_name} with {self.cuisine_type} cuisine."
        print(smsg)

    def open_restaurant(self):
        message = f"The {self.rest_name} is open!"
        print(message)

my_restaurant = Restaurants('McDonalds', 'fastfood')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()