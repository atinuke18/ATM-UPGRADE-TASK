import random



def init():
   
    valid_option = False
    print('Hello! Welcome to Page Financials')
   
    while valid_option == False:
        have_account = int(input("Do you have an account with us? 1. Yes  2. No \n "))


        if have_account == 1:
            valid_option = True
            login ()

        elif have_account ==2:
            valid_option= True
            print (register())
            

        else:
            print('Please select a valid option')


def login():
    print('----Login to your account----')
    user_account_number = int(input("What is your account number? \n"))
    Password= input('Enter your password.  \n')
    for account_number, user_details in database.items():
             if account_number == user_account_number:
                 if user_details[3]== Password:
                     bank_operation(user_details)
    print('Invalid account number or password')


def register():
    print('----Please Register----')
    email = input("register your email address \n")
    first_name = input('Type your first name  \n')
    last_name = input('Type your last name  \n')
    Password = int(input('Create a password for yourself  \n'))

    account_number= generate_account_number()

    database[account_number]= [email, first_name, last_name, Password]
    print("Your account has been created")
    print(f'Your account number is {account_number}')
    login()

def bank_operation(User):
    print('Welcome %s ' % (User[1], User[2]))
   
    Select_option = input("What would you like to do? (1) Deposit  (2) Withdraw  (3) Logout  (4)Exit")

    if Select_option == 1:
        deposit_operation()

    elif Select_option == 2:
        withdrawal_operation()

    elif Select_option == 3:
        logout()

    elif Select_option ==4:
        exit()

    else:
        print('Please select a valid option.')
        bank_operation(User)


def withdrawal_operation():
    withdraw = int(input('Enter (1) for withdrawal or (2) to logout \n'))
    if withdraw == 1:
        Cashout = int(input("How much would you like to withdraw? \n"))
        print("Transaction in progress . . . \n")
        print('Transaction completed \n')
        print(f"Take your cash N{Cashout}")
        import datetime

        leave_atm= False
        while leave_atm == False:
            choose = int(input("Enter (1) Logout of (2) Exit \n"))
            if choose ==1:
                leave_atm = True
                logout()

            elif choose==2:
                leave_atm= True
                exit()

            else:
                print ("Invalid option entered, try again")


def deposit_operation():
    deposit =int(input("Enter (1) to make deposit, or (2) to logout \n"))        
    if deposit ==1:
        Cashin = int(input("How much do you want to deposit? \n"))
        print("Transaction completed \n")
        print(f"Your current balance is : N{Cashin}")
        import datetime

        leave_atm= False
        while leave_atm == False:
            choose = int(input("Enter (1) Logout of (2) Exit \n"))
            if choose ==1:
                leave_atm = True
                logout()

            elif choose==2:
                leave_atm= True
                exit()

            else:
                print ("Invalid option entered, try again")

    elif deposit ==2:
        logout()

    else:
        print('Invalid input entered')



def generate_account_number():
   
    return random.randrange(1111111111, 9999999999)

def logout():
    login()

database= {'email': 'tinuodus@gmail.com'  , 'first_name': 'Atinuke' , 'last_name' : 'Odusanya', 'Password': 'Tinky', 'account_number': 5864258254}
init()

