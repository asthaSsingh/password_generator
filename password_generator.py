#password generator using python
import random
password="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz@#$%&*"
length_password=int(input("enter the length of password:"))
x="".join(random.sample(password,length_password))
print("your password is:",x)
