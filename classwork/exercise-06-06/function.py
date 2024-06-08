# def pick(b: int, a: int = 5) -> int:
#     return print(a + b)

# pick(1,1)

# pick(1)


list1 = [1,2,0]
for i in range(len(list1)):
    if list1[i] == 0:
        break
    print("The Squared value of", i, "is", list1[i]*list1[i])
