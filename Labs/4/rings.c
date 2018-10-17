#include <stdio.h>
#include <math.h>

void printRing(int *ring, int len, int k) {
    for (int j = 0; j < len; j ++) {
        k--;
        if (k == -1)
            k = len - 1;
        printf("%d, ", ring[k]);
    }
    printf("\n");
}

int main() {
    int length = 12, k;
    int ring[100] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
    printf("Enter k: ");
    scanf("%d", &k);
    printRing(ring, length, k);
    printf("Enter 2 values to add: ");
    int a, b;
    scanf("%d %d", &a, &b);
    ring[length] = a;
    ring[length + 1] = b;
    length += 2;
    printRing(ring, length, k);
    for (int i = 0; i < length; i ++) {
        ring[i] = ring[i * 2 + 1];
    }
    length = length / 2;
    printRing(ring, length, k);
    return 0;
}