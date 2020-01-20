import string
def longest(s1, s2):
    
    # sortedS1 = ''.join(set(s1))
    # sortedS2 = ''.join(set(s2))
    result = ''

    for letter in string.ascii_letters:
        if s1.count(letter) >= 1 and s2.count(letter) >= 1:
            result+=letter
        # if s2.count(letter) >= 1:
        #     result+=letter

    # joinedWords = sortedS2 + sortedS1
    result = list(result)
    result.sort()
    result = ''.join(result)
    # sorted(joinedWords)
    print(result)
    

    # your code

if __name__ == "__main__":
    longest("xyaabbbccccdefww", "xxxxyyyyabklmopq")