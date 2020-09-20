print('---------------7-4')
food = ''
while food != 'quit':
    food = input('Please choose your food')
    if food == 'quit':
        break
    print('You chose '+food)


print('-------------------7-8')
unconfirmed_users = ['becky','Nannna','Yangyang']
confirmed_user = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifing user '+current_user)
    confirmed_user.append(current_user)

print('The following users are confirmed')
for user in confirmed_user:
    print(user)
print('current unconfirmed user size is '+str(len(unconfirmed_users)))


print("------------------------7-9")
pets= ['dog','cat','zebra','goldfist','cat','dog']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)