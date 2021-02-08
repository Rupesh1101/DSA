# Find digits in array whose sum is equal to the given number...

def pair_sum(arr, k):
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for val in arr:
        target = k - val
        if target not in seen:
            seen.add(val)
        else:
            output.add((min(val, target), (max(val, target))))

    # return len(output)
    print('\n'.join(map(str, list(output))))


pair_sum([1, 3, 2, 2], 4)
