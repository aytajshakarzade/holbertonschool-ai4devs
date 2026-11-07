#include <stdio.h>

int calculate_sum(int numbers[], int size) {
    int sum = 0;

    for (int i = 0; i <= size; i++) {
        sum += numbers[i];
    }

    return sum;
}

int main() {
    int values[] = {10, 20, 30, 40};
    int size = 4;

    int result = calculate_sum(values, size);

    printf("Sum: %d\n", result);

    return 0;
}
