import random
import datetime
import string
import sys
def validate_dob_format(dob):
    try: 
        datetime.datetime.strptime(dob, '%d/%m/%Y')
        return  True
    except ValueError:
        return False

#password generator
def generate_chars(char_set, num_chars):
        return [random.choice(char_set) for _ in range(num_chars)]
def generate_password(num_upper, num_lower, num_digits, num_special):
    upper_chars = generate_chars(string.ascii_uppercase, num_upper)
    lower_chars = generate_chars(string.ascii_lowercase, num_lower)
    digit_chars = generate_chars(string.digits, num_digits)
    special_chars = generate_chars(string.punctuation, num_special)
    password = upper_chars + lower_chars + digit_chars + special_chars
    random.shuffle(password)
    return ''.join(password)

def main():
    #user input
    firstname=input("Enter your first name: ")
    lastname=input("Enter your last name: ")
    age=int(input("Enter your age: "))
    birthday=input("Enter your birthday in dd/mm/yyyy format: ")
    if validate_dob_format(birthday):
        print("Date of birth  is in correct format.")
    else:
        print("Date of birth is in invalid format.")

    #username
    print (f"\nHello {firstname} {lastname}, welcome to the Motion Detector! Let's Start.")
    Username= firstname[:2] + lastname[:3] + birthday[-4:] + birthday[3:5] + birthday[:2]
    print(f"your username is: {Username}")

    #password generator
    print("\nYour password generator.")
    num_upper = int(input("Enter number of uppercase you want: "))
    num_lower = int(input("Enter number of lowercase you want: "))
    num_digits = int(input("Enter number of digits you want: "))
    num_special= int(input("Enter number of special characters: "))
    password= generate_password(num_upper, num_lower , num_digits , num_special)
    print("Your password is:",password)
    
    #User rights
    if firstname.upper() == "BIJAY" and lastname.upper() == "SATYAL":
        print(f"\nWelcome {firstname}, you have admin rights.")
    elif firstname.upper() == "MIRA" and lastname.upper() == "VORNE":
        print(f"\nWelcome {firstname}, you have super-user rights.")
    elif age >= 18:
        print(f"\nWelcome {firstname}, you have viewer rights.")
    else:
        print(f"\nGreetings {firstname}, you are too young to operate this program.")
        sys.exit()
        
    #temperature check
    temp=input("\nDo you want to see temperature in fahrenheit or celsius? ")
    temperature_in_Fahrenheit = random.randint(32, 212)
    temperatue_in_celsius= random.randint(0, 100)
    if temp.upper() == "CELSIUS" and temperatue_in_celsius > 80:
        print(f"The temperature of the CPU is {temperatue_in_celsius} °C, it is ON FIRE")
    elif temp.upper() == "CELSIUS" and 70 <= temperatue_in_celsius <= 80 :
        print(f"The temperature of the CPU is {temperatue_in_celsius} °C, it is TOO HOT")
    elif temp.upper() == "CELSIUS" and temperatue_in_celsius < 70:
        print(f"The temperature of the CPU is {temperatue_in_celsius}°C, it is OK")
    elif temp.upper() == "FAHRENHEIT" and temperature_in_Fahrenheit > 176:
        print(f"The temperature of the CPU is {temperature_in_Fahrenheit} °F, it is ON  FIRE")
    elif temp.upper() == "FAHRENHEIT" and 158 <= temperature_in_Fahrenheit <= 176:
        print(f"The temperature of the CPU is {temperature_in_Fahrenheit} °F, it is TOO HOT")
    else:
        print(f"The temperature of the CPU is {temperature_in_Fahrenheit} °F, it is OK")

    #movement
    movement=["Yes","No"]
    movement_detection= random.choice(movement)
    if movement_detection == "YES":
        print("\nMovement detected: 'Yes'")
    else:
        print("\nMovement detected: 'No'")

    #celsius to fahrenheit
    celsius=float(input("\nEnter temperature in celsius: "))
    fahrenheit= (celsius * 9/5) + 32
    print(f"The given temperature {celsius} °C is {fahrenheit} °F")
    
    #exiting
    quit=input("\nDo you want to quit (Yes / NO)? ")
    if quit.upper()== "YES":
        print("Thanks for visiting. Welcome back soon.")
        sys.exit()
main()
