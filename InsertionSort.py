# Insertion Sort
def insertionSort(list, n):
    for i in range(1, n):
        x = list[i]
        pos = i
        while pos > 0 and x < list[pos - 1]:
            list[pos] = list[pos - 1]
            pos -= 1
        list[pos] = x

myList = [65, 1, 87, 7, 18]
insertionSort(myList, len(myList))
print(myList)