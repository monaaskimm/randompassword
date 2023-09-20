import random

passlen = int(input("şifre uzunluğu?"))

def passwordGeneretor(uzunluk) :
    characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(uzunluk):
        password = password + random.choice(characters)
    return password
    
password = passwordGeneretor(passlen)
print(password)
