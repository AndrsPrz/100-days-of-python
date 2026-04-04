"""
caesar.py
=========
A command-line Caesar Cipher tool that can both encrypt and decrypt messages.
 
The Caesar Cipher is one of the oldest and simplest encryption techniques.
It works by shifting each letter in a message a fixed number of positions
along the alphabet. For example, with a shift of 3, 'a' becomes 'd',
'b' becomes 'e', and so on. Decoding reverses the shift.
 
Features
--------
- Encode (encrypt) any text message using a custom shift number.
- Decode (decrypt) a previously encoded message with the correct shift.
- Non-alphabetic characters (spaces, numbers, punctuation) are preserved as-is.
- The shift wraps around the alphabet, so a shift of 27 is the same as 1.
- The program loops until the user decides to quit.
 
Dependencies
------------
- art : third-party package used to display the ASCII logo at startup.
        Install with: pip install art
 
Usage
-----
    python caesar.py
 
Part of the 100 Days of Code - Python Bootcamp (Day 8).
"""
 
from art import logo
 
# Display the project logo at startup
print(logo)
 
# The full lowercase alphabet used as the cipher reference
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
 
 
def caesar(original_text: str, shift_amount: int, encode_or_decode: str) -> None:
    """Encode or decode a message using the Caesar Cipher algorithm.
 
    Each letter in *original_text* is shifted forward (encode) or backward
    (decode) by *shift_amount* positions within the alphabet. The shift
    wraps around using modulo arithmetic, so it always produces a valid
    letter regardless of how large the shift is.
 
    Non-alphabetic characters — spaces, digits, punctuation — are passed
    through unchanged.
 
    Parameters
    ----------
    original_text : str
        The message to process. Should already be lowercase; uppercase
        characters are treated as non-alphabetic and passed through as-is.
    shift_amount : int
        Number of positions to shift each letter. Any positive integer is
        valid; the modulo operation handles values larger than 25.
    encode_or_decode : str
        Either ``"encode"`` to encrypt or ``"decode"`` to decrypt.
        When decoding, the shift is applied in the opposite direction.
 
    Returns
    -------
    None
        The result is printed directly; the function has no return value.
 
    Examples
    --------
    >>> caesar("hello", 3, "encode")
    Here is the encoded result: khoor
 
    >>> caesar("khoor", 3, "decode")
    Here is the decoded result: hello
 
    >>> caesar("hello world!", 3, "encode")
    Here is the encoded result: khoor zruog!
    """
    output_text = ""
 
    # Decoding is just encoding in the opposite direction
    if encode_or_decode == "decode":
        shift_amount *= -1
 
    for letter in original_text:
        if letter in alphabet:
            # Shift the letter's position, wrapping around with modulo
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            # Preserve spaces, numbers, punctuation unchanged
            output_text += letter
 
    print(f"Here is the {encode_or_decode}d result: {output_text}")
 
 
# ---------------------------------------------------------------------------
# Main loop — keeps running until the user types 'no'
# ---------------------------------------------------------------------------
 
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
 
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
 
    again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if again == "no":
        print("Goodbye!")
        break
