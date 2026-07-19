# def caesar(text, shift, encrypt=True):

#     if not isinstance(shift, int):
#         return 'Shift must be an integer value.'

#     if shift < 1 or shift > 25:
#         return 'Shift must be an integer between 1 and 25.'

#     alphabet = 'abcdefghijklmnopqrstuvwxyz'

#     if not encrypt:
#         shift = - shift
    
#     shifted_alphabet = alphabet[shift:] + alphabet[:shift]
#     translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
#     encrypted_text = text.translate(translation_table)
#     return encrypted_text

# def encrypt(text, shift):
#     return caesar(text, shift)
    
# def decrypt(text, shift):
#     return caesar(text, shift, encrypt=False)

# normal_text = "Caesar is found in unlikely places."
# encrypted_text_1 = encrypt(normal_text , 5)
# print(encrypted_text_1)

# encrypted_text_2 = "Pbhentr vf sbhaq va hayvxryl cynprf."
# decrypted_text = decrypt(encrypted_text_2, 13)
# print(decrypted_text)








from math import ceil, floor


def caesar(text , shift , encrypt = True) :
    if not isinstance(shift , int) :
        return "shift must be integer value" 
    if shift > 25 or shift < 1 :
        return "shift must be btwn 1 and 25" 
    if not encrypt :
        shift = -shift

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    shifted_alphabet = alphabet[shift : ] + alphabet[ : shift]

    to_be_translated = str.maketrans(alphabet + alphabet.upper() ,shifted_alphabet + shifted_alphabet.upper() )

    encrypted_text = text.translate(to_be_translated)
    return encrypted_text


def encrypt(text , shift):
    return caesar(text , shift , True)

def decrypt(text , shift ):
    return caesar(text , shift , False)

text1 = 'i am ahmed haitham' 
text2 = 'ifmmp'

print(encrypt(text1 , 4))
print(decrypt(text2 , 1))


# yeah, i did it finally!

