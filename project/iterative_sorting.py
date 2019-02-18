# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        print(f"LOOP {i}")
        print(f"{arr}")
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
			#from the i'th position to the end of the array if j is smaller than the current value then j is the current smallest index
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        print(f"SMALLEST ELEMENT: {arr[smallest_index]}")

        # TO-DO: swap
        # Swap that with the current element
        # arr[i], arr[smallest_inex] = arr[smmallest_index], arr[i}
        temp = arr[i]
        arr[i] = arr[smallest_index
        arr[smallest_index] = temp
    return arr


# try it out
my_arr = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print(my_arr)
arr = selection_sort(my_arr)
print(my_arr)


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
