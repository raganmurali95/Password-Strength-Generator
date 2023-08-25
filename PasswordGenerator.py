import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*().,/~"

string = lower + upper + digits + symbols
length = int(input("Enter a number between 8-16 for Password : "))
if(length > 7 and length < 17):
    password = "".join(random.sample(string,length))
    print("Your Password is:  ",password)
else:
    print("Cant Generate password with the given length!!!")

