#include <stdio.h>
#include <math.h>

unsigned long fact(unsigned long f) {
    if (f == 0 || f == 1) {
        return 1;
    }
    return(f * fact(f - 1));
}

int main() {
    double a = 0.1, b = 1, x, step = (b-a)/10, sn, se, y, diff;
    int n = 20;
    unsigned long i;
    for (x = a; x <= b; x += step) {
        sn = 1;
        se = 1;
        y = exp(2*x);
        diff = 1;
        for (i = 1; i < n; i ++) {
            sn += pow(2*x, i)/fact(i);
        }
        i = 1;
        while (1) {
            diff = pow(2*x, i)/fact(i);
            se += diff;
            if (diff < 0.0001) {
                break;
            }
            i ++;
        }
        printf("X = %f    SN = %f    SE = %f    Y = %f\n", x, sn, se, y);
    }
    return 0;
}