# Selection Sort
def selectionSort(list, n):
    for i in range(n - 1):
        min = i
        for j in range((i + 1), n):
            if list[j] < list[min]:
                min = j
        if min != i:
            list[min], list[i] = list[i], list[min]

myList = [4, 8, 1, 7, 54]
selectionSort(myList, len(myList))
print(myList)