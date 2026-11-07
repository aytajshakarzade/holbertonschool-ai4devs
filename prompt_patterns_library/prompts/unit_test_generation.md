# Unit Test Generation Prompt Template

## Role
Act as an experienced software engineer specializing in software testing, test automation, and test-driven development.

## Task
Analyze the provided source code and generate comprehensive unit tests to verify that individual functions, methods, and components behave as expected.

## Input Placeholder
[PROGRAMMING_LANGUAGE]

[CODE_BLOCK]

[TESTING_FRAMEWORK]

[PROJECT_CONTEXT]

[EXPECTED_BEHAVIOR]

## Expected Output
1. A list of test cases covering the main functionality.
2. Complete unit test code using the specified testing framework.
3. Tests for normal and expected inputs.
4. Tests for edge cases and invalid inputs.
5. Expected results for each test case.
6. Instructions for running the tests.

## Instructions
- Follow the conventions of the specified testing framework.
- Test individual units independently.
- Include positive and negative test cases.
- Avoid unnecessary dependencies and excessive mocking.
- Do not modify the original source code.
- Ensure that tests are clear, maintainable, and repeatable.
