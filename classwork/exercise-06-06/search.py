import time
import random

list1 = list(range(1000000))

def linear_search(list1, item):
    for i in range(len(list1)):
        if list1[i] == item:
            return i

def binary_search(list1, item):
    low = 0
    high = len(list1) - 1
    while low <= high:
        mid = (low + high) // 2
        if list1[mid] == item:
            return mid
        elif list1[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

for i in range(6):
    item = random.choice(list1)
    print("Random number for search: ", item)
    time1 = time.time()
    result = linear_search(list1, item)
    time2 = time.time()
    t1 = time2 - time1
    print("The execution time for linear search: ", t1)

    time3 = time.time()
    result = binary_search(list1, item)
    time4 = time.time()
    t2 = time4 - time3
    print("The execution time for binary search: ", t2)
    print("Time  difference: ", t1 - t2, "\n")


