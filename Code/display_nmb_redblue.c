#include <stdio.h>

int main() {
    int choice;

    printf("enter a number (1-4): ");
    scanf("%d", &choice);

    switch (choice){
        case 1: 
            printf("Red\n");
            break;
        case 2:
            printf("Blue\n");
            break;
        case 3:
            printf("Green\n");
            break;
        case 4:
            printf("Yello\n");
            break;
        default:
            printf("No valid choice\n");
    }
    return 0;
}