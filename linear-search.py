# Linear search algorithm

# Linear Search Function
def linear_search(arr, item):
    for i in range(0, len(arr)):
        if arr[i] == item:
            return i
    return -1


# Main Code
arr = [2, 7, 11, 19, 34, 53, 3, 45, 72, 75]
item = 34

index = linear_search(arr, item)
if index == -1:
    print("Item not found")
else:
    print("Item found at index ", index)



