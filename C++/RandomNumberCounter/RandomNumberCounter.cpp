#include <iostream>
#include <conio.h>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    srand (time (0));
    int randMax;
    int randMin;
    int randCount;
    cout << "Random Number Counter v0.07\n";
    cout << "Enter the minimum number: ";
    cin >> randMin;
    cout << "Enter the maximum number: ";
    cin >> randMax;
    cout << "Enter the number of numbers: ";
    cin >> randCount;
    cout << "This application will now generate " << randCount << " random numbers in the range [" << randMin << "; " << randMax << "]\n";
    cout << "Your numbers are:\n";
    for (int i = 0; i < randCount; i ++) {
        cout << (randMin + (rand () % (1 + (randMax - randMin)))) << "\n";
    }
    _getch ();
    return 0;
}
