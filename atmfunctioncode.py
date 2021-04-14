#register
# - first name, last name, password, email
# - generate user account
#TO-DO LIMIT PASSWORD TO 4 DIGIT, FIX LOGIN() FOR OLD USER


#login
# - account number & password


#bank operations

#Initializing the system
import random
userBalance = 0
database = {} #dictionary

def init():

   
    print("Welcome to bankPHP")
 
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        
        login()
    elif(haveAccount == 2):
        
        register()
    else:
        print("You have selected invalid option")
        init()


def generateAccountNumber():

    return random.randrange(1111111111,9999999999)


def login():
    
    print("********* Login ***********")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
               
                
    
    


def register():

    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()

def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if(selectedOption == 1):
        
        depositOperation()
    elif(selectedOption == 2):
        
        withdrawalOperation()
    elif(selectedOption == 3):
        
        logout()
    elif(selectedOption == 4):
        
        exit()
    else:
      
        print("Invalid option selected")
        bankOperation(user)


def withdrawalOperation():
    print("====Withdrawal====")
    global userBalance
    userDebit = int(input("How much would you like to withdraw? \n"))
    if (userBalance < userDebit):
        print(f'Insufficient funds, current balance is: {userBalance}')
        bankOperation(user) #WHY CANT I CALL THIS FUNCTION HERE ? OR HOW ELSE CAN I LOOP?
        
    else:
        userBalance = userBalance - userDebit
        print(f'Take your cash!, your new balance is {userBalance}')
    logout()


def depositOperation():
    global userBalance
    print("====Deposit Operation====")
    userDeposit = int(input('How much would you like to deposit? \n'))
    userBalance = userBalance + userDeposit
    print(f'Money deposited. Your current balance is {userBalance}')
    logout()




def logout():
    action = int(input('Would you like to perform another action? \n 1. Yes 2. No \n'))
    if action == 1: 
        login()
    elif action == 2:
        exit()
    else:
        print('Please select a valid option')
        logout()

def exit():
    print('Please collect your card')

#### ACTUAL BANKING SYSTEM #####

init()


