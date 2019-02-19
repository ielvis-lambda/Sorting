# helper function
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range(0, elements):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# recursive sorting function
def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0: int(len(arr) / 2)])
        right = merge_sort(arr[int(len(arr) / 2):])
        arr = merge(left, right)   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


arr = [2, 5, 9, 7, 4, 1, 3, 8, 6]

# TO-DO: implement the Quick Sort function below USING RECURSION


def quick_sort(arr, high, low):
    # 1. Select a pivot. Often times this is the first or last element in a set. It can also be the middle.
    # pivot = arr[len(arr)-1]
    pivot = high
    pivotIndex = len(arr)-1
    print(f"I'm the pivot: {pivot}")
    print(f"I'm the pivotIndex: {pivotIndex}")
    # 2. Move all elements smaller than the pivot to the left.
    # Find these elements.
    smaller = []
    for i in range(0, pivotIndex):
        if arr[i] < pivot:
            # Move these elements
            smaller.append(arr[i])
    print(f"I'm the smaller: {smaller}")
    # 3. Move all elements greater than the pivot to the right.
    bigger = [pivot]
    for j in range(0, pivotIndex):
        # print(arr[j])
        if arr[j] > pivot:
            # Move these elements
            bigger.append(arr[j])
    print(f"I'm the bigger: {bigger}")

    arr = smaller + bigger
    # 4. While LHS and RHS are greater than 1, repeat steps 1-3 on each side.
    # arr = smaller + bigger
    print(f"I'm the len of smaller: {len(smaller)}")
    print(f"I'm the len of bigger: {len(bigger)}")

    print(f"I'm the current array: {arr}")

    if len(smaller) > 1 and len(bigger) > 1:
        arr = quick_sort(smaller, smaller[len(smaller)-1], 0) + quick_sort(bigger, bigger[len(bigger)-1], 0)

    # elif len(smaller) == 1 and len(bigger) == 1:
    #     pass

    print(f"I'm the final array: {arr}")
    return (arr)

print(quick_sort(arr, arr[len(arr)-1], 0))



# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
