#
contact = {}
#initializing an empty dictionary
running = True
while running:
    command = input('A)dd D)elete L)ook up Q)uit: ')
    if command == 'A' or command == 'a':
        name=input('enter name: ')
        print('Enter phone number for', name, end=':')
        #{'name': 12, name2:12}
        number = input()
        contact[name] = number
        #above is just the name and the key i.e  to access an item in a dic we use dic_name[key] 
        # to access the value
    elif command == 'D' or command == 'd':
        name = input('enter name : ')
        del contact[name]
    elif command == 'L' or command == 'l':
        name = input('Enter name :')
        print(name, contact[name])
    elif command == 'Q' or command == 'q':
        running = False
    elif command=='dump':
        print(contact)
    else:
        print(command, 'is not a valid command')
        #THE QUESTIONS THOUGH REMAINS HOW DO I VALIDATE THE KEY IN OUR CASE 
        # THE NAME TO MAKE SURE THE KEY IS UNIQUE REM THE KEY SHOULD BE UNIQUE IN A DICTIONARY.
for d, v in contact.items():
    print(d, v)
    # break that break makes sure the program breaks after looping once
# dic = {'jonh':12, 'ko':12}
# print(dic)