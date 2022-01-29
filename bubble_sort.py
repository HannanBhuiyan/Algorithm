class Sort:
    @staticmethod
    def bubble_sort(arr):
        size = len(arr) - 1
        for i in range(0, size):
            swap = 0
            for j in range(0, size-i):
                if arr[j] > arr[j+1]:
                    # Swap two numbers
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swap = 1

            if swap == 0:
                break


arr = [33, 44, 2, -1, -5, 77, 200, 150]
Sort.bubble_sort(arr)
for i in range(0, len(arr)):
    print(arr[i])







