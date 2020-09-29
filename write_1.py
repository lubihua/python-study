with open("text_folder/write_demo.txt",'a') as file_object:
    file_object.write('I am Nannan \n')
    user_input = input("please input your language")
    file_object.write(user_input+'\n')
