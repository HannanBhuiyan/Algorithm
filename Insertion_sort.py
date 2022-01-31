# Inserting sort asc
class Insertion:
    @staticmethod
    def insertion_sort_asc(arr):
        for i in range(1, len(arr)):
            value = arr[i]
            hole = i
            while hole > 0 and arr[hole - 1] > value:
                arr[hole] = arr[hole - 1]
                hole = hole - 1

            arr[hole] = value
        for i in range(0, len(arr)):
            print(arr[i])


arr = [39, 2, 3, 7, 66, 33, 22]
Insertion.insertion_sort_asc(arr)


print("=========================")


class Insertion:
    @staticmethod
    def insertion_sort_desc(arr):
        for i in range(1, len(arr)):
            value = arr[i]
            hole = i
            while hole > 0 and arr[hole - 1] < value:
                arr[hole] = arr[hole - 1]
                hole = hole - 1

            arr[hole] = value
        for i in range(0, len(arr)):
            print(arr[i])


arr = [39, 2, 3, 7, 66, 33, 22]
Insertion.insertion_sort_desc(arr)
















