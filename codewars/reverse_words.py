# Codewars Training - Reverse the words
# Reverses each each word in the string while retaining all the spaces

# Best Answer on Codewars
# def reverse_words(str):
#     return ' '.join(s[::-1] for s in str.split(' '))


# My Answer
def reverse_words(word):
    # split each word using the space delimeter
    split_up = word.split(" ")
    reverse_words = [each_word[::-1] for each_word in split_up]

    return " ".join(reverse_words)


if __name__ == "__main__":
    pass

    print(reverse_words("This is an example!"))
    print(reverse_words("double  spaces"))

    # Test Cases
    assert (
        reverse_words("This is an example!") == "sihT si na !elpmaxe"
    ), "Should be sihT si na !elpmaxe"
    assert (
        reverse_words("double  spaces") == "elbuod  secaps"
    ), "Should be elbuod  secaps"
