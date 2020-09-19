car = 'bmw'
print(car == 'bmw')
print(car.upper() == 'BMW')

print("=============")

request_topping = 'mushrooms'
if request_topping != 'anchovies':
    print("Hold the anchovies")

print("----------------")

request_toppings = ['mushrooms', 'onions', 'pineapple']
pineapple = "pineapple"
print('onions' in request_toppings)
print("pineapple" not in request_toppings)
print(pineapple in request_toppings)

print("---------------- 5-3")
alien = 'yellow'
if alien == 'green':
    print("Got 5 points")
elif alien == 'yellow':
    print("Got 10 points")
elif alien == 'red':
    print("Got 15 points")


print("---------------- 5-6")
age = -1
if age < 0:
    print("age could not less than zero")
elif age < 2:
    print("It's a baby")
elif age < 4:
    print("study walking")
elif age < 13:
    print("go to school")
elif age < 20:
    print("young man")
elif age < 65:
    print("audit")
else:
    print("old man")


print("---------------- 5-7")
array=['abc','def']
if array:
    for str in array:
        print(str)
else:
    print("array is empty")