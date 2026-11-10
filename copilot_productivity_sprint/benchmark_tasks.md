# Benchmark Tasks – Copilot Productivity Sprint

## Introduction

For this sprint, I selected three small programming tasks that cover different parts of software development. Each task should take approximately 15–30 minutes to complete.

The same tasks will be solved twice: first without AI assistance and then with GitHub Copilot.

The goal is to compare the time required, code quality, and number of corrections needed.

---

## Task 1 – User Registration Validation

**Estimated Time:** 15–20 minutes

**Requirements:**

Create a function that validates user registration data. It should check whether the username, email, and password meet basic requirements.

- Username must not be empty.
- Email must have a valid format.
- Password must contain at least 8 characters.
- Return clear validation messages for invalid fields.

**Inputs:**

A user object containing:

```json
{
  "username": "aytaj",
  "email": "aytaj@example.com",
  "password": "Secure123"
}
```

**Outputs:**

A validation result indicating whether the registration data is valid, along with any error messages.

Example successful output:

```json
{
  "isValid": true,
  "errors": []
}
```

**Acceptance Criteria:**

- Returns valid when all fields meet the requirements.
- Rejects an empty username.
- Rejects an incorrectly formatted email.
- Rejects passwords shorter than 8 characters.
- Returns meaningful error messages.
- Handles missing or null values without crashing.

---

## Task 2 – Product Price Calculator

**Estimated Time:** 15–20 minutes

**Requirements:**

Create a function that calculates the final price of a product after applying a discount.

The function should:

- Accept the original product price.
- Accept a discount percentage.
- Calculate the discount amount.
- Return the final price.
- Reject negative prices and invalid discount percentages.

**Inputs:**

```json
{
  "price": 100,
  "discountPercentage": 20
}
```

**Outputs:**

```json
{
  "originalPrice": 100,
  "discountAmount": 20,
  "finalPrice": 80
}
```

**Acceptance Criteria:**

- Correctly calculates the discount amount.
- Returns the correct final price.
- Accepts a discount percentage between 0 and 100.
- Rejects negative product prices.
- Rejects discount percentages below 0 or above 100.
- Handles invalid inputs appropriately.

---

## Task 3 – REST API Task Manager

**Estimated Time:** 20–30 minutes

**Requirements:**

Create a simple task management API that allows users to add, retrieve, update, and delete tasks.

Each task should contain:

- An ID.
- A title.
- A description.
- A completion status.

The API should support the following operations:

- POST /tasks – Create a new task.
- GET /tasks – Retrieve all tasks.
- PUT /tasks/{id} – Update an existing task.
- DELETE /tasks/{id} – Delete a task.

**Inputs:**

Example request for creating a task:

```json
{
  "title": "Complete Copilot Sprint",
  "description": "Finish the benchmark tasks",
  "isCompleted": false
}
```

**Outputs:**

Example successful response:

```json
{
  "id": 1,
  "title": "Complete Copilot Sprint",
  "description": "Finish the benchmark tasks",
  "isCompleted": false
}
```

**Acceptance Criteria:**

- Successfully creates a task and returns HTTP 201.
- Returns all existing tasks with HTTP 200.
- Updates an existing task successfully.
- Deletes an existing task successfully.
- Returns HTTP 404 when a task ID does not exist.
- Rejects requests with an empty task title.
- Returns appropriate HTTP status codes and error messages.

---

## Experiment Notes

All three tasks will be completed under the same conditions.

For each task, I will record:

1. Time spent completing the task.
2. Number of lines of code written.
3. Number of tests passed.
4. Number of bugs or corrections required.
5. Overall code quality.

The first attempt will be completed without AI assistance. The second attempt will use GitHub Copilot.

This approach will make it easier to compare the results and understand where AI assistance provides the most benefit.
