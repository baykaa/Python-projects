# Task 1
# def number_lines(input_file, output_file):
#     with open(input_file, "r") as f, open(output_file, "w") as output:
#         line_number = 1
#         aline = f.readline()
#         while aline:
#             formatted_line_number = f"{line_number:04d}"
#             output_line = f"{formatted_line_number} {aline}"
#             output.write(output_line)
#             line_number += 1
#             aline = f.readline()

# input_file = "classwork/exercise-06-10/test-data.txt"
# output_file = "outputfile.txt"

# number_lines(input_file, output_file)

# with open(output_file, "r") as output:
#     print(output.read())


# Task 2: Remove line numbers from the file
# def remove_line_numbers(input_file, output_file):
#     with open(input_file, "r") as f, open(output_file, "w") as output:
#         aline = f.readline()
#         while aline:
#             output_line = aline[5:]
#             output.write(output_line)
#             aline = f.readline()

# numbered_file = "outputfile.txt"
# output_file_no_numbers = "outputfile_no_numbers.txt"

# remove_line_numbers(numbered_file, output_file_no_numbers)

# with open(output_file_no_numbers, "r") as output:
#     print(output.read())