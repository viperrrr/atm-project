#ATM MOCK-UP PROJECT
name = input('What is your name? \n')
allowedUsers = ['Seyi','Mike','Love']
allowedPassword = ['passwordSeyi','passwordMike','passwordLove']
initialBalance = ['1.0','2.0','3.0']

if(name in allowedUsers):
    password = input('Your password \n')
    userId = allowedUsers.index(name)
    balance = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        from datetime import datetime

        now = datetime.now()
        
        dtString = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time = ", dtString)

        print('Welcome %s' % name)
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option:'))

        if(selectedOption == 1):
            print('you selected %s' % selectedOption)
            withdrawalAmount = int(input('How much would you like to withdraw: \n'))
            print('Take your cash')

        elif(selectedOption == 2):
            print('you selected %s' % selectedOption)
            depositAmount = int(input('How much would you like to deposit: \n'))
            currentBalance = float(initialBalance[balance]) + depositAmount
            print('Current Balance is ', currentBalance)

        elif(selectedOption == 3):
            print('you selected %s' % selectedOption)
            complaint = input('What issue will you like to report: \n')
            print('Thank you for contacting us')

        else:
            print('Invalid option selected, please try again')


    else:
        print('Password incorrect, please try again')

else:
    print('Name not found, please try again')
