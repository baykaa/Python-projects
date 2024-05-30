def Arraysum(arr):
    result = 0
    for i in arr:
        result += i
    return result

def Arraymean(arr):
    total_count = len(arr)
    return Arraysum(arr) / total_count

def Arraymax(arr):
    max = arr[0]
    min = arr[0]
    for i in arr:
        if i >= max:
            max = i
        if i <= min:
            min = i
    return (min, max)

# print(Arraymax([-1,2,3,4,6,7,-1234, 20]))
