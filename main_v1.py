# # 1 - Encrypt

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"

#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# def encrypt(plain_text, shift_value):
#     cipher_text = ""

#     for letter in plain_text:
#         plain_letter_index = alphabet.index(letter)
#         # print(letter_index)
#         cipher_letter_index = plain_letter_index + shift_value
#         # print(cipher_letter_index)
#         cipher_letter = alphabet[cipher_letter_index]
#         cipher_text += cipher_letter
    
#     print(cipher_text)

# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# encrypt(plain_text = text, shift_value = shift)


# 2 - Decrypt

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

# #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#   #e.g. 
#   #cipher_text = "mjqqt"
#   #shift = 5
#   #plain_text = "hello"
#   #print output: "The decoded text is hello"

# def decrypt(plain_text, shift_value):
#     cipher_text = ""

#     for letter in plain_text:
#         plain_letter_index = alphabet.index(letter)
#         cipher_letter_index = plain_letter_index - shift_value
        
#         cipher_letter = alphabet[cipher_letter_index]
#         cipher_text += cipher_letter
    
#     print(cipher_text)

# decrypt(plain_text = text, shift_value = shift)


# 3 - Choose b/w Encrypt or Decrypt

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def choice():                                             #Function: Encrypt or Decrypt choice
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    return text, shift                                    #Return necessary to Unpack Variables

def encrypt(plain_text, shift_value):                     #Function: Encrypt
    cipher_text = ""

    for letter in plain_text:
        plain_letter_index = alphabet.index(letter)
        cipher_letter_index = plain_letter_index + shift_value
        
        cipher_letter = alphabet[cipher_letter_index]
        cipher_text += cipher_letter
    
    print(f"The Encoded text is {cipher_text}")

def decrypt(cipher_text, shift_value):                     #Function: Decrypt 
    plain_text = ""

    for letter in cipher_text:
        cipher_letter_index = alphabet.index(letter)
        plain_letter_index = cipher_letter_index - shift_value
        
        plain_letter = alphabet[plain_letter_index]
        plain_text += plain_letter
    
    print(f"The Decoded text is {plain_text}")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.#

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

if direction == "encode":
    # text = input("Type your message:\n").lower()
    # shift = int(input("Type the shift number:\n"))
    text, shift = choice()                                  #Unpacking Variables choice()
    encrypt(plain_text = text, shift_value = shift)
    
elif direction == "decode":    
    # text = input("Type your message:\n").lower()
    # shift = int(input("Type the shift number:\n"))
    text, shift = choice()                                  #Unpacking Variables choice()
    decrypt(cipher_text = text, shift_value = shift)

else:
    print("No Access!")
