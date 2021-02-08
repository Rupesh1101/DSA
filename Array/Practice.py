def reverseInGroups(arr, N, K):
    # code here
    list1 = arr[0:K]
    list2 = arr[K:]
    print(list1[::-1], list2[::-1])
    return list1[::-1] + list2[::-1]



print(reverseInGroups([1,2,3,4,5],5, 77))
