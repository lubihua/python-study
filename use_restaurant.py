import restaurant

first_restuarant = restaurant.Restaurant('McDonald', 'abc')
first_restuarant.describe()
first_restuarant.open_restuarant()
print("first count is "+str(first_restuarant.count))

second_restuarant = restaurant.Restaurant('KFC','Hello')
print(second_restuarant.name);
print("second count is "+str(second_restuarant.count))
second_restuarant.add_count(10)
print("second count is "+str(second_restuarant.count))

print("-------------------")

lemon = restaurant.Fruit('lemon')
ice_cream_restua = restaurant.IceCreamStand('HaGenHash','Big','Ice Cream',lemon)
ice_cream_restua.describe()
ice_cream_restua.show_flavor()
ice_cream_restua.fruit.change_type('watermelon')
ice_cream_restua.show_flavor()

