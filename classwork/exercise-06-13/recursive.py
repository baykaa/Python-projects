# def recursive_sum(nested_num_list):
#     total = 0
#     for element in nested_num_list:
#         if type(element) is list:
#             total += recursive_sum(element)
#         else:
#             total += element

#     return total

# print(recursive_sum([1, 2, [11, 13], 8]))

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))

# num = int(input("Give me a number: "))
# print(f"The factorial of {num} is {factorial(num)}")

#Fibonacci numbers
# import time 

# n = 35
# start_time = time.time()

# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
    
# result = fibonacci(n)

# end_time = time.time()
# execution_time = end_time = start_time

# print("fibonacci({0}) = {1}, ({2} secs)".format(n, result, execution_time))

#MUTUAL RECURSION
# def function_a(n):
#     if n == 0:
#         return
#     print('a')
#     function_b(n - 1)

# def function_b(n):
#     if n == 0:
#         return
#     print('b')
#     function_a(n - 1)

# function_a(5)

#Exercise - 1
# def recursive_min(nested_num_list):
#     min_num = nested_num_list[0]
#     for element in nested_num_list:
#         if type(element) is list:
#             min_num = recursive_min(element)
#         elif element < min_num:
#             min_num = element
#     return min_num

# print(recursive_min([3, 5, 19, [1, 6], 10]))

# Exercise - 2
# def recursive_count(nested_list, target):
#     count = 0
#     for element in nested_list:
#         if type(element) is list:
#             count += recursive_count(element, target)
#         elif element == target:
#             count += 1
#     return count

# nested_list = [1,4,6,2,1,4,5,6,3,2,1,[1,2,3,5,5,2,1,1]]
# target = 1
# result = recursive_count(nested_list, target)
# print(f"The occurence of {target} is: {result}")

# # Exercise - 3
# def recursive_flatten(nested_list):
#     new_list = []
#     for i in nested_list:
#         if type(i) is list:
#             new_list.extend(recursive_flatten(i))
#         else:
#             new_list.append(i)
#     return new_list

# print(recursive_flatten([1, 2, [3, 4], 5]))

# Exercise - 4
import time

n = 200
start_time = time.time()
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    num_0 = 0
    num_1 = 1
    for i in range(2, n+1):
        num_2 = num_0 + num_1
        num_0 = num_1
        num_1 = num_2

    return num_1

result = fibonacci(n)
end_time = time.time()
execution_time = end_time = start_time

print("fibonacci({0}) = {1}, ({2} secs)".format(n, result, execution_time))

# Exercise - 5
# def recursive_sum(n):
#     result = 0
#     for i in range(n):
#         result += i


