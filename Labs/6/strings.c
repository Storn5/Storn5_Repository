#include <stdio.h>
#include <string.h>
#include <ctype.h>

void bubbleSort(char words[16][16], int num) {
    for (int i = 0; i < num - 1; i ++) {
        int j = 0;
        while (words[i][j] == words[i+1][j])
            j ++;
        if (words[i][j] < words[i+1][j]) {
            char temp[16];
            strcpy(temp, words[i]);
            strcpy(words[i], words[i+1]);
            strcpy(words[i+1], temp);
        }
    }
}

int main() {
    char text[256];
    char words[16][16];
    fgets(text, 256, stdin);
    int word = 0, wordStart = 0;
    for (int i = 0; i < 256; i ++) {
        if (text[i] == '\0' || text[i] == '.')
            break;
        else if (text[i] != ' ')
            words[word][i-wordStart] = text[i];
        else {
            words[word][i-wordStart] = '\0';
            wordStart = i + 1;
            if (isdigit(words[word][0]))
                word ++;
        }
    }
    bubbleSort(words, word+1);
    for (int i = 0; i < word+1; i ++)
        printf("%s\n", words[i]);
}