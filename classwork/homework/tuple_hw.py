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