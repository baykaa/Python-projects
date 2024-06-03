#Exercise 1:

# print(list(range(10, 0, -2)))
# #rule: start stop steps
# if start > stop, stop must be < start, steps < 0
# if start < stop , stop must be > start, steps > 0 

#Exercise 4:
# this = ["I", "am", "not", "a", "crook"]
# that = ["I", "am", "not", "a", "crook"]
# print("Test 1: {0}".format(this is that)) #false
#two different object with different values
# that = this
#assigning same value to other variable
# print("Test 2: {0}".format(this is that)) #true

#Exercise 6:
# def scalar_mult(number, list):
#     new_list = []
#     for i in list:
#         i = i * number
#         new_list.append(i)
#     return new_list    
    
# print(scalar_mult(5, [1, 2]))
# print(scalar_mult(3, [1, 0, -1]))
# print(scalar_mult(7, [3, 0, 5, 11, 2]))

# print(scalar_mult(5, [1, 2]) == [5, 10])
# print(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
# print(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
