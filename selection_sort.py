def selection_sort(A):
    for i in range(0,len(A) -1):
        mixIndex = i
        for j in range(i+1,len(A)):
            if A[j] < A[mixIndex]:
                minIndex = j
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i]

    print(A)


selection_sort([3,2,1,5,4])
