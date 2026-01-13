def remove_even(numbers):
    result = []   # new list to store only odd numbers

    for n in numbers:
        if n % 2 != 0:
            result.append(n)

    return result
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_even(nums))