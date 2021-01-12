# Interchange Sort
def interChangeSort(list, n):
    for i in range(n - 1):
        for j in range((i + 1), n):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]

myList = [5, 1, 7, 7, 18]
interChangeSort(myList, len(myList))
print(myList)