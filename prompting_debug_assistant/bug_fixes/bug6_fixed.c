#include <stdio.h>
#include <assert.h>

int calculate_sum(int numbers[], int size) {
    int sum = 0;

    for (int i = 0; i < size; i++) {
        sum += numbers[i];
    }

    return sum;
}

int main() {
    int values[] = {10, 20, 30, 40};
    int size = 4;

    int result = calculate_sum(values, size);

    printf("Sum: %d\n", result);

    assert(result == 100);
    assert(calculate_sum(values, 0) == 0);

    printf("All tests passed!\n");

    return 0;
}
