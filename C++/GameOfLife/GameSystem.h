#ifndef GAMESYSTEM_H
#define GAMESYSTEM_H
#include <string>
#include <stdio.h>
#include <conio.h>
#include <fstream>
#include <vector>
#include <cstdlib>

using namespace std;

class GameSystem
{
    public:
        GameSystem();
        void playGame ();
        void loadLevel (string level);
        void printLevel ();
        void createCells ();
        void killCells ();
        void killX ();
        void createO ();
        int findNeighbours (int x, int y);
    private:
        bool over;
        vector <string> map;
};

#endif
