import string

# My way
# def toJadenCase(String):
#     print(String)
#     newString = string.capwords(String)
#     print(newString)
#     return newString

# Best Practice
def toJadenCase(string):
    print("Original: " + string)
    # Splits each word in the sentence into a list : for w in string.split()
    # Capitalizes the first letter of each word : w.capitalize()
    # Now we have to bring it all back together and add space : " ".join
    newString= " ".join(w.capitalize() for w in string.split()) 
    print("New: " + newString)
    return newString

if __name__ == '__main__':
    toJadenCase("How can mirrors be real if our eyes aren't real")

#Notes:
# - Join can only be used with lists and it must have a delimeter