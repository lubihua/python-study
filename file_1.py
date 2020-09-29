with open("text_folder/a.txt") as file_object:
    print(file_object.read().rstrip())


print('----------------11')
with open("text_folder/a.txt") as file_object2:
    for line in file_object2.readlines():
        print(line.rstrip())


print('---------------12')
with open("text_folder/a.txt") as file_object3:
    for line in file_object3:
        print(line.strip())

print('--------------13')
my_lines=''
with open("text_folder/a.txt") as file_object4:
    my_lines = file_object4.readlines()

print('line size is '+str(len(my_lines)))
for line in my_lines:
    print('aaa - '+line.rstrip())