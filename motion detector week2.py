import random
import datetime
def validate_dob_format(dob):
    try: 
        datetime.datetime.strptime(dob, '%d/%m/%Y')
        return  True
    except ValueError:
        return False
#user input
firstname=input("Enter your first name: ")
lastname=input("Enter your last name: ")
age=int(input("Enter your age: "))
temp=input("Do you want to see temperature in fahrenheit or celsius? ")
birthday=input("Enter your birthday in dd/mm/yyyy format:")
if validate_dob_format(birthday):
    print("Date of birth  is in correct format.")
else:
    print("Date of birth is in invalid format.")
#username
print (f"hello {firstname} {lastname} welcome to the Motion Detector! Let's Start.")
Username= firstname[:2] + lastname[:3] + birthday[-4:] + birthday[3:5] + birthday[:2]
print(f"your username is: {Username}")

#rights
if firstname.upper() == "BIJAY" and lastname.upper() == "SATYAL":
    print(f"Welcome {firstname}, you have admin rights.")
elif firstname.upper() == "MIRA" and lastname.upper() == "VORNE":
    print(f"Welcome {firstname}, you have super-user rights.")
elif age >= 18:
    print(f"Welcome {firstname}, you have viewer rights.")
else:
    print(f"Greetings {firstname}, you are too young to operate this program.")
#temperature check
temperature_in_Fahrenheit = random.randint(32, 212)
temperatue_in_celsius= random.randint(0, 100)

if temp.upper() == "CELSIUS" and temperatue_in_celsius > 80:
    print(f"The temperature of the CPU is {temperatue_in_celsius}, it is ON FIRE")
elif temp.upper() == "CELSIUS" and 70 <= temperatue_in_celsius <= 80 :
    print(f"The temperature of the CPU is {temperatue_in_celsius}, it is TOO HOT")
elif temp.upper() == "CELSIUS" and temperatue_in_celsius < 70:
    print(f"The temperature of the CPU is {temperatue_in_celsius}, it is OK")
elif temp.upper() == "FAHRENHEIT" and temperature_in_Fahrenheit > 176:
    print(f"The temperature of the CPU is {temperature_in_Fahrenheit}, it is ON  FIRE")
elif temp.upper() == "FAHRENHEIT" and 158 <= temperature_in_Fahrenheit <= 176:
     print(f"The temperature of the CPU is {temperature_in_Fahrenheit}, it is TOO HOT")
else:
     print(f"The temperature of the CPU is {temperature_in_Fahrenheit},it is OK")

#movement
movement=["Yes","No"]
movement_detection= random.choice(movement)
if movement_detection == "YES":
    print("Movement detected: 'Yes'")
else:
    print("Movement detected: 'No'")
#celsius to fahrenheit
celsius=input("Enter temperature in celsius: ")
celsius=float(celsius)
fahrenheit= (celsius * 9/5) + 32
print(f"The given temperature {celsius} C  is {fahrenheit} F")
#exiting
quit=input("Do you want to quit (Yes / NO)? ")
if quit.upper()== "YES":
    print("Thanks for visiting. Welcome back soon.")





    
