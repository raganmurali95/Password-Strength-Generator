import re
count = 10

password = input("Enter Your Password: ")

if(len(password)<8):
    count-=3
if not (re.search("[A-Z]",password)):
    count-=2
if not (re.search("[a-z]",password)):
    count-=2    
if not (re.search("[0-9]",password)):
    count-=2
if not (re.search("[~!@#$%^&*()]",password)):
    count-= 1.5

print("Your Password Strength is: ",count,"out of 10")