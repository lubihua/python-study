import json
numbers = [1,2,3,4,5,6]

with open('text_folder/json_demo.txt','w') as json_object:
    json.dump(numbers,json_object)
print('json.dump is done----------')

with open('text_folder/json_demo.txt') as json_read_obj:
    num = json.load(json_read_obj)
    print(num)
    print('size is '+str(len(num)))
print('json.load is done----------')


my_dict = {'name':'Becky','age':18}
with open('text_folder/json_demo_2.txt','w') as file_obj_1:
    json.dump(my_dict,file_obj_1)

print('my dict is saved')

with open('text_folder/json_demo_2.txt') as file_obj_2:
    get_my_dict = json.load(file_obj_2)
    print(get_my_dict['name'])