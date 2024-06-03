# # Exercise 1
# def add_integers(a, b):
#     try: 
#         b = int(b)
#         result =  a + b
#     except TypeError:
#         print("Type is wrong!")
#     except ValueError:
#         print("Value error!")
#     else:
#         print("Result:", result) 
#     finally:
#         print("Successful")
    
# a = input("A: ")
# b = input("B: ")

# add_integers(a,b)


# Exercise 2:
# def convert_to_int(s):
#     try:
#         s = int(s)
#     except ValueError:
#         print("THERE IS VALUE ERROR!")
#     else:
#         print(s)
#     finally:
#         print("Successful!")

# s = input("Input: ")
# convert_to_int(s)


# Exercise 3:
# class Error(Exception):
#     pass
 
# class NegativeNumberError(Error):
#     pass

# def square_root(x):
#     try: 
#         x = int(x)
#         if(x < 0):
#             raise NegativeNumberError
#         else:
#             result = x ** 0.5
#     except NegativeNumberError:
#         print("Bruh POSITIVE NUMBER!")
#     except TypeError:
#         print("Type error!")
#     except ValueError:
#         print("Value error!")
#     else:
#         print(result)
#     finally:
#         print("Successful!")

# user_input = input("Input int: ")
# square_root(user_input)

