# XOR Encryption Algorithm

def binary(num, length=8):
    b = bin(num).lstrip("0b")
    b = "0" *(length-len(b)) + b
    return b
def hexa(num, length=2):
    h = hex(num).lstrip("0x").upper()
    h = "0" *(length-len(h)) + h
    return h

plaintext = input("Enter a message to encrypt:\n")
key="101ComputingKey"
keyLength = len(key)
cipherAscii=""
cipherDen = ""
cipherHex=""
cipherBin=""

for i in range(0, len(plaintext)):
    j = i % keyLength
    
    xor = ord(plaintext[i]) ^ ord(key[j])
    cipherAscii = cipherAscii + chr(xor)
    cipherDen = cipherDen + str(xor) + " "
    cipherHex = cipherHex + hexa(xor) + " "
    cipherBin = cipherBin + binary(xor) + " "

print("\nCipher (Ascii form): \n" + cipherAscii)
print("\nCipher (Denary form): \n" + cipherDen)
print("\nCipher (Hexadecimal form): \n" + cipherHex)
print("\nCipher (Binary form): \n" + cipherBin)
