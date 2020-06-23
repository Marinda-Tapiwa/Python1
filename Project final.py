variable1 = input("Enter the independent variable: ")
variable2 = input("Enter dependent variable :")

variables = []
variables.append(variable1)
variables.append(variable2)





'''
pressure = "Pressure"
temperature = "Temperature"
while input_pressure != pressure or input_temperature != temperature:
    print("Error! Please Enter Valid Dependent and Independent Variable Names")
    input_pressure = input("\nEnter the independent variable: ")
    input_temperature = input("Enter dependent variable :")
    '''


print("\nSuccess!!")

def trials():
    while True:
        try:
            input_pressure_point = float(input("\nEnter the independent variable point: "))
            input_temperature_point = float(input("Enter dependent variable point:"))
        except ValueError:
            print("Error! The entered data are not numbers! Please re-enter the last point")
            continue
        else:
            values = []
            values.append(float(input_pressure_point))
            values.append(float(input_temperature_point))

        return values


# reads and writes to an external file
add_to_array = open("Tapiwa_project_final", 'r+')
add_to_array.write(str(trials()))
add_to_array.write("\n")

# asks the user to repeat
restart = input(str("\nDo you want to enter data again?:"))
response = ("yes", "no")  # set of valid responses
while restart.lower() not in response:  # checks if the response is valid
    restart = input("Invalid response!! \nDo you want to enter data again?:")

# restarts prompt or breaks based on user response
while restart.lower() == "yes":
    add_to_array.write(str(trials()))
    add_to_array.write("\n")
    restart = input("\nDo you want to enter data again?:")
    while restart.lower() not in response:
        restart = input("Invalid response!! \nDo you want to enter data again?:")
else:
    print("\nThanks and goodbye!")
add_to_array.close()  # closes the external file after writing to it.
print('Your values are: ')
print(variables)

add_to_array = open("Tapiwa_project_final", "r")  # reopens external file for reading it
print(add_to_array.read())
add_to_array.close()
