# Interchange Sort
def interChangeSort(list, n):
    for i in range(n - 1):
        for j in range((i + 1), n):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]

#  Bubble Sort
def bubbleSort(list, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

# Insertion Sort
def insertionSort(list, n):
    for i in range(1, n):
        x = list[i]
        pos = i
        while pos > 0 and x < list[pos - 1]:
            list[pos] = list[pos - 1]
            pos -= 1
        list[pos] = x

# Selection Sort
def selectionSort(list, n):
    for i in range(n - 1):
        min = i
        for j in range((i + 1), n):
            if list[j] < list[min]:
                min = j
        if min != i:
            list[min], list[i] = list[i], list[min]

# Quick Sort
def partition(list, low, high):
    pivot = list[high]
    left = low
    right = high - 1
    while True:
        while left <= right and list[left] < pivot:
            left += 1
        while right>= left and list[right] > pivot:
            right -= 1
        if left >= right:
            break
        list[left], list[right] = list[right], list[left]
        left += 1
        right -= 1
    list[left], list[high] = list[high], list[left]
    return left

def quickSort(list, low, high):
    if low < high:
        pi = partition(list, low, high)
        quickSort(list, low, pi -1)
        quickSort(list, pi + 1, high)

# Merge sort
# def merge(list, l, m, r):
#     n1 = m - l + 1
#     n2 = r - m
#     L[n1] = []
#     R[n2] = []
#     for i in range(n1):
#         L[i] = list[l + i]

#     for j in range(n2):
#         R[j] = list[m + 1 + j]

#     i = 0
#     j = 0
#     k = l
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             list[k] = L[i]
#             i += 1
#         else:
#             list[k] = R[j]
#             j += 1
#         k += 1
    
#     while i < n1:
#         list[k] = L[i]
#         i += 1
#         k += 1

#     while j < n2:
#         list[k] = R[j]
#         j += 1
#         k += 1

# def mergeSort(list, l, r):
#     if l < r:
#         m = l + (r - l) / 2
#         mergeSort(list, l, m)
#         mergeSort(list, m + 1, r)
#         merge(list, l, m, r)


myList = [4, 8, 1, 7, 54]
insertionSort(myList, len(myList))
print(myList)
