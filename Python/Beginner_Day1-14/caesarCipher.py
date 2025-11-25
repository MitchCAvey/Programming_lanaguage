alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 
#'shift' as inputs.
def encrypt(direction, text, shift):
    print(len(alphabet))
    #print(type(text))
    plainText = []
    normAlphaIndex = []
    cipherNums = []
    cipherText = []
    plainText += text
    #print(plainText)
    for l in plainText:
        normAlphaIndex.append(alphabet.index(l))
        #normAlphaIndex = int(alphabet.index(l))
        #print(normAlphaIndex)
    
    #print(normAlphaIndex)
    
    for num in range(0, len(normAlphaIndex)):
        #print(normAlphaIndex[num] + 5)
        cipherNums.append(int(normAlphaIndex[num] + shift))
        #cipher_text = alphabet.index(cipherNum)

    for n in cipherNums:
        #print(alphabet[n])
        cipherText.append(alphabet[n])

    print(f"{''.join(cipherText)}")
    
    #for ciphNum in range(0, len(cipherNums)):
        #cipherText.append(alphabet.index(int(ciphNum)))
    #for n in range(0, len(cipherNums)):
    #    print(type(cipherNums[n]))
    #print(cipherText)
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 
    #'text' forwards in the alphabet by the shift amount and print the 
    #encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You 
#should be able to test the code and encrypt a message.

if direction == 'encode':
    encrypt(direction, text, shift)
else:
    pass