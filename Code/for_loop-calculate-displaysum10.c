#include <stdio.h>

int main() {
    int sum = 0;
    for (int i = 2; i <= 10; i += 2) {
        sum += i;
    }
    printf("the sum of even numbers from 1 to 10 is: %d\n, sum");
    return 0;
}    