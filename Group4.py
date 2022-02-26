# Authors: Justin Swain, LaCreatia Harris, Nicholas Kimmel, Kate Cain
# Date: February 25, 2022
#
# HOW TO RUN
#
# Change to whatever directory you have the files saved in. (cd 'directoryname' in cmd on Windows. IDK about you Mac users)
#
# Use the commands below. Only encrypt and decrypt work for now
#
#
# python main.py –e <file to be encrypted> key <output file>
#
# python main.py –d <file to be decrypted> key <output file>
#
# python main.py –c <file to crack>

import sys

arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z"]
key = 0 # Varable used for the key encryption and decryption

# Function to write to file
def writeToFile(string, outputFile):
    file = open(outputFile, "w")
    file.write(string)
    file.close()

# Encryption Function
def encrypt(line):
    encryptedString = ""
    encryptedWord = ""
    line = readFile(line)
    line = line.split()
    global key # Global variable created and the variable is used to read and write in functions
    key = key % 26
    for word in line: # Checking each plaintext characters range of each line in the file
        for letter in word:
            shift = arr.index(letter) + key # Shifting the plain text using the key
            if shift >= len(arr): # Encrypt the plain text
                shift = shift % 26
            encryptedWord = encryptedWord + arr[shift]

        encryptedString = encryptedString + ' ' + encryptedWord
        encryptedWord = ""

    return encryptedString

# Decryption Function
def decrypt(line):
    decryptedString = ""
    decryptedWord = ""
    line = readFile(line)
    line = line.split()
    global key # Global variable created and the variable is used to read and write in functions
    key = key % 26
    for word in line: # Checking each ciphertext characters range of each line in the file
        for letter in word:
            shift = arr.index(letter) - key # Shifting the ciphertext using the key
            if shift <= len(arr): # Decrypt the ciphertext
                shift = shift % 26
            decryptedWord = decryptedWord + arr[shift]
        decryptedString = decryptedString + ' ' + decryptedWord
        decryptedWord = ""
    return decryptedString

# Read File Function
def readFile(file):
    try:
        with open(file) as f:
            line = f.read()
            line = line.lower()
            return line

    except FileNotFoundError: # Catching errors if file is not located in the program
        print("Could not open file")

# Check Word Function reading each word from dictionary text file
def checkWord(string):
    with open('dictionary.txt', 'r') as f:
        lines = f.readlines()
        string = string + '\n'
        for line in lines:
            if string == line:
                return True

        return False

#Brute Force Function
def bruteForce(file):
    decryptedWord = ''
    finalDecrypt = ""
    count = 0
    with open(file) as f:
        line = f.readline()
        line = line.lower()
    line = line.split()
    for key in range(1, 25): # Attack is done by trial and error by checking the range from 1-25 to find the possible key by opening the file 'bruteForce.txt' and splitting each line
        for word in line:
            for letter in word: # Attack makes the shift value increase by 26 and establishes the decryptedWord along with the array index for the shift value
                shift = arr.index(letter) - key
                if shift < 0: # Checking if the shift is less than zero
                    shift = shift + 26
                decryptedWord = decryptedWord + arr[shift]
            if checkWord(decryptedWord):
                count += 1 # Increases the 'count' counter by 1 every time
            finalDecrypt = finalDecrypt + ' ' + decryptedWord
            decryptedWord = ''
        if count / len(line) >= 0.7:
            print(finalDecrypt + ': key = ' + str(key))
        finalDecrypt = '' # Final decrypt variable then becomes finalDecrypt along with decryptedWord from above
        count = 0 # Count becomes 0 if the 'count/len(line) is greater than or equal to 0.7

# Main
if __name__ == '__main__':
    arguments = len(sys.argv)
    if arguments != 5 and arguments != 3:
        print("Please enter correct arguments")
    else:

        if sys.argv[1] == '-e': # Encrpting the file
            try:
                key = int(sys.argv[3])
                encryptedText = encrypt(sys.argv[2])
                outputFile = sys.argv[4]
                writeToFile(encryptedText, outputFile)
            except ValueError:
                print("Illegal entry")
            except IndexError:
                print("Illegal entry")

        elif sys.argv[1] == '-d':# Decrypting the file to get the plain text
            try:
                key = int(sys.argv[3])
                decryptedText = decrypt(sys.argv[2])
                outputFile = sys.argv[4]
                writeToFile(decryptedText, outputFile)
            except ValueError:
                print("Illegal entry")
            except IndexError:
                print("Illegal entry")

        elif sys.argv[1] == '-c':# Cracking the file to get the plain text
            try:
                bruteForce(sys.argv[2])
            except ValueError:
                print("Illegal entry")
            except IndexError:
                print("Illegal entry")
