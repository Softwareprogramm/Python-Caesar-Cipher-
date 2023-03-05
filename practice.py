import caesarcipher

print(caesarcipher.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(acquired_text, num_shift, direction_taken):
    caesar_result = ""
    for letter in acquired_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction_taken == "encode":
                new_position = position + num_shift
            else:
                new_position = position - num_shift
            caesar_result += alphabet[new_position]
        else:
            caesar_result += letter
    print(f"The {direction_taken} text is: {caesar_result}")


recurring = True
while recurring:
    user = input("Type 'yes' to continue or 'no' to end the program: ").lower()
    if user == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift %= 26
        caesar(acquired_text=text, num_shift=shift, direction_taken=direction)
    else:
        recurring = False
        print("\nThank you for using Caesar-Cipher. Goodbye!")
