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

    caesar(text, shift, direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if result == "no":
        should_continue = False
        print("Goodbye")