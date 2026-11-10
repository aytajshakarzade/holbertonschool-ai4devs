# Bug Descriptions

This project contains four intentionally flawed code snippets written in Python, JavaScript, and Java. Each example demonstrates a common programming issue.

## bug1.py
- **Language:** Python
- **Intended Behavior:** Return the last `n` elements of a list.
- **Current Issue:** The slicing logic uses an incorrect end index, which can return fewer elements than expected.
- **Bug Type:** Logic error (off-by-one).

## bug2.js
- **Language:** JavaScript
- **Intended Behavior:** Calculate the total price of all products in a shopping cart.
- **Current Issue:** The function uses incorrect type handling and may concatenate strings instead of calculating a numeric total.
- **Bug Type:** Type coercion error.

## bug3.java
- **Language:** Java
- **Intended Behavior:** Find and return an element from an array using its index.
- **Current Issue:** The method does not properly validate the index, which can cause an ArrayIndexOutOfBoundsException.
- **Bug Type:** Runtime error.

## bug4.py
- **Language:** Python
- **Intended Behavior:** Check whether a user is allowed to access a resource based on their role.
- **Current Issue:** The authorization condition is incorrectly implemented and may grant access to users with insufficient permissions.
- **Bug Type:** Security / authorization logic error.

## Summary

The snippets cover logic errors, type handling problems, runtime exceptions, and authorization weaknesses. They are intended to be used for debugging, testing, and evaluating AI-generated fixes.
