#include <stdio.h>

int main() {
    int password;

    do {
        printf("Enter the password: ");
        scanf("%d", &password);

        if (password != 1234) {
            printf("incorrect. try again.\n");
        }    
    } while (password != 1234);

    printf("Access Granted!\n");
    return 0;
}    
