# Image encoder project using XOR encryption

# 1.Converting to binary
from PIL import Image
from numpy import array
import numpy as np

def to_binary(image_codes):
    # Convert each pixel to binary representation
    binary_image = np.unpackbits(image_codes, axis=-1)
    # Reshape to match original shape
    return binary_image.reshape(image_codes.shape[0], image_codes.shape[1], -1)

# 2. Expand key to match image code
def expand_key(key, length):
    expanded_key = ""
    while len(expanded_key) < length:
        expanded_key += bin(int.from_bytes(key.encode(), 'big'))[2:].zfill(8)
    return expanded_key[:length]

# 3. Xor ecnryption
def xor_encrypt(image_codes, key):
    binary_image = to_binary(image_codes)
    total_bits = image_codes.size * 8 
    expanded_key = expand_key(key, total_bits)

    encrypted_image = []
    for i in range(len(binary_image)):
        encrypted_row = []
        for j in range(len(binary_image[i])):
            encrypted_pixel = ""
            for k in range(len(binary_image[i][j])):
                # Calculate the index for the expanded key based on the pixel position
                key_index = (i * len(binary_image[i][j]) * 8) + (j * 8) + k
                encrypted_pixel += str(int(binary_image[i][j][k]) ^ int(expanded_key[key_index]))
            # Ensure that encrypted_pixel is a binary string of length 8
            encrypted_pixel = encrypted_pixel.zfill(8)[:8]
            encrypted_row.append(encrypted_pixel)
        encrypted_image.append(encrypted_row)
    return encrypted_image

image = Image.open("pic.png")
image_codes = np.array(image)

should_end = False
while not should_end:

    print("Image codes to encrypt:")
    for row in image_codes:
        print(row)
    print()

    key = input("Input key: ")
    print()

    encrypted_image = xor_encrypt(image_codes, key)

    print("Encrypted Image:")

    for row in encrypted_image:
        print(row)
    print()

    encrypted_image_array = array(encrypted_image, dtype='uint8')
    encrypted_image_array = Image.fromarray(encrypted_image_array)
    encrypted_image_array.save("encrypted_image.png")

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
