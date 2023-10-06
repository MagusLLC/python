from collections import UserList
import timeit
list = [5, 1, 4, 2, 8, 34, 3, 90]

def bubbleSort(userList):
    # startTime = time.time()
    for i in range(len(list)//2 + 1):
        for j in range(len(list)-1):
            if(list[j] > list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]
    # print("Time taken to sort this list is", time.time()-startTime, "seconds")
    return userList

sortedList = bubbleSort(list)
print(timeit.timeit(str(sortedList)))
print(bubbleSort(list))