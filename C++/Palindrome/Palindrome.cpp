#include <stdio.h>
#include <conio.h>
#include <string.h>

using namespace std;

int main () {
    char input [100];
    scanf ("%s", input);
    bool notPalindrome = false;
    for (int i = 0; i < strlen (input) / 2; i ++) {
        if (input [i] != input [strlen (input) - (i + 1)]) {
            notPalindrome = true;
        }
    }
    if (notPalindrome) {
        printf ("%s is not a palindrome.", input);
    } else {
        printf ("%s is a palindrome.", input);
    }
    _getch ();
    return 0;
}
