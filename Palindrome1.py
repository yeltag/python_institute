"""The 2nd variant of Palindrome code.  The code checks if the given string is a palindrome.  The lettercase and spaces between words are ignored"""

def palindrom1 (string):
    string = string.lower()
    string = string.replace(" ","")
    string1 = list(string)
    string2 = ""
    for let in range(len(string1)//2):
        string1[let], string1[-1-let] = string1[-1-let],string1[let]
    for let in range(len(string1)):
        string2 += string1[let]

    if string == string2:
        return "It's a palindrome"
    else:
        return "It's not a palindrome"



#test

print("Ten animals I slam in a net:", palindrom1("Ten animals I slam in a net"))
print("Eleven animals I slam in a net:", palindrom1("Eleven animals I slam in a net"))

