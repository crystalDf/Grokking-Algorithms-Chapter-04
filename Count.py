def count_digit(arr):

    if len(arr) == 0:
        return 0
    else:
        return 1 + count_digit(arr[1:])

print(count_digit([2, 4, 6]))
