# # Exercise 1
def add_integers(a, b):
    try: 
        b = int(b)
        # a = int(a)
        result =  a + b
    except TypeError:
        print("Type is wrong!")
    except ValueError:
        print("Value error!")
    else:
        return result
    finally:
        print("Successful")
    
a = input("A: ")
b = input("B: ")

print(add_integers(a,b))


# Exercise 2:
# def convert_to_int(s):
#     try:
#         s = int(s)
#     except ValueError:
#         print("THERE IS VALUE ERROR!")
#     else:
#         print(s)
#     finally:
#         print("Function executed successful!!")

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
#         print("Function executed successful!")

# user_input = input("Input int: ")
# square_root(user_input)



#EXCEPTION
#Exercise - 1
# def readposint():
#     while True:
#         try:
#             num = input("Please enter a positive integer: ")
#             if not num:
#                 print("No input provided. Please try again.")
#                 continue
#             num = int(num)
#             if num > 0:
#                 print("It is psotive number!")
#                 break
#             else:
#                 print("The number is not positive. Please try again.")
#         except ValueError:
#             print("Invalid input. Please enter a valid positive integer.")

# readposint()
