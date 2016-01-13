#include <iostream>
#include <ctime>
#include <random>

using namespace std;

int main () {
    default_random_engine randEng (time (0));
    uniform_real_distribution <float> hitChance (0.0f, 1.0f);
    const int HUM_ATT = 50;
    const int SKEL_ATT = 30;
    const int HUM_HP = 100;
    const int SKEL_HP = 70;
    int humHP = HUM_HP;
    int skelHP = SKEL_HP;
    int humNum;
    int skelNum;
    cout << "Battle Simulator 2015\nCopyright Storn Company, 2015, All right reserved\n\n";
    cout << "Enter the number of humans: ";
    cin >> humNum;
    cout << "Enter the number of skeletons: ";
    cin >> skelNum;
    int HUM_NUM = humNum;
    int SKEL_NUM = skelNum;
    while (humNum > 0 && skelNum > 0) {
        while (humHP > 0 && skelHP > 0) {
            if (hitChance(randEng) >= 0.3f) {
                humHP -= SKEL_ATT;
            }
            if (hitChance(randEng) >= 0.3f) {
                skelHP -= HUM_ATT;
            }
        }
        if (skelHP <= 0) {
            skelNum --;
            skelHP = SKEL_HP;
        }
        if (humHP <= 0) {
            humNum --;
            humHP = HUM_HP;
        }
    }
    cout << "\n\nHumans left: " << humNum << endl << "Skeletons left: " << skelNum;
    cout << "\n\nHumans died: " << HUM_NUM - humNum << endl << "Skeletons died: " << SKEL_NUM - skelNum;
    system ("PAUSE>nul");
    return 0;
}
