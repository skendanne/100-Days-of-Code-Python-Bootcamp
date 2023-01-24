alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# To do 1 - Create a different function called 'decrypt' that takes the
# 'text' and 'shift' as inputs.

# To do 2 - Inside the 'decrypt' function, shift each letter of the 'text'
# *backwards* in the alphabet by the shift amount and print the decrypted text.

# To do 3 - Check if the user wanted to encrypt or decrypt the message by
# checking the 'direction' variable. Then call the correct function based
# on that 'direction' variable. You should be able to test the code 
# to encrypt *AND* decrypt a message.

def encrypt(text, shift):
    text_list = list(text.strip())
    text_index = 0
    encoded_text = ""

    for i in range(len(text_list)):
        x = alphabet[alphabet.index(text_list[text_index]) + shift]
        text_list[text_index] = x
        text_index += 1

    for i in text_list:
        encoded_text += i

    print(f"The encoded text is {encoded_text}")

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""

#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter

#     print(f"The encoded text is {cipher_text}")

def decrypt(text, shift):
    text_list = list(text.strip())
    text_index = 0
    decoded_text = ""

    for i in range(len(text_list)):
        x = alphabet[alphabet.index(text_list[text_index]) - shift]
        text_list[text_index] = x
        text_index += 1

    for i in text_list:
        decoded_text += i

    print(f"The decoded text is {decoded_text}")

# def decrypt(cipher_text, shift_amount):
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter

#     print(f"The decoded text is {cipher_text}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)