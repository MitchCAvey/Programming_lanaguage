alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(startText, shiftAmount, cipherDirection):
    endText = ""
    if cipherDirection == "decode":
        shiftAmount *= -1
    for l in startText:
        position = alphabet.index(l)
        newPosition = position + shiftAmount
        endText += alphabet[newPosition]
    print(f"The {cipherDirection}d text is {endText}")

caesar(startText=text, shiftAmount=shift, cipherDirection=direction)

"""
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 
#'shift' as inputs.

def encrypt(text, shift):
    cipherText = ""
    for l in text:
        currentPosition = alphabet.index(l)
        shiftedPosition = currentPosition + shift
        newLetter = alphabet[shiftedPosition]
        cipherText += newLetter
    print(f"The encoded test is {cipherText}")

#TODO-3: Call the encrypt function and pass in the user inputs. You 
#should be able to test the code and encrypt a message.
def decrypt(ciperText, shiftAmount):
    plainText = ""
    for l in ciperText:
        position = alphabet.index(l)
        newPosition = position - shiftAmount
        plainText += alphabet[newPosition]
    print(f"The decoded text is {plainText}")

if direction == 'encode':
    encrypt(text=text, shift=shift)
else:
    decrypt(ciperText=text, shiftAmount=shift)

"""
