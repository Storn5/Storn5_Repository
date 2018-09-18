#include <sc50.h>
#include <stdio.h>
#include <math.h>

int main() {
    float change;
    int coins = 0;
    while(1) { 
        printf("Change: ");
        change = GetFloat();
        if(change >= 0) {
            break;
        }
    }
    coins += (int)(change / 0.25);
    change -= (int)(change / 0.25) * 0.25;
    coins += (int)(change / 0.1);
    change -= (int)(change / 0.1) * 0.1;
    coins += (int)(change / 0.05);
    change -= (int)(change / 0.05) * 0.05;
    change *= 100
    coins += (int)round(change);
    printf("%d\n", coins);
}