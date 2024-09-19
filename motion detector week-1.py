firstname=input("Enter your first name. ")
lastname=input("Enter your last name. ")
birthday=input("Enter your date of birth in (dd/mm/yyyy):")
print (f"hello {firstname} {lastname} welcome to the Motion Detector! Let's Start.")
Username= firstname[:2] + lastname[:3] + birthday[-4:] + birthday[3:5] + birthday[:2]
print(f"your username is: {Username}")
movement= input("Has there been any movement in the room? (yes/no)")
if movement .lower() == "yes":
    print("Movement detected: YES")
else:
    print("Movement detected: NO")

celsius=input("Enter temperature in celsius: ")
celsius=float(celsius)
fahrenheit= (celsius * 9/5) + 32
print(f"The given temperature{celsius}C  is {fahrenheit}F")