def binary_search(arr, item):

    if len(arr) == 0:
        return None

    mid = len(arr) // 2
    guess = arr[mid]

    if guess == item:
        return guess
    if guess > item and mid > 0:
        return binary_search(arr[:mid], item)
    elif guess < item and mid < len(arr) - 1:
        return binary_search(arr[(mid + 1):], item)

    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
