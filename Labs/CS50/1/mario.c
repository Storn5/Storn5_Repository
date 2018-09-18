#include <sc50.h>
#include <stdio.h>

int main() {
    int height;
    while(1) { 
        printf("Height: ");
        height = GetInt();
        if(height <= 23 && height >= 0) {
            break;
        }
    }
    for(int i = 0; i < height; i ++) {
        for(int j = 0; j < height - (i+1); j ++) { 
            printf(" ");
        }
        for(int j = 0; j <= i+1; j ++) { 
            printf("#");
        }
        printf("\n");
    }
}