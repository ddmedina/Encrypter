keyNum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
keyLowerAlpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keyHigherAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
keySPChar = ['!', '@', '#', '$', '%', '&', ' ', '_', '-', '+', '/','?','*', '.', ',' , ':', ';', "'", '!', '@', '#', '$', '%', '&', ' ', '_', '-', '+', '/','?','*', '.', ',' , ':', ';', "'"]
             
class Error(Exception):
    pass
class NoEncryption(Error):
    pass

while(True):
    fileName = input("Enter the name of the encrypted file you wish to open: ")
    try:
        f = open(fileName + ".txt", 'r')
        line1 = f.readline(-1).strip()
        if line1 != "3NCRY":
            raise NoEncryption
    except NoEncryption:
        print("This file is not encrypted! Please try again.")
    else:
        break

# Reads in the offset number along with the message
encryptedArray = f.readline(-1).split('^')
offset = encryptedArray[0]
#encodedMessage = encryptedArray[1].rstrip("\n")

# Reads the rotated character type array of the encoded file
typeArray = f.readline(-1).split("^")
typeArray.pop()             #Removes the n\ character


# Reads in the index array for each character
IndexArray = f.readline(-1).split(".")
IndexArray.pop()            #Removes the \n character
IndexArray.reverse()


# Reads in the key for the rotated character type array
# and converts each entyr to an int, which is then appended 
# to a new array
rotatorKeyArray = f.readline(-1).split(".")
rotatorKeyArray.pop()       #Removes the \n character
rKeyArray = []
for i in range(len(rotatorKeyArray)):
    rKeyArray.append(int(rotatorKeyArray[i]))
f.close()

# Creates a dictionary of original position keys
# and the character type values and assigns the 
# original positions to their chunk of type-integers
d = {}
for element in range(len(rKeyArray)):
    d.update({rKeyArray[element]: typeArray[element]})


# Re-constructs the character type array by retrieving 
# values of the previously constructed dictionary
actualKey = ""
for i in range(len(d)):
    actualKey += d.get(i)


# Instantiation of a list to house the decrypted characters
# and of the string that houses the decrypted message
decodedLst = []
#decodedMesaage = ""


# Simple method that accesses a list and returns the 
# character at the provided index
# *NOTE* the provided index is taken from the difference of
# the array of indicies and the offset value
def getChar(aLst, index):
    decodedLst.append(aLst[index])


ind = 0
for i in range(len(actualKey)):
    charIndex = int(IndexArray[ind]) - int(offset)
    if actualKey[i] == '0' or actualKey[i] == '1':
        #char in keyNum
        getChar(keyNum, charIndex)
        ind += 1
    elif actualKey[i] == '2' or actualKey[i] == '3' or actualKey[i] == '4':
        #char in keyLowerAlpha
        getChar(keyLowerAlpha, charIndex)
        ind += 1
    elif actualKey[i] == '5' or actualKey[i] == '6' or actualKey[i] == '7':
        #char in keyHigherAlpha
        getChar(keyHigherAlpha, charIndex)
        ind += 1
    elif actualKey[i] == '8' or actualKey[i] == '9':
        #char in keySPChar
        getChar(keySPChar, charIndex)
        ind += 1
        

decodedLst.reverse()    #Reverse the list to get the proper message

of = open("Decoded Message.txt", "w")
for eachElement in decodedLst:
    of.write(eachElement)
of.close()