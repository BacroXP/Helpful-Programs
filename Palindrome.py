import sys

var = sys.argv[1]
chars = []
isPelindrome = True

small_char = {
    "A": "a",
    "B": "b",
    "C": "c",
    "D": "d",
    "E": "e",
    "F": "f",
    "G": "g",
    "H": "h",
    "I": "i",
    "J": "j",
    "K": "k",
    "L": "l",
    "M": "m",
    "N": "n",
    "O": "o",
    "P": "p",
    "Q": "q",
    "R": "r",
    "S": "s",
    "T": "t",
    "U": "u",
    "V": "v",
    "W": "w",
    "X": "x",
    "Y": "y",
    "Z": "z",
}


for char in var:
    if char != " ":
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            chars.append(small_char[char])
        else:
            chars.append(char)

if "." in str(len(chars) / 2):
    chars.remove(chars[int((len(chars) / 2) - 0.5)])

for i in range(int(len(chars) / 2)):
    if chars[i] != chars[len(chars) - i - 1]:
        isPelindrome = False

if isPelindrome:
    print(True)
else:
    print(False)
