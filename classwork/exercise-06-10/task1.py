# Task1
# f = open("classwork/exercise-06-10/studentdata.txt", "r")

# aline = f.readline()
# while aline:
#     split_data = aline.split()
#     if len(split_data) >= 7:
#         print(aline)
#     aline = f.readline()

# f.close()

# Task2
# f = open("classwork/exercise-06-10/studentdata.txt", "r")
# aline = f.readline()
# while aline:
#     split_data = aline.split()
#     length = len(split_data)
#     total = 0
#     for i in range(1,length):
#         total += int(split_data[i])
#     average_score = total / (length-1)

#     print("Name:", split_data[0], "average: ", average_score)
#     aline = f.readline()

# f.close()

# Task3 
# f = open("classwork/exercise-06-10/studentdata.txt", "r")

# aline = f.readline()
# while aline:
#     split_data = aline.split()
#     length = len(split_data)
#     min = split_data[1]
#     max = split_data[1]
#     for i in range(1,length):
#         if split_data[i] > max:
#             max = split_data[i]
#         if split_data[i] < min:
#             min = split_data[i]
#     print(f"Name: {split_data[0]}, min: {min}, max: {max}")
#     aline = f.readline()

# f.close()