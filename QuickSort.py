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

myList = [14, 2, 57, 9, 34]
quickSort(myList, 0, len(myList) - 1)
print(myList)