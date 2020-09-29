try:
    a = int(input("please input a number"))
    b = int(input("please input another number"))
except ValueError:
    print('incorrect format data')
else:
    c = int(a)+int(b)
    print('sum value is '+str(c))

print('111111111')