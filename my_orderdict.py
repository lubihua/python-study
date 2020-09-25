from collections import OrderedDict

my_orderdict = OrderedDict()
my_orderdict['becky'] = 34
my_orderdict['nannna'] = 5
my_orderdict['yangyang'] = 2

for key in my_orderdict.keys():
    print(key+' is '+str(my_orderdict[key])+' years old.')


print('--------done')
