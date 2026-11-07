# Fix Validation Report

## Bug 1 — bug1_fixed.py

- **Input:** `[80, 90, 75, 85]`
- **Expected Output:** `82.5`
- **Actual Output:** `82.5` ✅
- **Additional Test:** Empty list raises `ValueError`.
- **Result:** Passed.

## Bug 2 — bug2_fixed.js

- **Input:** Three users: Aytac, Leyla, Nigar.
- **Expected Output:** `["Aytac", "Leyla", "Nigar"]`
- **Actual Output:** `["Aytac", "Leyla", "Nigar"]` ✅
- **Additional Test:** The loop does not access an invalid array index.
- **Result:** Passed.

## Bug 3 — bug3_fixed.py

- **Input:** Price = 100, Discount = 20%.
- **Expected Output:** `80`
- **Actual Output:** `80` ✅
- **Additional Test:** Price = 200, Discount = 10%, result = 180.
- **Result:** Passed.

## Bug 4 — bug4_fixed.js

- **Input:** `["100", "200", "300"]`
- **Expected Output:** Total = `600`, Average = `200`.
- **Actual Output:** Total = `600`, Average = `200` ✅
- **Additional Test:** Empty array returns `0` for the average.
- **Result:** Passed.

## Bug 5 — bug5_fixed.py

- **Input:** `[12, 45, 7, 89, 34]`
- **Expected Output:** `89`
- **Actual Output:** `89` ✅
- **Additional Test:** Negative numbers return `-2`; empty list returns `None`.
- **Result:** Passed.

## Bug 6 — bug6_fixed.c

- **Input:** `{10, 20, 30, 40}`
- **Expected Output:** `100`
- **Actual Output:** `100` ✅
- **Additional Test:** An array size of `0` returns `0`.
- **Result:** Passed.

## Summary

All six code snippets have been corrected to address their original bugs. Test cases and expected outcomes have been documented for each fix.

**Manual Adjustments:** Empty-input handling and additional assertions were included to improve reliability and test coverage.
