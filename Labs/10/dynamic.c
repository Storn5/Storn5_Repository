#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void init(char **lines, int n) {
    for (int i = 0; i < n; i ++)
        lines[i] = malloc(255);
}

void input(char **lines, int n) {
    for (int i = 0; i < n; i ++)
        scanf("%s", lines[i]);
}

void printLines(char **lines, int n) {
    printf("\n\nLINES: \n");
    for (int i = 0; i < n; i ++)
        printf("%s\n", lines[i]);
}

void countBadLines(char **lines, int n, int *badLines) {
    for (int i = 0; i < n; i ++) {
        badLines[i] = 0;
        for (int j = 0; j < 255; j ++)
            if ((lines[i][j] == '\0' || lines[i][j] == '\n') && lines[i][j-1] == lines[i][0] && lines[i][0] == 'a')
                badLines [i] = 1;
    }
}

int main() {
    int length;
    printf("Length: ");
    scanf("%d", &length);
    char **lines = malloc(length * sizeof(char*));
    init(lines, length);
    input(lines, length);

    int *badLines = malloc(length * sizeof(int));
    countBadLines(lines, length, badLines);
    int deleted = 0;
    for (int i = 0; i < length; i ++)
        if (badLines[i])
            deleted ++;
    char **newLines = malloc((length - deleted) * sizeof(char*));
    init(newLines, length - deleted);

    for (int i = 0, j = 0; i < length; i ++) {
        if (!badLines[i]) {
            strcpy(newLines[j], lines[i]);
            j ++;
        }
    }

    printLines(lines, length);
    printLines(newLines, length - deleted);
    free(lines);
    free(badLines);
    free(newLines);
}