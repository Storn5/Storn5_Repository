#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main() {
    double change;
    int coins = 0, changeInt;
    while(1) {
        printf("Change: ");
        change = get_float();
        if(change >= 0) {
            break;
        }
    }
    changeInt = (int)round(change * 100);
    printf("%d %d\n", coins, changeInt);
    coins += (int)(changeInt / 25);
    changeInt -= (int)(changeInt / 25) * 25;
    printf("%d %d\n", coins, changeInt);
    coins += (int)(changeInt / 10);
    changeInt -= (int)(changeInt / 10) * 10;
    printf("%d %d\n", coins, changeInt);
    coins += (int)(changeInt / 5);
    changeInt -= (int)(changeInt / 5) * 5;
    printf("%d %d\n", coins, changeInt);
    coins += (int)(changeInt);
    printf("%d\n", coins);
}