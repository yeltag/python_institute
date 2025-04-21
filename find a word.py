#! /user/bin/env python
"""This code find characters of the first srting in the second string.  Returns "yes" if found and "No" if not """

def find_word(string1,string2):
    string1 = string1.lower()
    string2 = string2.lower()
    symbols ={}
    for key in string1:
        if key in symbols:
            symbols[key] = string2.find(key,(symbols[key]+1))
        else:
            symbols[key]=""
            symbols[key] = string2.find(key)
    for keys in symbols:
         if  symbols[keys] == -1:
             return "No"
    else:
         return "Yes"

# test

print("donor","Nabucodonosor -",find_word("donor","Nabucodonosor")=="Yes")
print("donut","Nabucodonosor -",find_word("donut","Nabucodonosor")=="No")

string1 = input("Enter string1:")
string2 = input("Enter string2:")
print(find_word(string1,string2))