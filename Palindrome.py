"""The code checks if the given string is palindrome.  The lettercase and spaces between words are ignored"""

def palindrom(string):
    string1 = string.lower()
    string1 = string1.replace(" ","")
    string2 = ""
    for let in range(len(string1)):
        string2 += string1[-1 - let]
    if string1 == string2:
       return "It's a palindrome"
    else:
        return "It's not a palinrome"


# test

print("Ten animals I slam in a net:", palindrom("Ten animals I slam in a net"))
print("Eleven animals I slam in a net", palindrom("Eleven animals I slam in a net"))

