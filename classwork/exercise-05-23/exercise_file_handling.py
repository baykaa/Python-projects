# 2 - What does the ‘open’ function do?
# The open() function takes two parameters; filename, and mode.

# 3 - What does the following code do?
# fo = open("dummyFile.txt", "r")
# it opens text file called dummyFile.txt for Read.

fo = open("dummyFile.txt", "w+")
print(type(fo)) # class '_io.TextIOWrapper
print(fo) # io.TextIOWrapper name='dummyFile.txt' mode='w+' encoding='UTF-8'


#5 - What does the close() method do on a file object?
# fo.close()


# fo = open("dummyFile.txt", "w+")
# for i in range(10):
#     fo.write("This is line %d\r\n" % (i+1))