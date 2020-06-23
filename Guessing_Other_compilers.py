
import datetime
import pytz
import random
import time

time_utc = datetime.datetime.now(tz=pytz.UTC)
now_1 =time_utc.astimezone(pytz.timezone('Africa/Johannesburg'))

def greeting():
    now = now_1.strftime("%H")
    if int(now) < 12:
        return "Good Morning Babe."
    elif int(now) < 19:
        return "Good day babe."
    else:
        return "Good night babe."


print(greeting() + " Welcome to a random guessing game. \nYou have to guess the name that I want you to call me today. \nYou can choose from either Babe, Stix or Tapiwa. \nThe names continuosly change randomly. \nPlay until you get it correct. Enjoy my stupid code kkk !! \n")


def secrete_words():
    secrete_word = ["Stix", "Tapiwa", "Babe"]
    random.shuffle(secrete_word)
    return secrete_word[0]  # The function returns a randomly shuffled secrete word at index 0


time_of_execution = now_1.strftime("%H:%M")

guess = ""  # Creates a viable with an empty string

start_time = time.time()
def condition():
    guess = input("Enter guess of my name: ")
    count = 1
    while guess != secrete_words():
        guess = input("That's not correct. Enter guess again: ")
        count += 1
    return str(count)



print("\nCongrats you got the name. It took you " + str(condition()) + " trial(s) to find the name. You executed this code at " + str(time_of_execution))

time_level = time.time()-start_time
if time_level<=25:
    print("\nYou're very good at guessing!!!!!")
elif time_level <=45:
     print("\nYou're average at guessing!!!!")
else:
    print("\nYou're poor at guessing!!!!")

print("\nOnce again " + greeting() + "\nThanks for running my stupid code kkk \nI love you so much. ")
#for tz in pytz.all_timezones:
    #print(tz)
