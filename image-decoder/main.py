#Image decoder project using XOR encryption

#1.Converting to binary
def to_binary(image_codes):
  binary_image = []
  for row in image_codes:
    binary_row = []
    for pixel in row:
      binary_pixel = bin(pixel)[2:].zfill(8)
      binary_row.append(binary_pixel)
    binary_image.append(binary_row)
  return binary_image

#2. Expand key to match image code
def expand_key(key, length):
    expanded_key = ""
    while len(expanded_key) < length:
        expanded_key += bin(int.from_bytes(key.encode(), 'big'))[2:].zfill(8) 
    return expanded_key[:length]

#3. Xor ecnryption 
def xor_encrypt(image_codes, key):
    binary_image = to_binary(image_codes)
    total_bits = len(image_codes) * len(image_codes[0]) * 8 
    expanded_key = expand_key(key, total_bits)

    encrypted_image = []
    for i in range(len(binary_image)):
        encrypted_row = []
        for j in range(len(binary_image[i])):
            encrypted_pixel = ""
            for k in range(len(binary_image[i][j])):
                encrypted_pixel += str(int(binary_image[i][j][k]) ^ int(expanded_key[i * len(binary_image[i][j]) + k]))
            encrypted_row.append(encrypted_pixel)
        encrypted_image.append(encrypted_row)
    return encrypted_image

image_codes = [
    [123, 234, 123,],
    [210, 230, 234,],
    [111, 000, 234,],
]

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

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
    


# from PIL import Image
# from numpy import array
# image_code = array(Image.open(r"pic.png"))






