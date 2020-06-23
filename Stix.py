import random
import time
now = time.strftime("%H")
name = input("Hello! What's your name?:")

def greeting():
    if int(now)<12:
        print("Good morning "+ name +"\nWelcome to a three number lotto!")
    else:
        print("Greetings " + name + "\nWelcome to a three number lotto!")

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
        print("The winning numbers are " + str(lotto_numbers) + ". You got all the numbers! \nCongratulations " + name + " you hit the jackpot! You won R15,000! ")

    elif num1 in lotto_numbers and num2 in lotto_numbers:
        print("The winning numbers are " + str(lotto_numbers) + ". You got two of the numbers! \nCongratulations " + name + " you won R1,500! ")
    elif num1 in lotto_numbers and num3 in lotto_numbers:
        print("The winning numbers are " + str(lotto_numbers) + ". You got two of the numbers! \nCongratulations " + name +  " you won R1,500! ")
    elif num2 in lotto_numbers and num3 in (lotto_numbers):
        print("The winning numbers are " + str(lotto_numbers) + ". You got two of the numbers! \nCongratulations " + name + " you won R1,500! ")
    elif num1 in lotto_numbers or num2 in lotto_numbers or num3 in lotto_numbers:
        print("The winning numbers are " + str(lotto_numbers) + ". You got one of the numbers! \nCongratulations " + name + " you won R200! ")
    else:
        print("The winning numbers are " + str(lotto_numbers) + ". You didn't get any of the numbers! \nSorry " + name + " you lost ")

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
        print("The winning numbers are " + str(lotto_numbers) + ". You got all the numbers! \nCongratulations " + name + " you hit the jackpot! You won R15,000! ")

    elif num1 in lotto_numbers and num2 in lotto_numbers:
        print("The winning numbers are " + str(lotto_numbers) + ". You got two of the numbers! \nCongratulations " + name + " you won R1,500! ")
    elif num1 in lotto_numbers and num3 in lotto_numbers:
        print("The winning numbers are " + str(lotto_numbers) + ". You got two of the numbers! \nCongratulations " + name +  " you won R1,500! ")
    elif num2 in lotto_numbers and num3 in (lotto_numbers):
        print("The winning numbers are " + str(lotto_numbers) + ". You got two of the numbers! \nCongratulations " + name + " you won R1,500! ")
    elif num1 in lotto_numbers or num2 in lotto_numbers or num3 in lotto_numbers:
        print("The winning numbers are " + str(lotto_numbers) + ". You got one of the numbers! \nCongratulations " + name + " you won R200! ")
    else:
        print("The winning numbers are " + str(lotto_numbers) + ". You didn't get any of the numbers! \nSorry " + name + " you lost ")

    return

def lotto_decision():
    pick_type = input("\nDo you want to play Auto Pick(Q) or Manual Pick (M):")
    decision = pick_type.upper()
    while decision != "Q" or decision != "M":

        if decision == "Q":
            random_pick()
            break
        elif decision == "M":
            manual_pick()
            break
        print("Please enter a valid response!")
        pick_type = input("Do you want to play Auto Pick(Q) or Manual Pick (M):")
        decision = pick_type.upper()

def restart():

    repeat = input("\nDo you want to play lotto again?: ")
    repeat_decison = repeat.upper()
    decision_set = ("YES", "NO")
    if repeat_decison == "YES":
        lotto_decision()
    elif repeat_decison == "NO":
        print("Thanks " + name + " for playing the lotto! Good bye!")

    else:
        while repeat_decison not in decision_set:
            print("Please enter valid response!")
            repeat = input("Do you want to play lotto again?: ")
            repeat_decison = repeat.upper()
        else:
            if repeat_decison == "YES":
                lotto_decision()
            elif repeat_decison == "NO":
                print("Thanks " + name + " for playing the lotto! Good bye!")
    return
greeting()
lotto_decision()
restart()

print("\nDone by : StixTheMiner")