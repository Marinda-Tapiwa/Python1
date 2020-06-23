name = input("Hie, whats your name:  ")
print("I would like to get feedback from you \nAnswer with Yes/No")
response= ["Yes", "yes", "YES"]

male= input("\nMale: ")
black = input("Black: ")
smart = input("Smart: ")

if male in response and black in response and smart in response:
    print (name + " this describes Stix")
else:
    if male in response  and black not in response:
        print(name + " you're a white man")
    else:
        if male not in response and black not in response:
            print(name + " you're a white woman")
        else:
            if male in response and black in response:
                print(name + " you're a black man")
            else:
                if male not in response and black in response:
                    print(name + " you're a black woman")