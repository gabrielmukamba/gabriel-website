#include<stdio.h> 

int main() {
    int a, b;

    printf("enter two number:");
    scanf("%d %d", &a, &b);

    if (a > b)
        printf("Largest number = %d", a);
    else 
        printf("Largest number = %d", b);    
    
     
 return 0; 
}
