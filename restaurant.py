class Restaurant():
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type;
        self.count = 5


    def describe(self):
        print("restaurant name is "+self.name)
        print("cuisine type is " + self.cuisine_type)

    def open_restuarant(self):
        print("restuarant is open")


    def add_count(self,count):
        self.count += count

class Fruit():

    def __init__(self,type):
        self.type = type


    def change_type(self,new_type):
        self.type = new_type


class IceCreamStand(Restaurant):
    def __init__(self, name,cuisine,flavors,fruit):
        super().__init__(name,cuisine)
        self.flavors = flavors
        self.fruit = fruit

    def show_flavor(self):
        print("flavor is "+self.flavors)
        print("flavor fruit is "+self.fruit.type)

