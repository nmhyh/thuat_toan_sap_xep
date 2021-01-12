#  Bubble Sort
def bubbleSort(list, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

myList = [4, 8, 1, 7, 54]
bubbleSort(myList, len(myList))
print(myList)