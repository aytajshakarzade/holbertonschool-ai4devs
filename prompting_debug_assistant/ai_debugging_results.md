# AI-Assisted Debugging Results

This document contains the results of using AI to identify and explain bugs in the provided code snippets.

## Bug 1 — Runtime Error

### Original File
`bug_snippets/bug1.py`

### AI Debugging Prompt
Analyze the following Python code. Identify the bug, explain why it occurs, describe how to reproduce it, and provide a corrected version. Preserve the original functionality and explain your changes.

### AI Response

**Identified Bug:** ZeroDivisionError.

**Root Cause:** The function divides the sum of the numbers by the length of the list. When the list is empty, its length is zero, causing a division-by-zero error.

**How to Reproduce:** Call `display_average([])` or run the original file, which passes an empty list to the function.

**Suggested Fix:** Check whether the list is empty before performing the division. Raise a clear ValueError if no numbers are provided.

### Corrected Code

```python
def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list.")

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
