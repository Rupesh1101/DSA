# Find the missing number from given two arrays....
# method-1:-
import collections


def finder(arr1, arr2):
    count = collections.defaultdict(int)

    for i in arr2:
        count[i] += 1

    for i in arr1:
        if count[i] == 0:
            print(i, 'is the missing number.')
        else:
            count[i] -= 1


# finder([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 6])
# finder([5, 5, 7, 7], [5, 7, 7])

# method-2:-


def finder2(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

        return arr1[-1]


print(finder2([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 6]))
