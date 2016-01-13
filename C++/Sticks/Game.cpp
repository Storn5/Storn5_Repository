#include "Game.h"

Game::Game () {
    piles = 0;
    maxSticks = 0;
    name = "";
    name2 = "";
    turn = "";
    winner = "";
    over = false;
    choice = 3;
}

void Game::playEasy () {
    printf ("\n\n\nEnter your name: ");
    cin >> name;
    printf ("Enter the number of piles: ");
    cin >> piles;
    for (int p = 0; p < piles; p ++) {
        sticks.push_back (0);
    }
    printf ("Enter the maximum number of sticks in each pile: ");
    cin >> maxSticks;
    randomizeSticks ();
    while (!over) {
        turn = name;
        printBoard ();
        printf ("Enter the pile number [1-%d]: ", piles);
        cin >> pile;
        pile -= 1;
        if (pile < piles && pile >= 0 && sticks [pile] > 0) {
            printf ("Enter the number of sticks [1-3]: ");
            cin >> stick;
            if (stick >= 1 && stick <= 3 && sticks [pile] >= stick) {
                sticks [pile] -= stick;
                if (noSticksLeft ()) {
                    over = 1;
                    winner = turn;
                }
                else {
                    printBoard ();
                    printf ("Computer's turn. Press any key to continue...\n");
                    _getch ();
                    turn = "Computer";
                    do {
                        srand (time (0));
                        pile = rand () % piles;
                        stick = rand () % 3;
                        stick += 1;
                    } while (sticks [pile] < stick);
                    sticks [pile] -= stick;
                    if (noSticksLeft ()) {
                        over = 1;
                        winner = turn;
                    }
                }
            }
            else {
                error ();
            }
        }
        else {
            error ();
        }
    }
    printf ("\n\nGame over! %s won!\n", winner.c_str ());
    eraseBoard ();
    over = 0;
    _getch ();
}

void Game::printBoard () {
    printf ("\n");
    for (int p = 0; p < piles; p ++) {
        printf ("%d: ", p + 1);
        for (int s = 0; s < sticks [p]; s ++) {
            printf ("I");
        }
        printf ("\n");
    }
    printf ("\n");
}

void Game::randomizeSticks () {
    srand (time (0));
    for (int p = 0; p < piles; p ++) {
        sticks [p] = (rand () % (maxSticks)) + 1;
    }
}

void Game::menu () {
    printf ("Sticks v0.4\n\nMENU\nSingleplayer [1]\nMultiplayer [2]\nQuit [3]\n\n");
    cin >> choice;
    switch (choice) {
    case 1:
        playEasy ();
        break;
    case 2:
        playMulti ();
        break;
    case 3:
        //quit ();
        break;
    default:
        error ();
        break;
    }
    menu ();
}

bool Game::noSticksLeft () {
    int emptyPiles = 0;
    for (int p = 0; p < piles; p ++) {
        if (sticks [p] == 0) {
            emptyPiles += 1;
        }
    }
    if (emptyPiles == piles) {
        return 1;
    }
    else {
        return 0;
    }
}

void Game::error () {
    printf ("\n\n\n\nError!!! You may have mistyped the input. Press any key to continue...");
    _getch ();
}

void Game::playMulti () {
    printf ("\n\n\nEnter the first player's name: ");
    cin >> name;
    printf ("Enter the second player's name: ");
    cin >> name2;
    printf ("Enter the number of piles: ");
    cin >> piles;
    for (int p = 0; p < piles; p ++) {
        sticks.push_back (0);
    }
    printf ("Enter the maximum number of sticks in each pile: ");
    cin >> maxSticks;
    randomizeSticks ();
    while (!over) {
        turn = name;
        printf ("\n%s's turn.\n", name.c_str ());
        printBoard ();
        printf ("Enter the pile number [1-%d]: ", piles);
        cin >> pile;
        pile -= 1;
        if (pile < piles && pile >= 0 && sticks [pile] > 0) {
            printf ("Enter the number of sticks [1-3]: ");
            cin >> stick;
            if (stick >= 1 && stick <= 3 && sticks [pile] >= stick) {
                sticks [pile] -= stick;
                if (noSticksLeft ()) {
                    over = 1;
                    winner = turn;
                }
                else {
                    turn = name2;
                    printf ("\n%s's turn.\n", name2.c_str ());
                    printBoard ();
                    printf ("Enter the pile number [1-%d]: ", piles);
                    cin >> pile;
                    pile -= 1;
                    if (pile < piles && pile >= 0 && sticks [pile] > 0) {
                        printf ("Enter the number of sticks [1-3]: ");
                        cin >> stick;
                        if (stick >= 1 && stick <= 3 && sticks [pile] >= stick) {
                            sticks [pile] -= stick;
                            if (noSticksLeft ()) {
                                over = 1;
                                winner = turn;
                            }
                        }
                        else {
                        error ();
                        }
                    }
                    else {
                        error ();
                    }
                }
            }
            else {
                error ();
            }
        }
        else {
            error ();
        }
    }
    printf ("\n\nGame over! %s won!\n", winner.c_str ());
    eraseBoard ();
    over = 0;
    _getch ();
}

void Game::eraseBoard () {
    for (int i = 0; i < piles; i ++) {
        sticks.erase (sticks.begin () + i);
    }
}
