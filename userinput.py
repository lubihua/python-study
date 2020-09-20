print('-------------------7-1')

car = input('Please input the can type')
print('Let me see if i can find '+car)

print('------------------7-2')
people_count = input('Please input how many people')
people_count = int(people_count)
if people_count < 8 :
    print('can eat now')
else:
    print('Please wait')


print('----------------7-3')
random_number = input('Please input a number')
random_number = int(random_number)
if random_number %10 ==0:
    print('能够整除10')
else:
    print('不能够整除10')