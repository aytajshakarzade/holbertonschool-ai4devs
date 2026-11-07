def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


def display_average(numbers):
    result = calculate_average(numbers)
    print("Average score:", result)


scores = [80, 90, 75, 85]

display_average(scores)

empty_scores = []

display_average(empty_scores)
