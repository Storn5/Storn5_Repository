#include <iostream>
#include <string>

using namespace std;


int findMin(int len, int arr[]) {
    int min = arr[0];
    for (int i = 0; i < len; i ++)
        if (arr[i] < min) min = arr[i];
    return min;
}

string findMin(string text) {
    string tmpWord = "";
    string minWord = text;
    for (int i = 0; i < (int)text.length(); i++) {
        if(text[i] != ' ')
            tmpWord += text[i];
        else {
            if(tmpWord.length() < minWord.length())
                minWord=tmpWord;
            tmpWord = "";
        }
    }
    if(tmpWord != "") {
        if(tmpWord.length() < minWord.length())
            minWord=tmpWord;
    }
    return minWord;
}

int main() {
   int a[5];
   string b;
   for (int i = 0; i < 5; i ++) {
       cin >> a[i];
   }
   getline(cin, b);
   cout << "Min of A: " << findMin(5, a) << endl;
   cout << "Min of B: " << findMin(b) << endl;
}