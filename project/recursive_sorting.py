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
arr2 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr3 = []
arr4 = [0, 1, 2, 3, 4, 5]

# TO-DO: implement the Quick Sort function below USING RECURSION


def quick_sort(arr, low, high):
	# 1. Select a pivot. Often times this is the first or last element in a set. It can also be the middle.
	if high == 0:
		return arr
	elif high-low <= 0:
		return arr

	pivot = arr[high]
	pivotIndex = len(arr)-1
	# 2. Move all elements smaller than the pivot to the left.
	# Find these elements.
	smaller = []
	for i in range(0, pivotIndex):
		if arr[i] < pivot:
			# Move these elements
			smaller.append(arr[i])
	# print(f"I'm the smaller: {smaller}")
	# 3. Move all elements greater than the pivot to the right.
	bigger = []
	for j in range(0, pivotIndex):
		if arr[j] > pivot:
			# Move these elements
			bigger.append(arr[j])
	# 4. While LHS and RHS are greater than 1, repeat steps 1-3 on each side.
	arr = smaller + [pivot] + bigger
	if len(bigger) == 0 and len(smaller) > 1:
		smaller = quick_sort(smaller, 0, len(smaller)-1)
		arr = smaller + [pivot] + bigger


	elif len(smaller) > 1 or len(bigger) > 1:
		smaller = quick_sort(smaller, 0, len(smaller)-1)
		bigger = quick_sort(bigger, 0, len(bigger)-1)
		arr = smaller + [pivot] + bigger
	return (arr)


# print(quick_sort(arr, 0, len(arr)-1))
print(quick_sort(arr2, 0, len(arr2)-1))
# print(quick_sort(arr3, 0, len(arr3)-1))
# print(quick_sort(arr4, 0,
#  len(arr4)-1))



# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

	return arr
