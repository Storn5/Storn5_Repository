#include <stdio.h>
#include <math.h>

int main() {
    double sum, a, n;
    sum = 0;
    n = 0;
    do {
        n ++;
        a = n / pow(n-1, 2);
        sum += a;
    } while (a >= 0.0001)
    printf("Sum: %f", sum);
}