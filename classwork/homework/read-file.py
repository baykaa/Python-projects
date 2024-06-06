infile = open("classwork/homework/data1.txt", "r")
line = infile.readline()
while line:
    values = line.split()
    print('In', values[0], 'the average temp. was', values[1], '°C and CO2 emmisions were', values[2], 'gigatons.')
    line = infile.readline()

infile.close()




# infile = open("ccdata.txt", "r")
# outfile = open("emissiondata.txt", "w")

# aline = infile.readline()
# outfile.write("Year \tEmmision\n")
# while aline:
#     items = aline.split()
#     dataline = items[0] + '\t' + items[2]
#     outfile.write(dataline + '\n')
#     aline = infile.readline()

# infile.close()
# outfile.close()


