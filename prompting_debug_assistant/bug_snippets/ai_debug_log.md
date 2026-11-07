# AI Debugging Log

## Bug 1 — bug1.py

**AI Diagnosis:**  
The function `calculate_average()` divides the sum by the number of elements without checking whether the list is empty. When an empty list is passed, `len(numbers)` is zero, causing a `ZeroDivisionError`.

**Suggested Fix:**  
Check whether the list is empty before performing the division. Raise a `ValueError` if no numbers are provided.

**Fixed Code:**
```python
def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")

    total = sum(numbers)
    return total / len(numbers)
```

**Alternative Fixes Tested:** None.

**Result:** The fix prevents division by zero and correctly calculates the average for non-empty lists.

---

## Bug 2 — bug2.js

**AI Diagnosis:**  
The loop uses `i <= users.length` instead of `i < users.length`. This causes the loop to access an array index outside its valid range. The final iteration tries to read the `name` property of `undefined`.

**Suggested Fix:**  
Change the loop condition from `i <= users.length` to `i < users.length`.

**Fixed Code:**
```javascript
function getUserNames(users) {
    const names = [];

    for (let i = 0; i < users.length; i++) {
        names.push(users[i].name);
    }

    return names;
}
```

**Alternative Fixes Tested:** None.

**Result:** The function now returns all user names without accessing an invalid array index.

---

## Bug 3 — bug3.py

**AI Diagnosis:**  
The function subtracts the discount value directly from the product price. However, the discount represents a percentage, not a fixed amount. This produces an incorrect discounted price.

**Suggested Fix:**  
Calculate the discount amount by multiplying the price by the discount percentage divided by 100.

**Fixed Code:**
```python
def calculate_discount(price, discount):
    discounted_price = price - (price * discount / 100)
    return discounted_price
```

**Alternative Fixes Tested:** None.

**Result:** The function now correctly calculates percentage-based discounts.

---

## Bug 4 — bug4.js

**AI Diagnosis:**  
The product prices are stored as strings instead of numbers. In JavaScript, adding strings results in concatenation rather than numerical addition. Consequently, the total and average calculations are incorrect.

**Suggested Fix:**  
Convert each price to a number before adding it to the total.

**Fixed Code:**
```javascript
function calculateTotal(prices) {
    let total = 0;

    for (let i = 0; i < prices.length; i++) {
        total += Number(prices[i]);
    }

    return total;
}
```

**Alternative Fixes Tested:** None.

**Result:** The function now performs numerical addition and calculates the correct total and average for valid numeric price strings.

---

## Bug 5 — bug5.py

**AI Diagnosis:**  
The `if` statement inside the loop is missing a colon at the end of its condition. Python requires a colon after conditional statements. Without it, the program raises a `SyntaxError`.

**Suggested Fix:**  
Add a colon after `if number > maximum`.

**Fixed Code:**
```python
def find_maximum(numbers):
    if len(numbers) == 0:
        return None

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum
```

**Alternative Fixes Tested:** None.

**Result:** The syntax error is resolved, and the function correctly finds the maximum number in a non-empty list.

---

## Bug 6 — bug6.c

**AI Diagnosis:**  
The `for` loop uses `i <= size`, which causes it to access one element beyond the end of the array. Valid array indices range from `0` to `size - 1`. Accessing `numbers[size]` results in undefined behavior in C.

**Suggested Fix:**  
Change the loop condition from `i <= size` to `i < size`.

**Fixed Code:**
```c
#include <stdio.h>

int calculate_sum(int numbers[], int size) {
    int sum = 0;

    for (int i = 0; i < size; i++) {
        sum += numbers[i];
    }

    return sum;
}
```

**Alternative Fixes Tested:** None.

**Result:** The function now accesses only valid array elements and correctly calculates their sum.
