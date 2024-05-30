# 1. Take user message(input) & shift amount
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# 2. We need alphabets (list)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Shift each letter to the right (function)
def caesar(start_text, shift_amount):
  end_text = ""
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char) #Ex: a-0
      
      new_position = position + shift_amount #Ex: 0 + 3 = 4 (d)
      end_text += alphabet[new_position]
    else:
      end_text += char
  return end_text

# 4. Print the result to the user
result = caesar(start_text=text, shift_amount=shift)
print("Here's the encoded result: ", result)