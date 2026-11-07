# Structured Bug Reports

This document records the five bugs investigated and fixed in the Prompting Debug Assistant project.

## Bug Report 1 — Empty List Runtime Error

- **File name:** `bug_snippets/bug1.py`
- **Fixed file:** `bug_fixes/bug1_fixed.py`
- **Bug summary:** The `calculate_average()` function raises a `ZeroDivisionError` when it receives an empty list.
- **Root cause:** The function divides the sum by the length of the list without checking whether the list is empty.
- **AI suggestion:** The AI identified the division-by-zero condition and recommended validating the input before calculating the average.
- **Resolution:**
  - **AI-assisted fix:** Added an empty-list check and raised a descriptive `ValueError`.
  - **Manual edits:** Added a `try/except` block in `display_average()` to handle the exception and display a clear error message.
- **Validation:** Tested both a normal list and an empty list. The normal input produces an average, while the empty input produces a handled error message.
- **Lessons learned:** Always validate input before performing division. Empty collections are important edge cases to test.

## Bug Report 2 — Off-by-One Error in JavaScript Loop

- **File name:** `bug_snippets/bug2.js`
- **Fixed file:** `bug_fixes/bug2_fixed.js`
- **Bug summary:** The `getUserNames()` function attempts to access an array element outside the valid range.
- **Root cause:** The loop condition uses `i <= users.length` instead of `i < users.length`.
- **AI suggestion:** The AI identified the off-by-one error and recommended correcting the loop boundary.
- **Resolution:**
  - **AI-assisted fix:** Changed `i <= users.length` to `i < users.length`.
  - **Manual edits:** Added a `console.assert()` test to verify that all expected user names are returned.
- **Validation:** Confirmed that the function returns `["Aytac", "Leyla", "Nigar"]` in the correct order.
- **Lessons learned:** Always check array boundaries and remember that array indexes start at zero.

## Bug Report 3 — Incorrect Discount Calculation

- **File name:** `bug_snippets/bug3.py`
- **Fixed file:** `bug_fixes/bug3_fixed.py`
- **Bug summary:** The discount function subtracts the discount value directly instead of calculating a percentage.
- **Root cause:** The original formula `price - discount` does not account for percentage-based discounts.
- **AI suggestion:** The AI identified the incorrect formula and recommended calculating the discount amount as a percentage of the original price.
- **Resolution:**
  - **AI-assisted fix:** Replaced the formula with `price - (price * discount / 100)`.
  - **Manual edits:** Added assertions to test different discount percentages.
- **Validation:** Confirmed that a 20% discount on 100 returns 80 and a 10% discount on 200 returns 180.
- **Lessons learned:** Understand the meaning and units of input parameters. Percentage calculations require dividing by 100.

## Bug Report 4 — String Concatenation Instead of Numeric Addition

- **File name:** `bug_snippets/bug4.js`
- **Fixed file:** `bug_fixes/bug4_fixed.js`
- **Bug summary:** The total and average price calculations produce incorrect results because prices are stored as strings.
- **Root cause:** The `productPrices` array contains string values, and the `+` operator can concatenate strings instead of performing numeric addition.
- **AI suggestion:** The AI identified the data-type mismatch and recommended converting each price into a number before performing arithmetic operations.
- **Resolution:**
  - **AI-assisted fix:** Used `Number(prices[i])` inside `calculateTotal()`. Added an empty-array check in `calculateAverage()`.
  - **Manual edits:** Added `console.assert()` checks for the expected total and average.
- **Validation:** Confirmed that the total is 600 and the average is 200 for the sample data.
- **Lessons learned:** Always validate data types before performing mathematical operations. Handle empty collections explicitly.

## Bug Report 5 — Python Syntax Error

- **File name:** `bug_snippets/bug5.py`
- **Fixed file:** `bug_fixes/bug5_fixed.py`
- **Bug summary:** The Python program cannot execute because the `if` statement is missing a colon.
- **Root cause:** The condition `if number > maximum` does not include the required colon.
- **AI suggestion:** The AI identified the syntax error and recommended adding the missing colon.
- **Resolution:**
  - **AI-assisted fix:** Changed the condition to `if number > maximum:`.
  - **Manual edits:** Added assertions to test positive numbers, negative numbers, and an empty list.
- **Validation:** Confirmed that the maximum of `[12, 45, 7, 89, 34]` is 89, the maximum of `[-5, -2, -10]` is -2, and an empty list returns `None`.
- **Lessons learned:** Follow language syntax rules and test both normal and edge-case inputs after fixing errors.

## Overall Summary

The five debugging exercises covered different categories of programming errors:

1. Runtime error caused by division by zero.
2. Off-by-one error in a JavaScript loop.
3. Logical error in percentage calculation.
4. Data-type error involving strings and numeric addition.
5. Python syntax error caused by a missing colon.

AI assistance helped identify root causes and suggest possible solutions. Manual review and testing were also important to ensure that the fixes worked correctly.

This project demonstrates that AI-generated debugging suggestions should always be reviewed, validated, and tested before being accepted.
