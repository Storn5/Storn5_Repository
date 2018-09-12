#include <stdio.h>
#include <math.h>

int main() {
    double a = 100, b = 0.001, c, d, e, ans;
    c = pow(a + b, 4);
    d = pow(a, 4) + (4*pow(a, 3)*b) + (6*pow(a, 2)*pow(b, 2));
    e = (4*a*pow(b, 3)) + pow(b, 4);
    ans = (c-d) / e;
    printf("%f\n", ans);
}