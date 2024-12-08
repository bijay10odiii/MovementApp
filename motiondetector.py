import time
from datetime import datetime
import random
import string
import requests
import json
import sys
#checking dob validity
def valid_dob(dob):
    try:
        datetime.strptime(dob, '%d/%m/%Y')
        return  True
    except ValueError:
        return False
    
#checking age is above 18 or not
def age_validation(dob):
    dob = datetime.strptime(dob, '%d/%m/%Y')
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age >= 18

#username generator
def username_generator(first_name, last_name, birthday):
    username = first_name[:2] + last_name[:3] + birthday[-4:] + birthday[3:5] + birthday[:2]
    print(f"Your Username is {username}")

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

#game section
def game():
    lowest_num = 1
    highest_num = 100
    answer = random.randint(lowest_num, highest_num)
    guesses = 0
    attempts = 5
    is_running = True

    print("Number Guessing Game.")
    while is_running:
        if guesses >= attempts:
            print()
            print("***************************************")
            print(f"Sorry!, you've used all your {attempts} attempts.")
            print(f"Correct answer was {answer}.")
            print("Better luck next  time!!")
            print("***************************************")
            break

        guess =input(f"Guess number between {lowest_num} and {highest_num}: ")
        if guess.isdigit():
            guess = int(guess)
            guesses += 1

            if guess < lowest_num or guess > highest_num:
                print("Invalid Input")
                print(f"Enter number between {lowest_num} and {highest_num}")
            elif guess < answer:
                print("Your guess is too LOW!!, Try Again")
            elif guess > answer:
                print("Your guess is too HIGH!!, Try Again")
            else:
                print("********************************************************************")
                print(f"Congratulations!! You guessed correctly! The answer was {answer}.")
                print(f"You made {guesses} guesses.")
                print("********************************************************************")
                is_running = False
            
        else:
            print("Invalid Input")
            print(f"Enter number between {lowest_num} and {highest_num}")

#User rights
def user_right(first_name, last_name):
    if first_name.upper() == "BIJAY" and last_name.upper() == "SATYAL":
        print(f"\nWelcome {first_name}, you have admin rights.")
        return "admin"
    elif first_name.upper() == "MIRA" and last_name.upper() == "VORNE":
        print(f"\nWelcome {first_name}, you have super-user rights.")
        return "super-User"
    else:
        print(f"\nWelcome {first_name}, you have viewer rights.")
        return "Viewer"
    #temperature check
def temperature_check(temp, temperature):
    if temp.upper() == "C":
        if temperature > 80:
            print(f"The temperature of CPU is {temperature}°C, It is on FIRE")
        elif 70 <= temperature <=80:
            print(f"The temperature of the CPU is {temperature}°C, It is too HOT")
        else:
            print(f"The temperature of the CPU is {temperature}°C, It is OK")
    elif temp.upper() == "F":
        if temperature > 176:
            print(f"The temperature of CPU is {temperature}°F, It is on FIRE")
        elif 158 <= temperature <= 176:
            print(f"The temperature of the CPU is {temperature}°F, It is too HOT")
        else:
            print(f"The temperature of the CPU is {temperature}°F, It is OK")

#store user information
def store_info(user_info, temperature, Movement):
    data={
        "user_inofrmation": user_info,
        "temperature": temperature,
        "motion": Movement
    }     
    with open("user_data.json","a") as file:
        json.dump(data, file, indent=4)
    print("Data saved to json file in computer")


def main():
    print()
    print("**********Welcome to motion detector**********")
    print()
    print("Please confirm your age to continue.")
    while True:
        birthday=input("Enter your birthday in dd/mm/yyyy format: ")
        print()
        time.sleep(1)
        print("Checking Dob validity and eligibility....")
        time.sleep(1)
        if valid_dob(birthday):
            if age_validation(birthday):
                print()
                print("***Access Granted.***")
                break
            else:
                print("\nSorry!! You age must be above 18 to continue.")
                print("Exiting.")
                sys.exit()
        else:
            print("\nDate of birth is in invalid format. Please try Again!.")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print()
    time.sleep(1)
    user = user_right(first_name, last_name)
    
    while True:
        print()
        time.sleep(1)
        print("----------")
        print("   Menu  ")
        print("----------")
        print("1) Generate Username")
        print("2) Generate Password")
        print("3) Play Game")
        print("4) Check temperature using API and Json")
        print("0) Exit ")
        choice = int(input("Please Select Option(1-4)(0 to exit): "))
        if choice == 1:
            print()
            print("Generating username....")
            print()
            time.sleep(1)
            username_generator(first_name, last_name, birthday)
        elif choice == 2:
            while True:
                print()
                time.sleep(1)
                print("*****Password generator*****")
                num_upper = int(input("Enter number of uppercase you want: "))
                num_lower = int(input("Enter number of lowercase you want: "))
                num_digits = int(input("Enter number of digits you want: "))
                num_special= int(input("Enter number of special characters: "))
                password= generate_password(num_upper, num_lower , num_digits , num_special)
                print()
                print(f"*****Your password is: {password}*****")
                emotion = input("Are you happy with the password generated(Yes/NO): ")

                if emotion.lower() == "yes":
                    print()
                    time.sleep(1)
                    print("Redirecting to main menu....")
                    break
                elif emotion.lower() == "no":
                    print()
                    time.sleep(1)
                    print("Generate new password.")
                else:
                    print("Please choose (Yes/No)")
        elif choice == 3:
            print()
            print("Loading Game...")
            time.sleep(1)
            print("*****Game*****")
            while True:
                game()
                print()
                play_again = input("Do you want to play again? (Yes/No): ")
                if play_again not in ['yes']:
                    print("Thanks for playing! goodbye!")
                    break 
        
        elif choice == 4:
            print()
            print("*****Checking the CPU temperature and making Json file*****")
            time.sleep(1.5)
            while True:
                url ="https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=1&timezone=Europe/Helsinki"
                response = requests.get(url)
                print(f"Status code: {response.status_code}")
                data = response.json()
                entry= random.choice(data["feeds"])
                movement_value = entry["field1"]
                temperature_value =  entry["field2"]
                temp = input("Enter the temperature in desired format(C or F): ")
                if temp.upper() == "C":
                        temperature_in_celsius = float(temperature_value)
                        print(f"Temperature is {temperature_in_celsius}°C celsius")
                        temperature_check(temp,temperature_in_celsius)
                        break
                elif temp.upper()== "F":
                        temperature_in_Fahrenheit = float((float(temperature_value) * 9/5) + 32)
                        print(f"Temperature is {temperature_in_Fahrenheit} degree fahrenheit")
                        temperature_check(temp,temperature_in_Fahrenheit)
                        break
                else:
                    print("Invalid format. Please enter 'c' or 'f'.")
            
            Movement = movement_value  
            print(f"Movement value :{Movement}")
            user_info={
                "User's First Name":first_name,
                "User's Last Name": last_name,
                "Date of birth": birthday,
                "User Role": user,
            }

            store_info(user_info, temperature_value, Movement)
        elif choice == 0:
            print()
            time.sleep(1)
            print("Exiting...")
            print()
            time.sleep(1)
            print("Thank you for visiting.")
            break
        else:
            print("Invalid choice!! Please Select Option(1-4)(0 to exit): ")
main()