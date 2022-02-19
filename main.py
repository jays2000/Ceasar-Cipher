import sys

arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z"]
key = 0


def writeToFile(string):
    file = open("output.txt", "w")
    file.write(string)
    file.close()


def encrypt(line):
    encryptedString = ""
    global key
    key = key % 26
    for i in range(0, len(line)):
        shift = arr.index(line[i]) + key
        if shift >= len(arr):
            shift = shift % 26
        encryptedString = encryptedString + arr[shift]

    writeToFile(encryptedString)


def readFile(file):
    try:
        with open(file) as f:
            line = f.read()
            line = line.lower()
            encrypt(line)

    except FileNotFoundError:
        print("Could not open file")


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Pleas enter correct arguments")
    else:
        if sys.argv[1] == '-e':
            try:
                key = int(sys.argv[3])
                readFile(sys.argv[2])
            except ValueError:
                print("Illegal entry")
