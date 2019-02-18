# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        print(f"LOOP {i}")
        print(f"{arr}")
        cur_index = i
        smallest_index = cur_index
        # TO-DO: Separate the first element from the rest of the array. Think about it as a sorted list of one element.
        for j in range(i, len(arr)):
                                                                        # from the i'th position to the end of the array if j is smaller than the current value then j is the current smallest index
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        print(f"SMALLEST ELEMENT: {arr[smallest_index]}")

        # TO-DO: swap
        # Swap that with the current element
        # arr[i], arr[smallest_index] = arr[smallest_index], arr[i}
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr


# try it out
# my_arr = [2, 5, 9, 7, 4, 1, 3, 8, 6]
# print(my_arr)
# arr = selection_sort(my_arr)
# print(my_arr)


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):

    # Algorithm
    # Separate the first element from the rest of the array. Think about it as a sorted list of one element.
    # For all other indices, beginning with [1]:
    # a. Copy the item at that index into a temp variable
    for i in range(1, len(arr)):
        print(f"LOOP {i}")
        print(f"{arr}")
        temp = arr[i]
    # b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted
        j = i
        while j > 0 and temp < arr[j-1]:
            # Shift items over to the right as you iterate
            # c. When the correct index is found, copy temp into this position
        	arr[j] = arr[j - 1]
        j -= 1
        arr[j] = temp
    return arr


# try it out
arr = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print(arr)
arr = insertion_sort(arr)


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
