#include <stdio.h>

int main() {
    int m, n, o, p, r;
    scanf("%d %d", &m, &n);
    o = --m - ++n;
    p = m*n < n;
    n++;
    r = n-- > m++;
    printf("1) %d\n2) %d\n3) %d\n", o, p, r);
}