#4 - Combining Encrypt or Decrypt Functions

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def choice():                                             
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    return text, shift                                    #Return necessary to Unpack Variables

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(start_text, shift_value, direction_value):
    end_text = ""

    if direction_value == "decode":
            shift_value *= -1

    for letter in start_text:
        start_letter_index = alphabet.index(letter)

        end_letter_index = start_letter_index + shift_value
        end_letter = alphabet[end_letter_index]
        end_text += end_letter

    print(f"The {direction_value}d text is {end_text}.")

# def encrypt(plain_text, shift_value):                     #Function: Encrypt
#     cipher_text = ""

#     for letter in plain_text:
#         plain_letter_index = alphabet.index(letter)
#         cipher_letter_index = plain_letter_index + shift_value
        
#         cipher_letter = alphabet[cipher_letter_index]
#         cipher_text += cipher_letter
    
#     print(f"The Encoded text is {cipher_text}.")

# def decrypt(cipher_text, shift_value):                     #Function: Decrypt 
#     plain_text = ""

#     for letter in cipher_text:
#         cipher_letter_index = alphabet.index(letter)
#         plain_letter_index = cipher_letter_index - shift_value
        
#         plain_letter = alphabet[plain_letter_index]
#         plain_text += plain_letter
    
#     print(f"The Decoded text is {plain_text}")

while True:                                                   #Encrypt/Decrypt choice
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == "encode" or direction == "decode":        #Try again loop for different responses 
        break
    else:
        print("Try again!")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
text, shift = choice()                                         #Unpacking Variables choice()
caesar(direction_value = direction, start_text = text, shift_value = shift)
