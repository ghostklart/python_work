#09.02.py

class Restaurants():

    def __init__(self, rest_name, cuisine_type):
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type    
    
    def describe_restaurant(self):
        smsg = f"Restaurant's info: {self.rest_name} with {self.cuisine_type} cuisine."
        print(smsg)

    def open_restaurant(self):
        message = f"The {self.rest_name} is open!"

# three restaurants

rest_1 = Restaurants('Burger King', 'fastfood')
rest_2 = Restaurants('Tanuki', 'sushi')
rest_3 = Restaurants('BBQ Cafe', 'American')

rest_1.describe_restaurant()
rest_2.describe_restaurant()
rest_3.describe_restaurant()