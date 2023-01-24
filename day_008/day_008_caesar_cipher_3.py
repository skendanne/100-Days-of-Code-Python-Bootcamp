alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# To do 1 - Combine the encrypt() and decrypt() functions into a single
# function called caesar().

# To do 2 - Call the caesar() function, passing over the 'text', 'shift'
# and 'direction' values

def caesar(text, shift, direction):
    text_list = list(text.strip())
    text_index = 0
    encoded_text = ""

    for i in range(len(text_list)):
        if direction == "encode":
            x = alphabet[alphabet.index(text_list[text_index]) + shift]
        elif direction == "decode":
            x = alphabet[alphabet.index(text_list[text_index]) - shift]
        text_list[text_index] = x
        text_index += 1

    for i in text_list:
        encoded_text += i

    print(f"The {direction}d text is {encoded_text}")

# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""

#     if cipher_direction == "decode":
#         shift_amount *= -1

#     for letter in start_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         end_text += alphabet[new_position]
    
#     print(f"The {cipher_direction}d text is {end_text}")

caesar(text, shift, direction)