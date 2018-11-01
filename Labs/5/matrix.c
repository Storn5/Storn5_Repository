#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

bool isGood (int n, int nums[][n]) {
    bool possible = true;
    for (int i = 0; i < n-1; i ++) {
        if  (nums[i][0] > nums[i+1][0])
            possible = false;
    }
    return possible;
}

int main() {
    //Initialize random number generator
    time_t t;
    srand((unsigned) time(&t));

    int n = 0;
    printf("Enter N: ");
    scanf("%d", &n);
    int numbers[n*n];
    for (int i = 0; i < n*n; i ++) {
        numbers[i] = rand()%100;
    }
    int matrix[n][n];
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < n; j ++) {
            matrix[i][j] = numbers[i * n + j];
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
    if (isGood(n, matrix))
        printf("Possible.\n");
    else
        printf("No.\n");
}