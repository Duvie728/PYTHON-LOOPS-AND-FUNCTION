#register
# -first_name, last_name ,email, password
# - generate user_account



#login
# - account_number &  password

#bank operations

#initializing the system
import random




database = {
    3946159806: ['Elizabeth', 'Eli', 'elizabetheli4u@gmail.com', 'password', 1000]
}

def init():
  
    print("Welcome to BANK ZURI")

    have_account = int(input("Do you have an account with us:1 (yes), 2(no) \n"))

    if(have_account == 1):
        login()
    elif(have_account == 2):
         print(register()) 
    else:
        print("You have selected an invalid option")
        init()


def login():

    print("********* Login **********")

    account_number_from_user = int(input("What is your account number?\n"))
    password =input("What is your password\n")

    for account_number, user_details in database.items():
        if(account_number == account_number_from_user):
            if(user_details[3] == password):
                bank_operation(user_details)
                   
            else:
                print('Invalid account or password')
                login()

      
    
def register():

    print("******** Register ********")

    email = input("What is your email address?\n")
    first_name = input("What is your first_name?\n")
    last_name = input("What is your last-name?\n")
    password = input("create a password for yourself\n")

    account_number = generate_account_number()

    database[account_number] = [ first_name, last_name, email, password, 0]

    print("Your Account has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is :%d" % account_number)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()
    

def bank_operation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )


    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) transfer (4) complaint (5)get_ current_balance (6)logout (7) Exit\n"))

    if(selected_option == 1):
        deposit_operation()
    elif(selected_option == 2):
        withdrawal_operation()
    elif(selected_option == 3):
        transfer_operation()
    elif(selected_option == 4):
        complaint_operation()
    elif(selected_option == 5):
        get_current_balance(1000)
    elif(selected_option == 6):
        logout()
    elif(selected_option == 7):
        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation():
    print("***Withdrawal***")

   # print(get_current_balance(1000)

    withdrawal_amount = int(input('How Much do you want to withdraw?\n'))
    if get_current_balance(1000) > withdrawal_amount:
         print('current balance:',get_current_balance(1000) - withdrawal_amount)
         print("Take your cash")
         if get_current_balance(1000) < withdrawal_amount:
             print("\nYour balance is less than withdrawal amount")
             print("\nUpdated Balance: " + str(get_current_balance(1000)) + " n")
    

    selection = input("do you want to perform another operation?  yes or no\n")
    if selection == "yes":
        login()
    if selection == "no":
         logout()


def deposit_operation():
    print("***Deposit operation***")

    #print(get_current_balance(1000))
    deposit_amount = int(input('How Much would you like to deposit?\n')) 
    print('current_balance:',deposit_amount + get_current_balance(1000))


    
    selection = input("do you want to perform another operation?  yes or no\n")
    if selection == "yes":
        login()
    if selection == "no":
         logout()


def transfer_operation():
    print("***Transfer operation***")
    transfer_amount = int(input('How Much would you like to transfer?\n')) 
    print('current_balance:',transfer_amount + get_current_balance(1000)) 
    print("Transaction is now complete.")
    print("Transaction code: ", random.randint(1000, 99999))
    print("Thanks for choosing us as your bank")
    exit()
    

def get_current_balance(user_details):
    print(get_current_balance(1000))
    return user_details

           

def complaint_operation():
    print("^^^^Complaint ^^^^")
    complain = input('What issue will you like to report?\n')
    print("Your issue is currently been resolved")
    print("Transaction code: ", random.randint(1000, 99999))
    print("***Thank you for contacting us***")
    logout()

           

def generate_account_number():

    return random.randrange(1111111111,9999999999)

def generate_transaction_code():

    return random.randrange(1000,9999)





def logout():
    login()



init()


def exit():
    print("Thank you for choosing us as your bank")
   
    