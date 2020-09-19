print('-------------6-1')

first_dict = {'first_name': 'Lu', 'last_name': 'Becky', 'age': 34 , 'city': 'guangzhou'}
print(first_dict['first_name'])
print(first_dict['last_name'])
print(first_dict['age'])
print(first_dict['city'])

print('----------6-2')
second_dict = {'becky': 34, 'Gary': 35, 'Nannan': 5}
print('Nannan age is '+str(second_dict['Nannan']))
second_dict['Yang'] = 2
print('Yang yang age is '+str(second_dict['Yang']))
second_dict['becky'] = 30
del second_dict['Gary']
print('Becky age is '+str(second_dict['becky']))

print('----------6-4-1')
for name, age in second_dict.items():
    print(name+" age is "+str(age))

print('----------6-4-2')
for name in second_dict.keys():
    print(name)

for name in second_dict:
    print(name)

print('----------6-4-3')
for name in sorted(second_dict.keys()):
    print(name)

for name, age in sorted(second_dict.items()):
    print(name+" age is "+str(age))

print('----------6-4-4')
for age in second_dict.values():
    print(age)

second_dict['Nannan'] = 2
print('Set Nannan age to 2 years old')
for age in set(second_dict.values()):
    print(age)

print('-----------6-8')
pet_1={'type': 'cat','name': 'LittleC','host': 'Nannan'}
pet_2={'type': 'dog','name': 'BigC','host':'becky'}
pets=[pet_1, pet_2]
for pet in pets[:]:
    print("It's a "+pet['type']+' called '+pet['name']+' host is '+pet['host'])


print('----------------6-9')
favorite_fruit = {'Nannan': ['apple', 'lemon', 'pear'], 'becky': ['watermelon', 'lemon', 'melon']}
print('size is '+str(len(favorite_fruit)))
for key,value in favorite_fruit.items():
    print(key+' likes fruit :')
    for fruit in value:
        print(fruit)
print('----------------6-9------------')