input = input()

totalLength = len(input)
whiteSpaceCounter = 0
lowercaseCounter = 0
uppercaseCounter = 0
symbolCounter = 0

for e in input:
    asciiCode = ord(e)
    if e == '_':
        whiteSpaceCounter += 1
    elif asciiCode >= 65 and asciiCode <= 90:
        uppercaseCounter += 1
    elif asciiCode >= 97 and asciiCode <= 122:
        lowercaseCounter += 1
    else:
        symbolCounter += 1

print(whiteSpaceCounter/totalLength)
print(lowercaseCounter/totalLength)
print(uppercaseCounter/totalLength)
print(symbolCounter/totalLength)