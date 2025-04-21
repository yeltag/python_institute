#! /user/bin/env python
""" This code calculates digit of life"""

import days_elapsed_in_a_year as days

def digit_of_life(birthday):
    while birthday.isdigit() == False or len(birthday) != 8:
        birthday = input("The entered date is not valid.  Enter your birthday in format YYYYMMDD:")
    while int(birthday[4:6]) > 12 or int(birthday[4:6]) == 0 or int(birthday[6:]) == 0:
        birthday = input("The entered date is not valid.  Enter a valid date in format YYYYMMDD:")
    while days.is_year_leap(int(birthday[:4])) == True and birthday[4:6] == "02" and int(birthday[6:]) > 29:

        birthday = input("The entered date is not valid.  Enter a valid date in format YYYYMMDD:")
    while days.is_year_leap(int(birthday[:4])) == False and birthday[4:6] == "02" and int(birthday[6:]) > 28:
        birthday = input("The entered date is not valid.  Enter a valid date in format YYYYMMDD:")
    while  (birthday[4:6] == "04" or birthday[4:6] == "06" or birthday[4:6] == "09" or birthday[4:6] == "11") and int(birthday[6:]) > 30:
        birthday = input("The entered date is not valid.  Enter a valid date in format YYYYMMDD:")
    while (birthday[4:6] == "01" or birthday[4:6] == "03" or birthday[4:6] == "05" or birthday[4:6] == "07" or birthday[4:6] == "08" or birthday[4:6] == "10" or birthday[4:6] == "12") and int(birthday[6:]) > 31:
        birthday = input("The entered date is not valid.  Enter a valid date in format YYYYMMDD:")
    birthday1 = birthday[:]
    while len(birthday1) > 1:
        digit = 0
        for dig in birthday1:
            digit += int(dig)
        birthday1 = str(digit)

    return digit


# test

print ("19991229:",digit_of_life("19991229") == 6)
print ("20000101:",digit_of_life("20000101") == 4)


print(digit_of_life(input("Enter your birthday in format YYYYMMDD:")))