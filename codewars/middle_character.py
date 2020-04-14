# Get the middle character.
# For a given word, return the middle character of the word
# If the word's length is odd, return the middle
# else if it is even return the middle 2 characters


# Solution
def get_middle(s):
    # divmod takes two numbers and returns a pair of number
    # quotient and remainder
    index, odd = divmod(len(s), 2)
    if odd:
        return s[index]
    else:
        return s[index - 1: index + 1]

    # Original
    # return s[index] if odd else s[index - 1:index + 1]


# My Solution
# def get_middle(text):

#     # determine if the text length is odd or even
#     # find it out by getting the length and %2

#     if len(text) % 2 == 0:

#         list1 = []
#         list1.append(text[int(len(text) / 2) - 1])
#         list1.append(text[int(len(text)/2)])
#         return "".join(list1)
#     else:
#         if len(text) == 1:
#             return text
#         return text[int(len(text) / 2)]


if __name__ == "__main__":

    print(get_middle("test"))
    print(get_middle("A"))
    print(get_middle("testing"))
    print(get_middle("middle"))

    # Test Cases
    assert get_middle("test") == "es", "Should be es"
    assert get_middle("testing") == "t", "Should be t"
    assert get_middle("middle") == "dd", "Should be dd"
    assert get_middle("A") == "A", "Should be A"
