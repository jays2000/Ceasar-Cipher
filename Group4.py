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
key = 0


def writeToFile(string, outputFile):
    file = open(outputFile, "w")
    file.write(string)
    file.close()


def encrypt(line):
    encryptedString = ""
    encryptedWord = ""
    line = readFile(line)
    line = line.split()
    global key
    key = key % 26
    for word in line:
        for letter in word:
            shift = arr.index(letter) + key
            if shift >= len(arr):
                shift = shift % 26
            encryptedWord = encryptedWord + arr[shift]

        encryptedString = encryptedString + ' ' + encryptedWord
        encryptedWord = ""

    return encryptedString


def decrypt(line):
    decryptedString = ""
    decryptedWord = ""
    line = readFile(line)
    line = line.split()
    global key
    key = key % 26
    for word in line:
        for letter in word:
            shift = arr.index(letter) - key
            if shift <= len(arr):
                shift = shift % 26
            decryptedWord = decryptedWord + arr[shift]
        decryptedString = decryptedString + ' ' + decryptedWord
        decryptedWord = ""
    return decryptedString


def readFile(file):
    try:
        with open(file) as f:
            line = f.read()
            line = line.lower()
            return line

    except FileNotFoundError:
        print("Could not open file")


def checkWord(string):
    with open('dictionary.txt', 'r') as f:
        lines = f.readlines()
        string = string + '\n'
        for line in lines:
            if string == line:
                return True

        return False


def bruteForce(file):
    decryptedWord = ''
    finalDecrypt = ""
    count = 0
    with open(file) as f:
        line = f.readline()
        line = line.lower()
    line = line.split()
    for key in range(1, 25):
        for word in line:
            for letter in word:
                shift = arr.index(letter) - key
                if shift < 0:
                    shift = shift + 26
                decryptedWord = decryptedWord + arr[shift]
            if checkWord(decryptedWord):
                count += 1
            finalDecrypt = finalDecrypt + ' ' + decryptedWord
            decryptedWord = ''
        if count / len(line) >= 0.7:
            print(finalDecrypt + ': key = ' + str(key))
        finalDecrypt = ''
        count = 0


if __name__ == '__main__':
    arguments = len(sys.argv)
    if arguments != 5 and arguments != 3:
        print("Please enter correct arguments")
    else:

        if sys.argv[1] == '-e': # encrpting the file
            try:
                key = int(sys.argv[3])
                encryptedText = encrypt(sys.argv[2])
                outputFile = sys.argv[4]
                writeToFile(encryptedText, outputFile)
            except ValueError:
                print("Illegal entry")
            except IndexError:
                print("Illegal entry")

        elif sys.argv[1] == '-d':# decrypting the file to get the plain text
            try:
                key = int(sys.argv[3])
                decryptedText = decrypt(sys.argv[2])
                outputFile = sys.argv[4]
                writeToFile(decryptedText, outputFile)
            except ValueError:
                print("Illegal entry")
            except IndexError:
                print("Illegal entry")

        elif sys.argv[1] == '-c':# cracking the file to get the plain text
            try:
                bruteForce(sys.argv[2])
            except ValueError:
                print("Illegal entry")
            except IndexError:
                print("Illegal entry")
