# Cross-Language Specification – Log Analyzer

## 1. Algorithm Description

The Log Analyzer is a small application designed to process server log entries and extract useful information from them.

The main purpose is to analyze HTTP requests and generate a summary of server activity.

The algorithm performs the following operations:

- Counts the total number of requests.
- Identifies the number of unique visitors using their IP addresses.
- Counts failed requests with HTTP status codes between 400 and 599.
- Calculates the error rate as a percentage.
- Groups requests by HTTP status code.

The implementation should produce the same results regardless of the programming language used.

## 2. Input Format

The algorithm receives a collection of server log entries.

Each entry contains:

- IP address
- Timestamp
- HTTP method
- Requested URL
- HTTP status code

Example input:

```json
[
  {
    "ip": "192.168.1.10",
    "timestamp": "2026-11-10T10:00:00",
    "method": "GET",
    "url": "/api/users",
    "status": 200
  },
  {
    "ip": "192.168.1.11",
    "timestamp": "2026-11-10T10:01:00",
    "method": "POST",
    "url": "/api/login",
    "status": 401
  },
  {
    "ip": "192.168.1.10",
    "timestamp": "2026-11-10T10:02:00",
    "method": "GET",
    "url": "/api/products",
    "status": 200
  }
]
```

## 3. Output Format

The algorithm returns a JSON object containing the analysis results.

Example output:

```json
{
  "total_requests": 3,
  "unique_visitors": 2,
  "error_count": 1,
  "error_rate": 33.33,
  "status_codes": {
    "200": 2,
    "401": 1
  }
}
```

The error rate is calculated using:

Error Rate = (Error Count / Total Requests) * 100

Only HTTP status codes from 400 to 599 are considered errors.

If there are no requests, the error rate must be 0.

## 4. Edge Cases

The implementation must handle the following situations:

1. Empty input: Return zero for all statistics.
2. Single log entry: Process one request correctly.
3. Duplicate IP addresses: Count the same IP address only once when calculating unique visitors.
4. Invalid status code: Ignore entries with missing or invalid status codes.
5. Missing IP address: Do not include missing IP addresses in the unique visitor count.
6. All requests successful: Return an error count of zero and an error rate of zero.
7. All requests failed: Return an error rate of 100 percent.
8. Invalid input format: Handle the input without crashing.

## 5. Test Cases

### Test Case 1 – Normal Requests

**Input:** Three requests with status codes 200, 401, and 200.

**Expected Output:**
- Total requests: 3
- Unique visitors: 2
- Error count: 1
- Error rate: 33.33%

### Test Case 2 – Empty Input

**Input:** An empty list.

**Expected Output:**
- Total requests: 0
- Unique visitors: 0
- Error count: 0
- Error rate: 0%

### Test Case 3 – Duplicate Visitors

**Input:** Four requests from the same IP address with status codes 200, 200, 404, and 500.

**Expected Output:**
- Total requests: 4
- Unique visitors: 1
- Error count: 2
- Error rate: 50%

### Test Case 4 – All Successful Requests

**Input:** Three requests with status codes 200, 201, and 204.

**Expected Output:**
- Total requests: 3
- Unique visitors: 3
- Error count: 0
- Error rate: 0%

### Test Case 5 – All Failed Requests

**Input:** Three requests with status codes 400, 404, and 500.

**Expected Output:**
- Total requests: 3
- Unique visitors: 3
- Error count: 3
- Error rate: 100%

### Test Case 6 – Mixed HTTP Status Codes

**Input:** Five requests with status codes 200, 301, 403, 404, and 503.

**Expected Output:**
- Total requests: 5
- Unique visitors: 5
- Error count: 3
- Error rate: 60%

## 6. Functional Requirements

The algorithm must:

- Accept a list of log entries.
- Validate the required input fields.
- Count valid requests.
- Identify unique visitors.
- Calculate the number and percentage of errors.
- Group requests by HTTP status code.
- Return the results in a consistent JSON structure.

## 7. Cross-Language Compatibility

The algorithm will be implemented in at least three programming languages:

- Python
- JavaScript (Node.js)
- Go

All implementations must follow the same specification and produce equivalent results for the same input data.

The same test cases will be used to verify each implementation.

## 8. Performance and Validation

Each implementation will be tested using the same input datasets.

The following aspects will be evaluated:

- Correctness of the results.
- Handling of edge cases.
- Execution time.
- Memory usage.
- Consistency between programming languages.

## 9. Conclusion

This specification defines the expected behavior of the Log Analyzer before implementation begins.

Having a common specification and a fixed set of test cases will make it possible to compare implementations across different programming languages and evaluate the accuracy of AI-assisted code translation.
