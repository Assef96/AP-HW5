import os
import re

def create_dir(name, address):
    dir = os.path.join(address, name)
    if not os.path.exists(dir):
        os.makedirs(dir)

def create_file(name, address):
    dir = os.path.join(address, name)
    if not os.path.exists(dir):
        os.mknod(dir)

def delete(name, address):
    dir = os.path.join(address, name)
    if os.path.exists(dir):
        os.remove(dir)

def find(name, address):
    dir_list = []
    for (dirpath, _, filenames) in os.walk(address):
        if name in filenames:
            dir_list.append(os.path.join(dirpath, name))
    return dir_list

# create_dir('hello', '/home/assef/Desktop/codes/Q5')
# create_dir('hello', '/home/assef/Desktop/codes/Q5/folder')
# create_file('hello.cpp', '/home/assef/Desktop/codes/Q5')
# create_file('hello.cpp', '/home/assef/Desktop/codes/Q5/folder')
# create_file('hello.h', '/home/assef/Desktop/codes/Q5/folder')
# delete('hello.cpp', '/home/assef/Desktop/codes/Q5')
# print(find('main.py', '/home/assef/Desktop/codes/Q5'))
# find(hello.cpp, /home/assef/Desktop/codes/Q5)

while True:
    doc = '''
Enter one of the following commands:
(Use . for refering to current working directory)
--->  create_dir(name, address)
--->  create_file(name, address)
--->  delete(name, address)
--->  find(name, address)
--->  exit()
'''
    print(doc)
    command = input('--->  ')
    if command == 'exit()':
        break
    else:
        x = re.search("(create_dir|create_file|delete|find)[(](.*), *(.*)[)]", command)
        if(x):
            function = x.group(1)
            name = x.group(2)
            address = x.group(3)
            if function == 'create_dir':
                create_dir(name, address)
            elif function == 'create_file':
                create_file(name, address)
            elif function == 'delete':
                delete(name, address)
            elif function == 'find':
                print(find(name, address))
        else:
            print("Error: No command was matched!")

