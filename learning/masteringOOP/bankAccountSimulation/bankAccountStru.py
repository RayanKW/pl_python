""" In this example we'll simulate a bank operations. 
    """
accountName = "Rayan"
accountBalance = 200
accountPassword = 'SweetSugar'

while True:
    print()
    print('Press B to show balance')
    print('press  D to deposit')
    print('press W to withdraw')
    print('press S to show the account')
    print('press q to quit')
    print()
    
    action = input(' What Do You Want To Do? ')
    action = action.lower()#force lowercase
    action = action[0] #Just use the first letter
    print()
    
    if action == 'b':
        print('GET BALANCE')
        userPassword = input('please enter the password: ')
        if userPassword !=  accountPassword:
            print("WRONG PASSWORD")
        else:
            print("YOUR BALANCE IS ", accountBalance)
    elif action == 'd':
        print('DEPOSIT MONEY')
        userDepositAmount = int(input('PLEASE ENTER AMOUNT TO DEPOSIT: '))
        userPassword  = input('please enter your password: ')
        
        if userDepositAmount < 0:
            print("You cannot deposit a negative amount")
        elif userPassword != accountPassword:
            print("Incorrect Password")
        else:
            accountBalance = accountBalance + userDepositAmount
            print('Your New Balance is: ', accountBalance)
    elif action == 's':
        print('show :')
        print('  Name', accountName)
        print('  Balance', accountBalance)
        print('  Password', accountPassword)
        print()
    elif action == 'q':
        break
    elif action == 'w':
        print("Withdraw")
        userWithdrawAmount = int(input('Please Enter Amount You Wish To Withdraw: '))
        userPassword = input('Please Input Your Password: ')
        if userWithdrawAmount < 0:
            print('Too Low Withdraw: ')
        elif userPassword != accountPassword:
            print('WRONG PASSWORD!!')
        elif userWithdrawAmount > accountBalance:
            print('INSUFFICIENT FUNDS!!!')
        else:
            accountBalance-= userWithdrawAmount
            print('YOUR NEW BALANCE IS: ', accountBalance)
print('DONE')