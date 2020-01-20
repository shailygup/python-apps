def longest(s1, s2):
    #change the word into a list
    #find all unique values and sort it in alphabetic order
    #change it back to a word
    #Add both strings into a singular word

    #My attempt
    joinedWords = ''.join(list(s1)) + ''.join(list(s2))
    newWord = ''.join(sorted(set(list(joinedWords))))

    #Best Practice way
    print( "".join(sorted(set(s1 + s2))))

    return newWord
    # your code
if __name__ == "__main__":
    longest("xyaabbbccccdefww", "xxxxyyyyabklmopq")