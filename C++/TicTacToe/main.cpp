//Мокрик Ярослав, 2015
//Підключаємо бібліотеку вводу-виводу, бібліотеку команд Windows і бібліотеку строк тексту
#include <iostream>
#include <windows.h>
#include <string>
//Ми будеми використовувати стандартний простір імен
using namespace std;
//Оголошуємо змінні для символів кожного гравця (якщо гравці їх не змінять)
char first = 'X';
char second = 'O';
//Створюємо клас для ігрової дошки
class Board {
public:
    //Перевіряємо, чи є вільні клітинки, якщо немає - нічия
    bool checkForEmptyCells () {
        for (int y = 0; y < 3; y ++) {
            for (int x = 0; x < 3; x ++) {
                if (cells [x] [y] == ' ') {
                    return 1;
                }
            }
        }
        return 0;
    }
    //Перевіряємо умови для виграшу, якщо хтось виграв - повернути First або Second, інакше повернути пробіл
    string win () {
        if ((cells [0] [0] == cells [0] [1] && cells [0] [1] == cells [0] [2] && cells [0] [0] == first) || (cells [1] [0] == cells [1] [1] && cells [1] [1] == cells [1] [2] && cells [1] [0] == first) || (cells [2] [0] == cells [2] [1] && cells [2] [1] == cells [2] [2] && cells [2] [0] == first)) {
            return "First";
        }
        else if ((cells [0] [0] == cells [0] [1] && cells [0] [1] == cells [0] [2] && cells [0] [0] == second) || (cells [1] [0] == cells [1] [1] && cells [1] [1] == cells [1] [2] && cells [1] [0] == second) || (cells [2] [0] == cells [2] [1] && cells [2] [1] == cells [2] [2] && cells [2] [0] == second)) {
            return "Second";
        }
        else if ((cells [0] [0] == cells [1] [0] && cells [1] [0] == cells [2] [0] && cells [0] [0] == first) || (cells [0] [1] == cells [1] [1] && cells [1] [1] == cells [2] [1] && cells [0] [1] == first) || (cells [0] [2] == cells [1] [2] && cells [1] [2] == cells [2] [2] && cells [0] [2] == first)) {
            return "First";
        }
        else if ((cells [0] [0] == cells [1] [0] && cells [1] [0] == cells [2] [0] && cells [0] [0] == second) || (cells [0] [1] == cells [1] [1] && cells [1] [1] == cells [2] [1] && cells [0] [1] == second) || (cells [0] [2] == cells [1] [2] && cells [1] [2] == cells [2] [2] && cells [0] [2] == second)) {
            return "Second";
        }
        else if ((cells [0] [0] == cells [1] [1] && cells [1] [1] == cells [2] [2] && cells [0] [0] == first) || (cells [2] [0] == cells [1] [1] && cells [1] [1] == cells [0] [2] && cells [2] [0] == first)) {
            return "First";
        }
        else if ((cells [0] [0] == cells [1] [1] && cells [1] [1] == cells [2] [2] && cells [0] [0] == second) || (cells [2] [0] == cells [1] [1] && cells [1] [1] == cells [0] [2] && cells [2] [0] == second)) {
            return "Second";
        }
        else if (!checkForEmptyCells ()) {
            return "Tie";
        }
        else {
            return " ";
        }
    }
    //Функція, яка повертає симовол в певній клітинці
    char getCell (int x, int y) {
        return cells [x] [y];
    }
    //Функція, яка змінює символ в певній клітинці
    void setCell (char cell, int x, int y) {
        cells [x] [y] = cell;
    }
    //Функція, яка очищає всю дошку
    void clearCells () {
        for (int y = 0; y < 3; y ++) {
            for (int x = 0; x < 3; x ++) {
                cells [x] [y] = ' ';
            }
        }
    }
    //Функція, яка виводить всю дошку на екран
    void printCells () {
        cout << "\n 123\n";
        for (int y = 0; y < 3; y ++) {
            cout << y + 1;
            for (int x = 0; x < 3; x ++) {
                cout << cells [x] [y];
            }
            cout << endl;
        }
    }
private:
    //Дошка для гри, двовимірний масив символів
    char cells [3] [3];
};

int main () {
    //Оголошуємо деякі змінні
    //Дошка
    Board board;
    //Статус гри (закінчена чи ні)
    bool over = 0;
    //Координати, які вводить гравець
    int x = 0;
    int y = 0;
    //Хід (хрестики чи нулики)
    bool o = 0;
    //Вибір в головному меню (1 або 2, грати чи вийти)
    char choice = 0;
    //Очищуємо дошку
    board.clearCells ();
    //Головне меню
    cout << "Tic Tac Toe\nBy Yaroslav Mokryk, 2015\n\nMain Menu\n\n[1]Play\n[2]Exit\n\nYour choice: ";
    cin >> choice;
    //Вихід, якщо гравець ввів 2
    if (choice == '2') {
        cout << "\nYou quit.\n";
    }
    //Інакше, почати гру
    else {
        //Пропонуємо гравцеві створити власні символи, замість хрестиків і нуликів
        cout << "Do you wish to make custom symbols? [y/n]: ";
        cin >> choice;
        //Якщо гравець вводить y або Y, створити власні символи
        if (choice == 'y' || choice == 'Y') {
            cout << "Enter the symbol for the first player: ";
            cin >> first;
            cout << "Enter the symbol for the second player: ";
            cin >> second;
        }
        //Поки гра не закінчена, продовжувати ігровий цикл
        while (!over) {
            //Вивести дошку на екран
            board.printCells ();
            //Якщо хтось виграв і не нічия - написати переможця і статус гри змінюється на завершений
            if (board.win () != " " && board.win () != "Tie") {
                cout << endl << board.win () << " player wins! Congratulations!\n";
                over = 1;
            }
            //Якщо нічия, написати це і статус гри змінюється на завершений
            else if (board.win () == "Tie") {
                cout << endl << board.win () << "!\n";
                over = 1;
            }
            //Якщо статус гри ще й досі не завершений, продовжити
            if (!over) {
                //Вводимо координати
                cout << "Enter the column: ";
                cin >> x;
                cout << "Enter the row: ";
                cin >> y;
                //Зменшуємо координати на 1 (бо масиви рахуються від нуля)
                x --;
                y --;
                //Якщо клітинка вільна, продовжити
                if (board.getCell (x, y) == ' ') {
                    //Якщо хід першого гравця - присвоїти клітинці символ першого гравця
                    if (o) {
                        board.setCell (second, x, y);
                        //Перевести хід
                        o = 0;
                    }
                    //Інакше, присвоїти клітинці символ другого гравця
                    else {
                        board.setCell (first, x, y);
                        //Перевести хід
                        o = 1;
                    }
                }
                //Якщо клітинка не вільна, написати, що введена неправильна клітинка (хід при цьому не змінюється, щоб дати можливість спробувати ще раз)
                else {
                    cout << "\nWrong cell! Try again!\n";
                }
            }
        }
    }
    //Вкінці гри вводимо Windows-команду "Pause", щоб гравці могли побачити результат
    system ("pause");
    //Програма закінчена без помилок
    return 0;
}
