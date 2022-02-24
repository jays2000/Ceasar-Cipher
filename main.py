#HOW TO RUN
#
#Change to whatever directory you have the files saved in. (cd 'directoryname' in cmd on Windows. IDK about you Mac users)
#
#Use the commands below. Only encrypt and decrypt work for now
#
#
#python main.py –e <file to be encrypted> key <output file>
#
#python main.py –d <file to be decrypted> key <output file>
#
#python main.py –c <file to crack>

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
    line = readFile(line)
    global key
    key = key % 26
    for i in range(0, len(line)):
        shift = arr.index(line[i]) + key
        if shift >= len(arr):
            shift = shift % 26
        encryptedString = encryptedString + arr[shift]
    return encryptedString

def decrypt(line):
    decryptedString = ""
    line = readFile(line)
    global key
    key = key % 26
    for i in range(0, len(line)):
        shift = arr.index(line[i]) - key
        if shift <= len(arr):
            shift = shift % 26
        decryptedString = decryptedString + arr[shift]
    return decryptedString


def readFile(file):
    try:
        with open(file) as f:
            line = f.read()
            line = line.lower()
            return line

    except FileNotFoundError:
        print("Could not open file")


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Please enter correct arguments")
    else:
        outputFile = sys.argv[4]
        if sys.argv[1] == '-e':
            try:
                key = int(sys.argv[3])
                encryptedText = encrypt(sys.argv[2])
                writeToFile(encryptedText, outputFile)
            except ValueError:
                print("Illegal entry")

        if sys.argv[1] == '-d':
            try:
                key = int(sys.argv[3])
                decryptedText = decrypt(sys.argv[2])
                writeToFile(decryptedText, outputFile)
            except ValueError:
                print("Illegal entry")



# Things I added or changed:
# Decrypt function and the option in main.
# encrypt and decrypt functions both now have the call for the readFile function
#     within them. Before it was called from main then the readFile function would call encrypt



#
# import sys
#
# arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
#        "w", "x", "y", "z"]
# key = 0
#
#
# def writeToFile(string):
#     file = open("output.txt", "w")
#     file.write(string)
#     file.close()
#
#
# def encrypt(line):
#     encryptedString = ""
#     global key
#     key = key % 26
#     for i in range(0, len(line)):
#         shift = arr.index(line[i]) + key
#         if shift >= len(arr):
#             shift = shift % 26
#         encryptedString = encryptedString + arr[shift]
#
#     writeToFile(encryptedString)
#
#
# def readFile(file):
#     try:
#         with open(file) as f:
#             line = f.read()
#             line = line.lower()
#             encrypt(line)
#
#     except FileNotFoundError:
#         print("Could not open file")
#
#
# if __name__ == '__main__':
#     if len(sys.argv) != 5:
#         print("Pleas enter correct arguments")
#     else:
#         if sys.argv[1] == '-e':
#             try:
#                 key = int(sys.argv[3])
#                 readFile(sys.argv[2])
#             except ValueError:
#                 print("Illegal entry")
