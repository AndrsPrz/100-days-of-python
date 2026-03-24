alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt(text, shift):

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
    plain_text = []
    encoded = []

    text2 = ""

    for i in text:
        if i in alphabet:
            plain_text.append(alphabet.index(i))
    # print(plain_text)

    for i in plain_text:
        encoded.append((i + shift) % 26)

    # print(encoded)
    # print(text)

    for i in encoded:
        text2 += alphabet[i]

    # print(final_tex)
    print(f"Here is the ecoded result: {text2}")

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

#         encoded.append((i + shift) % 26)
# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
if direction == "encode":
    encrypt(text, shift)
else :
    print("Invalid input")
# elif direction == "decode":
# # encrypt(text, shift)

