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


# Tuple HOMEWORK
# Exercise-1:
def len_tup(tuple):
    return len(tuple)

a = ("bob", 2034, "231")
print(len_tup(a))

# Exercise - 2: Write a Python program to find repeated items in a tuple.
def repeated_items(tuple):
    seen = []
    repeated = []
    
    for item in tuple:
        if item in seen:
            repeated.append(item)
        else:
            seen.append(item)
    return list(repeated)

b = (1, 2, 3, 2, 4, 5, 3, 6, 1)
print(repeated_items(b))

# Exercise 3: Write a Python program to reverse a tuple..Input : (100, 200, 300) , Output : (300, 200, 100)
def reverse_tup(tup):
    tup_to_list = list(tup)
    tup_to_list.reverse()
    return tuple(tup_to_list)

print(reverse_tup((100, 200, 300)))

# Exercise 4: Write a Python program to print a tuple with string formatting. 
# Sample tuple : (100, 200, 300) Output : This is a tuple (100, 200, 300)
def tup_to_string(tup):
    return f"This is a tuple {tup}"

print(tup_to_string((100, 200, 300)))
