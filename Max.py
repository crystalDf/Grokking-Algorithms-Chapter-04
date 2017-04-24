def find_max(arr):

    if len(arr) == 0:
        return 0
    else:
        return max(arr[0], find_max(arr[1:]))

print(find_max([2, 4, 6]))
