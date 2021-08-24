#include <stdio.h>

long int Fibonacci(unsigned long int n){
    if (n<0)
        printf("Incorrect input");
    else if (n==1)
        return 0 ;
    else if (n==2)
        return 1;
    else
        return Fibonacci(n-1)+Fibonacci(n-2); }
int main(void){
    unsigned long int count;

    if (1){
    printf("Maximum number of n: ");
    scanf("%ld",&count);}

    int n = 2;
    unsigned long int m = 0;
    int arr1[count];
    int arr2[count];
    printf("VAL OF n   VAL OF m   VAL OF Exp   TRUE/FALSE\n");
    for (n=2; n<count; n++){
        m=Fibonacci(n);
        arr1[n-2]=n;
        arr2[n-2]=m;
    }
    printf(" %d ",arr1);
    printf("%d",arr2);
    printf("\n\n\n");
    printf("Finished");
    return 0;
}