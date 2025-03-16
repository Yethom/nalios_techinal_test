def my_sum(arr: []) -> int:
    total = 0
    for n in arr:
        total += n
    return total


# bonus
def my_sum_recursive(arr: []) -> int:
    return arr[0] + my_sum_recursive(arr[1:]) if arr else 0


arr_test = [2, 4, 8, 9]  # -> 23
print(my_sum(arr_test))
print(my_sum_recursive(arr_test))
