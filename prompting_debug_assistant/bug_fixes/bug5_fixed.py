def find_maximum(numbers):
    if len(numbers) == 0:
        return None

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


values = [12, 45, 7, 89, 34]

result = find_maximum(values)

print("Maximum value:", result)

assert find_maximum([12, 45, 7, 89, 34]) == 89
assert find_maximum([-5, -2, -10]) == -2
assert find_maximum([]) is None

print("All tests passed!")
