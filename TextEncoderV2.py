import random
import sys

# Methods that will return the new character based on 
# the new index inputed
def higherEncrypt(index):
    return keyHigherAlpha[index]
def lowerEncrypt(index):
    return keyLowerAlpha[index]
def numEncrypt(index):
    return keyNum[index]   
def spEncrypt(index):
    return keySPChar[index]


# Method that returns the index of the original character 
# based on its location in the reference lists
def getIndex(character):
    if character in keyNum:
        return keyNum.index(character)
    elif character in keyLowerAlpha:
        return keyLowerAlpha.index(character)
    elif character in keyHigherAlpha:
        return keyHigherAlpha.index(character)
    elif character in keySPChar:
        return keySPChar.index(character)


# Method that checks the type of the original character
# and returns a number based on its type
def checkType(character):
    if character in keyNum:
        return random.choice(['0', '1'])
    elif character in keyLowerAlpha:
        return random.choice(['2', '3', '4'])
    elif character in keyHigherAlpha:
        return random.choice(['5', '6', '7'])
    elif character in keySPChar:
        return random.choice(['8', '9'])

    
# Collection of arrays that will serve as the lists that we
# reference characters from 
keyNum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
keyLowerAlpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keyHigherAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
keySPChar = ['!', '@', '#', '$', '%', '&', ' ', '_', '-', '+', '/','?','*', '.', ',' , ':', ';', "'", '!', '@', '#', '$', '%', '&', ' ', '_', '-', '+', '/','?','*', '.', ',' , ':', ';', "'"]

             
####### Main #######
def main(aMessage, fileName):
    text = []
    for element in aMessage:
        if element != "\n":
            text.append(element)
    outputName = fileName

    offset = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    if offset > len(text):
        offset = len(text)
    encryptionTypeKey = ""
    encryptionIndex = []
    encryptedText = ""
    encryption = ""

    for iter1 in range(len(text)):
        #Will chose a random char type as the stand in for the current char
        encryptionType = random.choice([0, 1, 2, 3])    
        char = text.pop()
        encryptionTypeKey += (checkType(char))
        ind = getIndex(char)
        newInd = ind + offset
        encryptionIndex.append(newInd)
    
        # Switch that decides what type of character each element 
        # will be presented as
        # 0 will become numbers
        # 1 will become lowercase letters
        # 2 will become uppercase letters
        # 3 will become special characters
        if encryptionType == 0:
            encryptedText += numEncrypt(newInd)
        elif encryptionType == 1:
            encryptedText += lowerEncrypt(newInd)
        elif encryptionType == 2:
            encryptedText += higherEncrypt(newInd)
        elif encryptionType == 3:
            encryptedText += spEncrypt(newInd)
        

    # Following blocks are for the encryption key rotator
    # length chooses how many elements will be in each rotated element
    messageLength = len(encryptedText)
    if messageLength > 80:    
        length = random.choice([8, 10, 12, 15])
    elif messageLength > 50:
        length = random.choice([5, 7, 9])
    elif messageLength > 20:
        length = random.choice([5, 6, 8])
    else:
        length = random.choice([2, 3, 4])
    rotatorElements = []
    remainder = len(encryptionTypeKey) % length
    starting = 0

    # Breaks up the var encryptionTypeKey into chunks that can be changed around
    while(True):
        rotator = ""
        for i in range(length):
            rotator += encryptionTypeKey[starting + i]
        rotatorElements.append(rotator)
        starting += length
        if((len(encryptionTypeKey) - remainder) == starting):
            break;
        
    # In the common case that the sum of the lengths of each rotated chunk is 
    # not equal to the length of the encrypted phrase a remainder is formed to
    # add the last few indices to the rotator
    if remainder > 0:
        rotator =""
        for i in range(remainder):
            rotator += encryptionTypeKey[starting + i]
        rotatorElements.append(rotator)
    # rotationOrder will be the new altered encryptionTypeKey
    # rotatorKey will allow us to put the encryptionTypeKey back 
    # in the proper order
    rotationOrder = []
    rotatorKey = []
    numRotators = len(rotatorElements)

    # Creates the new rotatorKey and randomizes the order
    for i in range(numRotators):
        rotatorKey.append(i)
    random.shuffle(rotatorKey)

    # Based on the order of the rotatorKey, the rotationOrder
    # will append the chunks of indices
    for element in rotatorKey:
        rotationOrder.append(rotatorElements[element])
    

    encryption = str(offset) + "^" + encryptedText 
    encryptionIndex.reverse()

    f = open(outputName + ".txt", "w")
    f.write("3NCRY\n")
    f.write(encryption + "\n")

    for element in rotationOrder:
        string = str(element)
        f.write(string + "^")
    f.write("\n")

    for element in encryptionIndex:
        char = str(element)
        f.write(char + '.')
    f.write("\n")

    for element in rotatorKey:
        char = str(element)
        f.write(char + '.')
    f.write("\n")
    f.close()