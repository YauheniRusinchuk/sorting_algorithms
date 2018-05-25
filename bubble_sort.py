def bubble_sort(A):
    for i in range(0, len(A)-1):
        for j in range(0,len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

    return A


result = bubble_sort([3,4,1,2,3,5,7])
print(result)
