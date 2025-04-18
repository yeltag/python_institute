def anagram (string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    while string1 == string2 == "":
        string1 = input ("Enter string1:")
        string2 = input ("Enter string2:")

    if len(string1) != len(string2):
        return "Not anagrams"
    elif string1.count(" ") == len(string1) or string2.count(" ") == len(string2):
        return "Not anagrams"
    else:
        for letter in string1:
            if string1.count(letter) != string2.count(letter):
                return "Not anagrams"
        return "Anagrams"

string1 = input("Enter string1:")
string2 = input("Enter string2:")

print(anagram(string1,string2))

# test

print("Listen","Silent","-",anagram("listen","Silent"))
print("modern","norman","-",anagram("modern","norman"))