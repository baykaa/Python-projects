import numpy as np
from PIL import Image

def xor_encrypt(image_path, password):
    img = Image.open(image_path)
    img_array = np.array(img)
    
    key = np.frombuffer(password.encode(), dtype=np.uint8)
    key = np.resize(key, img_array.shape)
    
    encrypted_img_array = np.bitwise_xor(img_array, key)
    encrypted_img = Image.fromarray(encrypted_img_array)
    
    encrypted_img.save('encrypted_image.png')
