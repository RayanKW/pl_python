# my computer doesn't work!! help me.
print("Please Help my computer isn't working")
#diagnosis QA
choice = input('does it show lights, yes(y) or no(n)')
if choice == 'N' or choice == 'n':
    choice2= input('is it pluged in y or n')
    if choice2 == 'n' or choice2 == 'N':
        print('plug it in')
    else:
        choice3 = input('does it have a fuse')
        if choice3 == 'n' or choice3 == 'N':
            print('go buy one')
        else:
            print('take it to a workshop')
elif choice == 'N' or choice == 'y':
    print('i dont know')
else:
    print('invalid command')
#nested loops.