//������ �������, 2015
//ϳ�������� �������� �����-������, �������� ������ Windows � �������� ����� ������
#include <iostream>
#include <windows.h>
#include <string>
//�� ������ ��������������� ����������� ������ ����
using namespace std;
//��������� ���� ��� ������� ������� ������ (���� ������ �� �� ������)
char first = 'X';
char second = 'O';
//��������� ���� ��� ������ �����
class Board {
public:
    //����������, �� � ���� �������, ���� ���� - ����
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
    //���������� ����� ��� �������, ���� ����� ������ - ��������� First ��� Second, ������ ��������� �����
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
    //�������, ��� ������� ������� � ����� �������
    char getCell (int x, int y) {
        return cells [x] [y];
    }
    //�������, ��� ����� ������ � ����� �������
    void setCell (char cell, int x, int y) {
        cells [x] [y] = cell;
    }
    //�������, ��� ����� ��� �����
    void clearCells () {
        for (int y = 0; y < 3; y ++) {
            for (int x = 0; x < 3; x ++) {
                cells [x] [y] = ' ';
            }
        }
    }
    //�������, ��� �������� ��� ����� �� �����
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
    //����� ��� ���, ���������� ����� �������
    char cells [3] [3];
};

int main () {
    //��������� ���� ����
    //�����
    Board board;
    //������ ��� (�������� �� �)
    bool over = 0;
    //����������, �� ������� �������
    int x = 0;
    int y = 0;
    //ճ� (�������� �� ������)
    bool o = 0;
    //���� � ��������� ���� (1 ��� 2, ����� �� �����)
    char choice = 0;
    //������� �����
    board.clearCells ();
    //������� ����
    cout << "Tic Tac Toe\nBy Yaroslav Mokryk, 2015\n\nMain Menu\n\n[1]Play\n[2]Exit\n\nYour choice: ";
    cin >> choice;
    //�����, ���� ������� ��� 2
    if (choice == '2') {
        cout << "\nYou quit.\n";
    }
    //������, ������ ���
    else {
        //��������� ������� �������� ����� �������, ������ �������� � ������
        cout << "Do you wish to make custom symbols? [y/n]: ";
        cin >> choice;
        //���� ������� ������� y ��� Y, �������� ����� �������
        if (choice == 'y' || choice == 'Y') {
            cout << "Enter the symbol for the first player: ";
            cin >> first;
            cout << "Enter the symbol for the second player: ";
            cin >> second;
        }
        //���� ��� �� ��������, ������������ ������� ����
        while (!over) {
            //������� ����� �� �����
            board.printCells ();
            //���� ����� ������ � �� ���� - �������� ��������� � ������ ��� ��������� �� ����������
            if (board.win () != " " && board.win () != "Tie") {
                cout << endl << board.win () << " player wins! Congratulations!\n";
                over = 1;
            }
            //���� ����, �������� �� � ������ ��� ��������� �� ����������
            else if (board.win () == "Tie") {
                cout << endl << board.win () << "!\n";
                over = 1;
            }
            //���� ������ ��� �� � ��� �� ����������, ����������
            if (!over) {
                //������� ����������
                cout << "Enter the column: ";
                cin >> x;
                cout << "Enter the row: ";
                cin >> y;
                //�������� ���������� �� 1 (�� ������ ��������� �� ����)
                x --;
                y --;
                //���� ������� �����, ����������
                if (board.getCell (x, y) == ' ') {
                    //���� ��� ������� ������ - �������� ������� ������ ������� ������
                    if (o) {
                        board.setCell (second, x, y);
                        //��������� ���
                        o = 0;
                    }
                    //������, �������� ������� ������ ������� ������
                    else {
                        board.setCell (first, x, y);
                        //��������� ���
                        o = 1;
                    }
                }
                //���� ������� �� �����, ��������, �� ������� ����������� ������� (��� ��� ����� �� ���������, ��� ���� ��������� ���������� �� ���)
                else {
                    cout << "\nWrong cell! Try again!\n";
                }
            }
        }
    }
    //����� ��� ������� Windows-������� "Pause", ��� ������ ����� �������� ���������
    system ("pause");
    //�������� �������� ��� �������
    return 0;
}
