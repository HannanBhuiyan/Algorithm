# Selection sort asc
class Selection:
    @staticmethod
    def selection_sort(arr):
        # Outer loop to iterate over all the arr numbers
        for i in range(0, len(arr)):
            min_ind = i
            # inner loop to find the minimum index
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_ind]:
                   min_ind = j
            # swap two numbers (i, min_ind)
            arr[i], arr[min_ind] = arr[min_ind], arr[i]


arr = [5, 1, 33, 22, 67, 55]
Selection.selection_sort(arr)
print("After Sorting")
for i in range(0, len(arr)):
    print(arr[i])


print("=======================")


# Selection sort dec
class Selection:
    @staticmethod
    def selection_sort(arr):
     for i in range(0, len(arr)):
        min_ind = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[min_ind]:
                min_ind = j
        # swap two numbers (i, min_ind)
        arr[i], arr[min_ind] = arr[min_ind], arr[i]


arr = [5, 1, 33, 22, 67, 55]
Selection.selection_sort(arr)
print("After Sorting ")

for i in range(0, len(arr)):
    print(arr[i])
