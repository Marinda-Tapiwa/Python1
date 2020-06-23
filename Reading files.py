from random import random
from random import randint
import glob
import time
now = time.strftime("%H")
def greeting():
    if int(now)<12:
        print("Good morning "+ Name +"\nWelcome to a three number lotto!")
    else:
        print("Greetings " + Name + "\nWelcome to a three number lotto!")

def random_pick():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lotto_machine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(lotto_machine)
    win1= lotto_machine[0]
    win2 = lotto_machine[2]
    win3 = lotto_machine[4]
    lotto_numbers = [int(win1), int(win2), int(win3)]
    random.shuffle(numbers)
    num1 = numbers[0]
    num2 = numbers[5]
    num3 = numbers[2]
    print("Your numbers are " + str([num1, num2, num3]))
    if num1 in lotto_numbers and num2 in lotto_numbers and num3 in lotto_numbers:
        print("The winning numbers are " + str(lotto_numbers) + ". You got all the numbers! \nCongratulations " + Name + " you hit the jackpot! You won R15,000! ")

    elif num1 in lotto_numbers and num2 in lotto_numbers:
        print("The winning numbers are " + str(lotto_numbers) + ". You got two of the numbers! \nCongratulations " + Name + " you won R1,500! ")
    elif num1 in lotto_numbers and num3 in lotto_numbers:
        print("The winning numbers are " + str(lotto_numbers) + ". You got two of the numbers! \nCongratulations " + Name +  " you won R1,500! ")
    elif num2 in lotto_numbers and num3 in (lotto_numbers):
        print("The winning numbers are " + str(lotto_numbers) + ". You got two of the numbers! \nCongratulations " + Name + " you won R1,500! ")
    elif num1 in lotto_numbers or num2 in lotto_numbers or num3 in lotto_numbers:
        print("The winning numbers are " + str(lotto_numbers) + ". You got one of the numbers! \nCongratulations " + Name + " you won R200! ")
    else:
        print("The winning numbers are " + str(lotto_numbers) + ". You didn't get any of the numbers! \nSorry " + Name + " you lost ")

    return

def manual_pick():
    lotto_machine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(lotto_machine)
    win1 = lotto_machine[0]
    win2 = lotto_machine[2]
    win3 = lotto_machine[4]
    lotto_numbers = [int(win1), int(win2), int(win3)]
    print("Enter a guess number between 1 and 10")
    num1 = int(input("Number 1:"))
    num2 = int(input("Number 2:"))
    num3 = int(input("Number 3:"))
    print("Your numbers are " + str([num1, num2, num3]))
    if num1 in lotto_numbers and num2 in lotto_numbers and num3 in lotto_numbers:
        print("The winning numbers are " + str(lotto_numbers) + ". You got all the numbers! \nCongratulations " + Name + " you hit the jackpot! You won R15,000! ")

    elif num1 in lotto_numbers and num2 in lotto_numbers:
        print("The winning numbers are " + str(lotto_numbers) + ". You got two of the numbers! \nCongratulations " + Name + " you won R1,500! ")
    elif num1 in lotto_numbers and num3 in lotto_numbers:
        print("The winning numbers are " + str(lotto_numbers) + ". You got two of the numbers! \nCongratulations " + Name +  " you won R1,500! ")
    elif num2 in lotto_numbers and num3 in (lotto_numbers):
        print("The winning numbers are " + str(lotto_numbers) + ". You got two of the numbers! \nCongratulations " + Name + " you won R1,500! ")
    elif num1 in lotto_numbers or num2 in lotto_numbers or num3 in lotto_numbers:
        print("The winning numbers are " + str(lotto_numbers) + ". You got one of the numbers! \nCongratulations " + Name + " you won R200! ")
    else:
        print("The winning numbers are " + str(lotto_numbers) + ". You didn't get any of the numbers! \nSorry " + Name + " you lost ")

    return

def lotto_decision():
    pick_type = input("\nDo you want to play Auto Pick(A) or Manual Pick (M):")
    decision = pick_type.upper()
    while decision != "A" or decision != "M":

        if decision == "A":
            random_pick()
            break
        elif decision == "M":
            manual_pick()
            break
        print("Please enter a valid response!")
        pick_type = input("Do you want to play Auto Pick(A) or Manual Pick (M):")
        decision = pick_type.upper()

def restart():

    repeat = input("\nDo you want to play lotto again?: ")
    repeat_decison = repeat.upper()
    decision_set = ("YES", "NO")
    while repeat.upper() in decision_set:
        if repeat.upper() == "YES":
            lotto_decision()
            repeat = input("\nDo you want to play lotto again?: ")
        if repeat.upper() == "NO":
            print("Thanks " + Name + " for playing the lotto! Good bye!")
            break
        else:
            print("Invalid response!")
            print("Thanks " + Name + " for playing the lotto! Good bye!")



    while repeat_decison not in decision_set:
        print("\nPlease enter valid response!")
        repeat = input("Do you want to play lotto again?: ")
        break
    while repeat.upper() in decision_set:
        if repeat.upper() == "YES":
            lotto_decision()
            repeat = input("\nDo you want to play lotto again?: ")
        if repeat.upper() == "NO":
            print("Thanks " + Name + " for playing the lotto! Good bye!")
            break
        else:
            print("Invalid response!")
            print("Thanks " + Name + " for playing the lotto! Good bye!")
    return

class User:
    def __init__(self, user_name, user_surname, user_email_address, user_password, user_id):
        self.name = user_name
        self.surname = user_surname
        self.email_address = user_email_address
        self.password = user_password
        self.user_id = user_id

def account_creation_prompts():
    name = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    email_address = input("Enter your email address: ")
    password = input("Enter password (minimum of 6 characters): ")
    ID = randint(2000000, 2999999)
    file = open("Python_Unused_Residual_Codes.py", 'a')
    file.write("ID = " + str(ID))

    while len(password) < 6:
        password = input("Password is too short!" "\nEnter password (minimum of 6 characters): ")

    User_details = User(name, surname, email_address, password, ID)
    add_user_database = open(str(name), "w")
    add_user_database.write(User_details.name)
    add_user_database.write("\n")
    add_user_database.write(User_details.surname)
    add_user_database.write("\n")
    add_user_database.write(User_details.email_address)
    add_user_database.write("\n")
    add_user_database.write(User_details.password)
    add_user_database.write("\n")
    add_user_database.write(str(User_details.user_id))
    add_user_database.close()
    print("Congrats "+ str(name) + " " + str(surname)+"! Your account has been successfully created. \nYour user ID is: "  + str(ID) +" Now you can try logging in")
def login_prompts():
    user_login_ID = input("Enter login ID (Your ID is your first name): ")
    global Name
    count1 = 0
    while True:
        count1 += 1
        try:
            add_user_database = open(str(user_login_ID), 'r')
        except FileNotFoundError:
            user_login_ID = input("User ID not found! Please enter login ID (Your ID is your first name): ")
            if count1 > 1:
                ac_prompt = input("No account exists for that ID! \nDo you want to create account? (Yes/No): ")
                prompts = ["yes", "no"]
                if ac_prompt.lower() == "yes":
                    account_creation_prompts()
                    exit()
                else:
                    exit()
        else:
            Name = user_login_ID
            break

    add_user_database = open(str(user_login_ID), 'r')
    login_ID = add_user_database.readlines()[0]
    add_user_database.close()

    add_user_database = open(str(user_login_ID), 'r')
    login_password = add_user_database.readlines()[3]
    add_user_database.close()

    user_login_password = input("Enter your password: ")
    count2 = 0
    while user_login_password not in login_password:
        user_login_password = input("Invalid password! Please enter your password: ")
        count2 += 1
        if count2 > 2:
            print("You tried too many attempts! Please try again later")
            break
    else:
        greeting()
        lotto_decision()
        restart()
        print("\nDone by : StixTheMiner")

def welcome_prompts():
    login = input("Hello and welcome. Do you want to create account or login? \nPlease reply with 'create' or 'login': ")
    attempts = ("create", "login")
    count2 = 0
    while login.lower() not in attempts:
        login = input ("Invalid response! \nPlease reply with 'create' or 'login': ")

        count2+=1
        if count2>3:
            print("You tried too many attempts! Please try again later")
            continue
    if login.lower() == 'create':
        account_creation_prompts()
    elif login.lower() == "login":
        login_prompts()

welcome_prompts()






