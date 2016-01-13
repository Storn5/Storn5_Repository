#ifndef GAME_H
#define GAME_H
#include <stdio.h>
#include <cstdlib>
#include <string>
#include <conio.h>
#include <vector>
#include <ctime>
#include <iostream>

using namespace std;

class Game
{
    public:
        Game ();
        void playEasy ();
        void printBoard ();
        void randomizeSticks ();
        void menu ();
        bool noSticksLeft ();
        void error ();
        void playMulti ();
        void eraseBoard ();
    private:
        int piles;
        int maxSticks;
        string name;
        string name2;
        string turn;
        string winner;
        vector<int> sticks;
        bool over;
        int choice;
        int pile;
        int stick;
};

#endif
