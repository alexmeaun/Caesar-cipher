# with open('caesar.txt', 'w') as f:
#     text = '''Shakespeare was born and raised in Stratford-upon-Avon.
# At the age of 18, he married Anne Hathaway, with whom he had three children
# Hamlet is considered among the most powerful and influential works of world literature
#     '''
#     f.writelines(text)
#
# with open('caesar.txt', 'r') as f:
#     for lines in f.readlines():
#         print(lines)


def shift_amount(i):
    '''In order to avoid an error by exeeding the length of the alphabet, we need this function'''
    return i % 26


def encrypt(text, shifter):
    text = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in text:
        if char not in alphabet:  # In case there's a space,a dot or a comma, in order to avoid confusions
            output += char
        else:
            alpha_index = alphabet.find(char)  # Finding the index of the text character from the alphabet
            output += alphabet[shift_amount(alpha_index + shifter)]  # Increasing the index by "shifter" and therefore, changing the character

    print(output)


L = 'Shakespeare was born and raised in Stratford-upon-Avon.'
print(L)
encrypt(L, -4)

