def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")

    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


def display_average(numbers):
    try:
        result = calculate_average(numbers)
        print("Average score:", result)
    except ValueError as error:
        print("Error:", error)


scores = [80, 90, 75, 85]
display_average(scores)

empty_scores = []
display_average(empty_scores)
