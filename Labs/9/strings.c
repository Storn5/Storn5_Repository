#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int nonRepeat(char *str) {
    char first [255], current [255];
    int i, j, firstWord = 1;
    for (i = 0; i < 255; i ++) {
        if (str[i] == ' ') {
            first[i] = '\0';
            break;
        }
        first[i] = str[i];
    }
    for (j = i+1; j < 255; j ++) {
        if (str[j] == ' ' || str[j] == '\n') {
            current[j-i-1] = '\0';
            if (strcmp(first, current) == 0)
                return 0;
            i = j;
            firstWord = 0;
        }
        if (str[j] == '\n' || str[j] == '\0')
            break;
        if (firstWord)
            current[j-i-1] = str[j];
        else
            current[j-i] = str[j];
    }
    return 1;
}

int countConsonants(char *str) {
    int consonants = 0;
    for (int i = 0; i < 255; i ++) {
        if (str[i] == '\0' || str[i] == '\n')
            break;
        if (str[i] <= 'z' && str[i] >= 'a' && str[i] != 'a' && str[i] != 'e' && str[i] != 'i' && str[i] != 'o' && str[i] != 'u' && str[i] != 'y')
            consonants ++;
        if (str[i] <= 'Z' && str[i] >= 'A' && str[i] != 'A' && str[i] != 'E' && str[i] != 'I' && str[i] != 'O' && str[i] != 'U' && str[i] != 'Y')
            consonants ++;
    }
    return consonants;
}

int main() {
    FILE *f1 = fopen("f1.txt", "r+"), *f2 = fopen("f2.txt", "w+");
    if (f1 == NULL || f2 == NULL) {
        perror("\nError opening the file.\n");
        exit(0);
    }
    char str [255];
    while (fgets(str, 255, f1) != NULL) {
        if (nonRepeat(str)) {
            printf("%s", str);
            fputs(str, f2);
        }
    }
    fseek(f1, 0, SEEK_SET);
    fgets(str, 255, f1);
    printf("\n%d\n", countConsonants(str));
    fclose(f1); fclose(f2);
}