inputs = input('Write Text: ')
inputs = inputs.lower()
output = []
for character in inputs:
    if character.isalpha():
        number = ord(character) - 96
        output.append(str(number))
        # print('Char', character)
    else:
        pass
print(' '.join(output))
