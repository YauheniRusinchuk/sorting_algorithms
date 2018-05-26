def merge_sort(A):
	merge_sort2(A, 0, len(A)-1)

def merge_sort2(A, first, last):
	if last-first < threshold and first < last:
		quick_selection(A, first, last)
	elif first < last:
		middle = (first + last)//2
		merge_sort2(A, first, middle)
		merge_sort2(A, middle+1, last)
		merge(A, first, middle, last)

def merge(A, first, middle, last):
	L = A[first:middle]
	R = A[middle:last+1]
	L.append(999999999)
	R.append(999999999)
	i = j = 0

	for k in range (first, last+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1

			
			
			
			
			
def merge(left,right):
	result = []
	i,j = 0, 0
	while i<len(left) and j< len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1

	result += left[i:]
	result += right[j:]
	return result


def mergesort(lst):
	if(len(lst) <= 1):
		return lst
	mid = int(len(lst)/2)
	left = mergesort(lst[:mid])
	right = mergesort(lst[mid:])
	return merge(left,right)


arr = [1,2,-1,0,9,65,7,3,4,1,2]
print(mergesort(arr))
			
			
