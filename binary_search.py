
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

// =====================  oop ========================
    
class Binary:
    def Binary_search(self, arr, item):
        self.left = 0
        self.right = len(arr) - 1
        while self.left <= self.right:
            middle = ( self.left + self.right) // 2
            if arr[middle] == item:
                print('Item found at index ', middle)
                exit()
            elif arr[middle] < item:
                self.left = middle + 1
            else:
                self.right = middle - 1
        return -1

obj = Binary()
arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 333, 456]
item = 55
index = obj.Binary_search(arr, item)
if index == -1:
    print("Item not found !")
    exit()
