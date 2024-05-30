# Practice assignment - Module Homework
import analysis as cal

user_input = input("Input array elements(seperate by comma): ").split(",")
def to_int_array(input):
    result = []
    for i in input:
        result.append(int(i))
    return result

user_input = to_int_array(user_input)
print(len(user_input))


print("Sum:", cal.Arraysum(user_input))
print("Mean of array:", cal.Arraymean(user_input))
print("Min & Max:", cal.Arraymax(user_input))