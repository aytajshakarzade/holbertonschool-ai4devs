def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

scores = [80, 90, 75, 85]

print("Average score:", calculate_average(scores))
