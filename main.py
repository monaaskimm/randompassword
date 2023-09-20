import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passlen = int(input("şifre uzunluğu?"))
password = ""

for i in range(passlen):
    password = password + random.choice(characters)
    print(i)
    print(password)

print(password)
