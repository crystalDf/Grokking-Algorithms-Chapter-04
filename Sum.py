def sum_digit(arr):

    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_digit(arr[1:])

print(sum_digit([2, 4, 6]))
