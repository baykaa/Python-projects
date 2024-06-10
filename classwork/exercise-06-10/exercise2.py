infile = open("classwork/exercise-06-10/studentdata.txt", "r")
outfile = open("outfile.txt", "w")

aline = infile.readline()
outfile.write("Name \tScore\n")
while aline:
    items = aline.split()
    dataline = items[0] + '\t' + items[1]
    outfile.write(dataline + '\n')
    aline = infile.readline()

infile.close()
outfile.close()

outfile = open("outfile.txt", "r")
print(outfile.read())