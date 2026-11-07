# Bug Descriptions

This document describes the five intentionally buggy code snippets created for the Prompting Debug Assistant project.

## Bug 1 — Empty List Runtime Error

- **File:** `bug1.py`
- **Bug Type:** Runtime Error
- **Intended Behavior:** The function should calculate and return the average of a list of numbers.
- **Problem:** The function divides the total by the length of the list without checking whether the list is empty.
- **Expected Error:** `ZeroDivisionError`
- **How to Reproduce:** Call `calculate_average([])`.

## Bug 2 — Off-by-One Error

- **File:** `bug2.js`
- **Bug Type:** Off-by-One / Loop Error
- **Intended Behavior:** The function should return the names of all users in an array.
- **Problem:** The loop condition uses `i <= users.length` instead of `i < users.length`. This causes the loop to access an array element outside its valid index range.
- **Expected Error:** `TypeError`
- **How to Reproduce:** Run the function with a non-empty users array.

## Bug 3 — Incorrect Discount Calculation

- **File:** `bug3.py`
- **Bug Type:** Logical Error
- **Intended Behavior:** The function should calculate the final product price after applying a percentage discount.
- **Problem:** The code subtracts the discount value directly instead of calculating the discount as a percentage of the original price.
- **Example:** A 20% discount on 1200 should produce 960, but the current code returns 1180.
- **Expected Result:** The discount should be calculated correctly.

## Bug 4 — Incorrect Data Type Usage

- **File:** `bug4.js`
- **Bug Type:** Data Type Misuse
- **Intended Behavior:** The functions should calculate the total and average of product prices.
- **Problem:** Product prices are stored as strings instead of numbers. The `+` operator concatenates strings rather than adding their numeric values.
- **Expected Result:** The total should be 600 and the average should be 200.

## Bug 5 — Syntax Error

- **File:** `bug5.py`
- **Bug Type:** Syntax Error
- **Intended Behavior:** The function should find and return the maximum number in a list.
- **Problem:** The `if` statement is missing a colon (`:`) at the end of its condition.
- **Expected Error:** `SyntaxError`
- **How to Reproduce:** Run the Python file.

## Summary

The project contains five intentionally buggy code examples covering the following categories:

1. Runtime Error
2. Off-by-One / Loop Error
3. Logical Error
4. Data Type Misuse
5. Syntax Error

These examples will be used to test AI-assisted debugging, code correction, structured bug reporting, and reflection.
