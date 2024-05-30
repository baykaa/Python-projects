#Array Homework
# Create 1 dim array with values given by the user using input() and split()
import numpy as np
user_input = input("Input(numbers with ,): ").split(",")
#Convert string to number in array
# Method 1: list items to int
# converted_input = []
# for i in user_input:
#     str_input.append(int(i))
# input_array_int = np.array(converted_input)

# Method 2: Turn array items to int
user_input_array = np.array(user_input)
input_array_int = user_input_array.astype('i')
print(input_array_int)

#A) Calculate the sum of all elements in array
print(np.sum(input_array_int))

#B) Calculate the mean of array
print(np.mean(input_array_int))

#C) Find the max and min values in the array
print("Max:", np.amax(input_array_int))
print("Min:", np.amin(input_array_int))
