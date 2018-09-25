#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>

int main(int argc, string argv[]) {
    if (argc != 2) {
        return 1;
    }
    int k = atoi(argv[1]);
    printf("Word: ");
    string p = get_string();
    printf("ciphertext: ");
    for (int i = 0, n = strlen(p); i < n; i ++) {
        if (p[i] >= 'a' && p[i] <= 'z') {
            if (p[i]+(k%26) >= 'z') {
                printf("%c", p[i]-26+(k%26));
            }
            else {
                printf("%c", p[i]+(k%26));
            }
        }
        else {
            if (p[i]+(k%26) >= 'Z') {
                printf("%c", p[i]-26+(k%26));
            }
            else {
                printf("%c", p[i]+(k%26));
            }
        }
    }
    printf("\n");
    return 0;
}