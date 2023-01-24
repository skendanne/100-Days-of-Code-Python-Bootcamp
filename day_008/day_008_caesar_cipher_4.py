import caesar_cipher_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(caesar_cipher_art.logo)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

# To do 1 - Import and print the logo from art.py when the program starts.

# To do 2 - What if the user enters a shift that is greater than the
# number of letter in the alphabet? Try running the program and entering
# a shift number of 45.
#     Add some code so that the program continues to work even if the user
# enters a shift number greater than 26.
#     Think about how you can use the modulus (%).

# To do 3 - What happens if the user enters a number/symbol/space?
# Can you fix the code to keep the number/symbol/space when the text is
# encoded/decoded?

# To do 4 - Can you figure out a way to ask the user if they want to
# restart the cupher program? Try creating a while loop that continues to
# execute the program if the user types 'yes'..

    def caesar(text, shift, direction):
        text_list = list(text.strip())
        text_index = 0
        encoded_text = ""

        for i in range(len(text_list)):
            if i in alphabet:
                if direction == "encode":
                    x = alphabet[alphabet.index(text_list[text_index]) + shift]
                elif direction == "decode":
                    x = alphabet[alphabet.index(text_list[text_index]) - shift]
                text_list[text_index] = x
                text_index += 1
            else:
                text_index += i

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

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if result == "no":
        should_continue = False
        print("Goodbye")