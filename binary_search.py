
def binary_search(arr, item):
    right = len(arr) - 1
    left = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == item:
            print("Item found at index ", mid)
            exit()
        elif arr[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    if left > right:
        return -1


arr = [1, 2, 3, 4, 6, 8, 10, 15, 16, 20, 100]
item = 3

index = binary_search(arr, item)
if index == -1:
    print("Item not found !")
