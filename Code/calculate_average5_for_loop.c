#include <stdio.h>

int main() {
    float number, sum = 0.0, average;

    for (int i = 1; i <= 5; i++) {
        printf("Enter number %d: ", i);
        scanf("%f", &number);
        sum += number;
    }
    
    average = sum / 5;
    printf("the average of the 5 numbers is: %.2f\n", average);
    return 0;
}    