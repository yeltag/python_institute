#! /user/bin/env python

"""This code encrypts a string entered by user by shifting it forward by a number of positions entered by user.
The letters' case and all non-alphabetical characters remain unchanged."""

def ceasar_cipher (string,shift):

    while str(shift).isdigit() == False or int(shift) not in range(1,26):
            shift = input("Enter a shift value in range from 1 to 25:")


    encrypted = ''
    for letter in string:
        if ord(letter) > 64 and ord(letter) < (91 - int(shift)) or ord(letter) > 96 and ord(letter) <(123 - int(shift)):
            encrypted += (chr(ord(letter) + int(shift)))
        elif ord(letter) >= 91 - int(shift) and ord(letter) < 91:
            encrypted += chr(64 + int(shift) - (90 - ord(letter)))
        elif  ord(letter) >= 123 - int(shift) and ord(letter) < 123:
            encrypted += chr(96 + int(shift) - (122 - ord(letter)))
        else:
            encrypted += letter
    return encrypted




print("abcxyzABCxyz 123","2"," : ",ceasar_cipher("abcxyzABCxyz 123",2) == "cdezabCDEzab 123")
print("The die is cast","25"," : ",ceasar_cipher("The die is cast",25) == "Sgd chd hr bzrs")

print(ceasar_cipher(input("Enter a string to encript:"),input("Enter a shift value in range from 1 to 25:")))