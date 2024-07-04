student_data = open("classwork/exercise-06-10/studentdata.txt", "r")
line_lists = student_data.readline()

while line_lists:
    values = line_lists.split()
    print("Name:", values[0], ", Score 1:", values[1] )
    line_lists = student_data.readline()
# print(line_lists[0:10])

# whole = student_data.read()
# print(whole[:110])

# for line in student_data:
#     values = line.split()
#     print("Name", values[0], "score", values[1])

student_data.close()

newfile = open("new.txt", "a")
# aline = newfile.readline()
for i in range(10):
    newfile.write(f"This is the {i} line \n ")

newfile.close()
newfile = open("new.txt", "r")
print(newfile.read())

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
