def get_last_items(items, n):
    if n <= 0:
        return []

    return items[-n:]


numbers = [10, 20, 30, 40, 50]

assert get_last_items(numbers, 3) == [30, 40, 50]
assert get_last_items(numbers, 1) == [50]
assert get_last_items(numbers, 0) == []
assert get_last_items(numbers, 10) == numbers
assert get_last_items(numbers, -2) == []

print("All bug1 tests passed!")
