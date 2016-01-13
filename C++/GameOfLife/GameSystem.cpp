#include "GameSystem.h"

using namespace std;

GameSystem::GameSystem()
{
    printf ("Conway's Game of Life\nEnter the level name: ");
    char levelName [100];
    scanf ("%s", levelName);
    loadLevel (levelName);
}

void GameSystem::playGame () {
    over = 0;
    while (!over) {
        printLevel ();
        _getch ();
        killCells ();
        createCells ();
        killX ();
        createO ();
    }
}

void GameSystem::loadLevel (string level) {
    ifstream inFile;
    inFile.open (level);
    if (inFile.fail ()) {
        perror (level.c_str ());
        _getch ();
        exit (1);
    }
    string line;
    while (getline (inFile, line)) {
        map.push_back (line);
    }
    inFile.close ();
}

void GameSystem::printLevel () {
    printf ("\n\n\n");
    for (int i = 0; i < map.size (); i ++) {
        printf ("%s\n", map [i].c_str ());
    }
    printf ("Press space to go to the next turn\n");
}

void GameSystem::createCells () {
    for (int y = 1; y < (map.size ()) - 1; y ++) {
        for (int x = 1; x < (map [y].size ()) - 1; x ++) {
            if (findNeighbours (x, y) == 3 && map [x] [y] == ' ') {
                map [x] [y] = 'o';
            }
        }
    }
}

void GameSystem::killCells () {
    for (int y = 1; y < (map.size ()) - 1; y ++) {
        for (int x = 1; x < (map [y].size ()) - 1; x ++) {
            if ((findNeighbours (x, y) <= 1 || findNeighbours (x, y) >= 4) && map [x] [y] == 'O') {
                map [x] [y] = 'X';
            }
        }
    }
}

void GameSystem::killX () {
    for (int y = 1; y < (map.size ()) - 1; y ++) {
        for (int x = 1; x < (map [y].size ()) - 1; x ++) {
            if (map [x] [y] == 'X') {
                map [x] [y] = ' ';
            }
        }
    }
}

void GameSystem::createO () {
    for (int y = 1; y < (map.size ()) - 1; y ++) {
        for (int x = 1; x < (map [y].size ()) - 1; x ++) {
            if (map [x] [y] == 'o') {
                map [x] [y] = 'O';
            }
        }
    }
}

int GameSystem::findNeighbours (int x, int y) {
    int neighbours = 0;
    if (map [x-1] [y-1] == 'O' || map [x-1] [y-1] == 'X') {
        neighbours += 1;
    }
    if (map [x-1] [y] == 'O' || map [x-1] [y] == 'X') {
        neighbours += 1;
    }
    if (map [x-1] [y+1] == 'O' || map [x-1] [y+1] == 'X') {
        neighbours += 1;
    }
    if (map [x] [y-1] == 'O' || map [x] [y-1] == 'X') {
        neighbours += 1;
    }
    if (map [x] [y+1] == 'O' || map [x] [y+1] == 'X') {
        neighbours += 1;
    }
    if (map [x+1] [y] == 'O' || map [x+1] [y] == 'X') {
        neighbours += 1;
    }
    if (map [x+1] [y-1] == 'O' || map [x+1] [y-1] == 'X') {
        neighbours += 1;
    }
    if (map [x+1] [y+1] == 'O' || map [x+1] [y+1] == 'X') {
        neighbours += 1;
    }
    return neighbours;
}
