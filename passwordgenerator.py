import random
import string

def generate_password(length):
    a=random.randint(0,9)
    c=str(a)
    characters = string.ascii_letters + string.digits + c
    password = ""
    for i in range(length):
        password+=random.choice(characters)
    return password
while (True):
    print("-----------PASSWORD GENERATOR------------")
    length=int(input("ENTER THE LENGTH OF PASSWORD YOU WANT => "))
    print("YOUR RANDOM PASSWORD OF LENGTH ",length,"IS")
    password = generate_password(length)
    print(password)
    print(''' CHOOSE ONE OF THE FOLLOWING OPTION :
    1.) GENERATE ANOTHER PASSWORD
    2.) EXIT ''')
    num=int(input())
    if num==1 :
        continue
    elif num==2:
        print("Thanks for using password generator ")
        break
    else :
        print("please enter a valid input .")

