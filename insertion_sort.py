def insertion_sort(A):
    for i in range(1,len(A)):
        for j in range(i-1, -1,-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break

    print(A)

insertion_sort([3,2,1,4])


def straight_insertion_sort(lst):
    for i in range(1, len(lst)):
        save = lst[i]
        j = i
        while j > 0 and lst[j - 1] > save:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = save


