#Dictionary
# dic = {
#     1 : "Python",
#     2 : "Java",
#     3 : "PHP",
#     4 : "C",
# }

# print(dic[1])
# print(dic)

# en2fr = {
#     "Eng" : "Fr",
#     "Hello" : "Salut",
#     "Good" : "Bien",
#     "Life" : "La vie",
#     "Kids" : "Les enfants",
# }

# print(en2fr["Hello"])
# print(en2fr)

# D1 = {
#     "D" : 3.99,
#     "A" : 0.99,
#     "C" : 2.99,
#     "B" : 1.99,
# }

# D1["D"] = 23
# D1.update({'D': 245})
# D1["key"] = "valueeeeee"
# del D1["A"]
# print(D1)
# a = D1.pop('key')
# print(D1)

# for key, value in D1.items():
#     print(f"Key: {key}, Value: {value}")

# print("\n")
# for key in D1:
#     value = D1[key]
#     print(f"Key: {key}, Value: {value}")
# print("\n")

# for key in D1.keys():
#     print(f"Key: {key}")
# print("\n")
# for value in D1.values():
#     print(f"Value: {value}")

# sorted(D1.items())

# # # import math

# # # result = math.sqrt(25)
# # # print(result)  # Output: 5.0


#MODULE LESSON
# # from math import sqrt  # Importing a specific object
# # from math import *  # Importing the entire module (not recommended)
# # import math as m  # Importing with an alias

# # m.sqrt(25)

# # import random as r
# from random import *
# # Generate a random number between 1 and 10
# random_number = randint(1, 10)
# print(random_number)

# Example: The time module
# import time

# def domysum(xs):
#     sum = 0
#     for v in xs:
#         sum += v
#     return sum

# sz = 10000000        # Lets have 10 million elements in the list
# testdata = range(sz)

# t0 = time.time()
# my_result = domysum(testdata)
# t1 = time.time()
# print("my_result    = {0} (time taken = {1:.4f} seconds)".format(my_result, t1-t0))

# t2 = time.time()
# their_result = sum(testdata)
# t3 = time.time()
# print("built-in result = {0} (time taken = {1:.4f} seconds)".format(their_result, t3-t2))



# Practice assignment - Module Homework
import analysis as cal

user_input = input("Input array elements(seperate by comma): ").split(",")
def to_int_array(input):
    result = []
    for i in input:
        result.append(int(i))
    return result

user_input = to_int_array(user_input)
print(len(user_input))


print("Sum:", cal.Arraysum(user_input))
print("Mean of array:", cal.Arraymean(user_input))
print("Min & Max:", cal.Arraymax(user_input))





