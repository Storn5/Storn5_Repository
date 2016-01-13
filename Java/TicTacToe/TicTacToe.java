import java.util.Scanner;
import java.util.Random;

public class TicTacToeClass {
	static Scanner input = new Scanner (System.in);
	static Random botInput = new Random ();
	static char [] [] board = new char [3] [3];
	public static void main (String args []) {
		for (int y = 0; y < 3; y ++) {
			for (int x = 0; x < 3; x ++) {
				board [x] [y] = '_';
			}
		}
		System.out.print ("\n\nTTT - Tic Tac Toe\nv0.51\n\nMain Menu\n\n[1]Singleplayer\n[2]Multiplayer\n[3]Exit\n\nEnter your choice: ");
		switch (input.nextInt ()) {
		case 1:
			System.out.print ("\nSides:\n[1]X\n[2]O\n\nPick a side: ");
			switch (input.nextInt ()) {
			case 1:
				PlaySingle ('X', 'X');
				break;
			case 2:
				PlaySingle ('X', 'O');
				break;
			default:
				System.out.println ("\nWrong number.");
				break;
			}
			break;
		case 2:
			PlayMulti ('X');
			break;
		case 3:
			System.out.println ("\nYou quit.");
			break;
		default:
			System.out.println ("\nWrong number.");
			break;
		}
	}
	public static void PlaySingle (char curTurn, char playerTurn) {
		boolean over = false;
		while (!over) {
			if (curTurn == 'X' && playerTurn == 'X') {
				PrintBoard ();
				System.out.print ("Enter the column number: ");
				int x = input.nextInt () - 1;
				System.out.print ("Enter the row number: ");
				int y = input.nextInt () - 1;
				if (x <= 2 && x >= 0 && y <= 2 && y >= 0) {
					if (board [x] [y] == '_'){
						board [x] [y] = curTurn;
						if (GameOver (x, y)) {
							over = true;
							PrintBoard ();
							System.out.println ("\nCongratulations! " + curTurn + " wins!!!");
							}
						else if (board [0] [0] != '_' && board [0] [1] != '_' && board [0] [2] != '_' && board [1] [0] != '_' && board [1] [1] != '_' && board [1] [2] != '_' && board [2] [0] != '_' && board [2] [1] != '_' && board [2] [2] != '_') {
							over = true;
							PrintBoard ();
							System.out.println ("\nDraw...");
						}
						curTurn = 'O';
					}
					else {
						over = true;
						PrintBoard ();
						System.out.println ("\nWrong cell! " + curTurn + " loses!!!");
					}
				}
				else {
					over = true;
					PrintBoard ();
					System.out.println ("\nWrong cell! " + curTurn + " loses!!!");
				}
			}
			else if (curTurn == 'X' && playerTurn == 'O') {
				int x = botInput.nextInt (3);
				int y = botInput.nextInt (3);
				while (board [x] [y] != '_') {
					x = botInput.nextInt (3);
					y = botInput.nextInt (3);
				}
				board [x] [y] = curTurn;
				if (GameOver (x, y)) {
					over = true;
					PrintBoard ();
					System.out.println ("\nCongratulations! " + curTurn + " wins!!!");
				}
				else if (board [0] [0] != '_' && board [0] [1] != '_' && board [0] [2] != '_' && board [1] [0] != '_' && board [1] [1] != '_' && board [1] [2] != '_' && board [2] [0] != '_' && board [2] [1] != '_' && board [2] [2] != '_') {
					over = true;
					PrintBoard ();
					System.out.println ("\nDraw...");
				}
				curTurn = 'O';
			}
			else if (curTurn == 'O' && playerTurn == 'O') {
				PrintBoard ();
				System.out.print ("Enter the column number: ");
				int x = input.nextInt () - 1;
				System.out.print ("Enter the row number: ");
				int y = input.nextInt () - 1;
				if (x <= 2 && x >= 0 && y <= 2 && y >= 0) {
					if (board [x] [y] == '_'){
						board [x] [y] = curTurn;
						if (GameOver (x, y)) {
							over = true;
							PrintBoard ();
							System.out.println ("\nCongratulations! " + curTurn + " wins!!!");
							}
						else if (board [0] [0] != '_' && board [0] [1] != '_' && board [0] [2] != '_' && board [1] [0] != '_' && board [1] [1] != '_' && board [1] [2] != '_' && board [2] [0] != '_' && board [2] [1] != '_' && board [2] [2] != '_') {
							over = true;
							PrintBoard ();
							System.out.println ("\nDraw...");
						}
						curTurn = 'X';
					}
					else {
						over = true;
						PrintBoard ();
						System.out.println ("\nWrong cell! " + curTurn + " loses!!!");
					}
				}
				else {
					over = true;
					PrintBoard ();
					System.out.println ("\nWrong cell! " + curTurn + " loses!!!");
				}
			}
			else if (curTurn == 'O' && playerTurn == 'X') {
				int x = botInput.nextInt (3);
				int y = botInput.nextInt (3);
				while (board [x] [y] != '_') {
					x = botInput.nextInt (3);
					y = botInput.nextInt (3);
				}
				board [x] [y] = curTurn;
				if (GameOver (x, y)) {
					over = true;
					PrintBoard ();
					System.out.println ("\nCongratulations! " + curTurn + " wins!!!");
				}
				else if (board [0] [0] != '_' && board [0] [1] != '_' && board [0] [2] != '_' && board [1] [0] != '_' && board [1] [1] != '_' && board [1] [2] != '_' && board [2] [0] != '_' && board [2] [1] != '_' && board [2] [2] != '_') {
					over = true;
					PrintBoard ();
					System.out.println ("\nDraw...");
				}
				curTurn = 'X';
			}
		}
	}
	public static void PlayMulti (char curTurn) {
		boolean over = false;
		while (!over) {
			PrintBoard ();
			System.out.print ("Enter the column number: ");
			int x = input.nextInt () - 1;
			System.out.print ("Enter the row number: ");
			int y = input.nextInt () - 1;
			if (x <= 2 && x >= 0 && y <= 2 && y >= 0) {
				if (board [x] [y] == '_'){
					board [x] [y] = curTurn;
					if (GameOver (x, y)) {
						over = true;
						PrintBoard ();
						System.out.println ("\nCongratulations! " + curTurn + " wins!!!");
					}
					else if (board [0] [0] != '_' && board [0] [1] != '_' && board [0] [2] != '_' && board [1] [0] != '_' && board [1] [1] != '_' && board [1] [2] != '_' && board [2] [0] != '_' && board [2] [1] != '_' && board [2] [2] != '_') {
						over = true;
						PrintBoard ();
						System.out.println ("\nDraw...");
					}
					else {
						if (curTurn == 'X') {
							curTurn = 'O';
						}
						else {
							curTurn = 'X';
						}
					}
				}
			}
			else {
				over = true;
				PrintBoard ();
				System.out.println ("\nWrong cell! " + curTurn + " loses!!!");
			}
		}
	}
	public static void PrintBoard () {
		System.out.println ("  1 2 3");
		for (int y = 0; y < 3; y ++) {
			System.out.print (y + 1);
			for (int x = 0; x < 3; x ++) {
				System.out.print (" " + board [x] [y]);
			}
			System.out.println ();
		}
	}
	public static boolean GameOver (int x, int y) {
		if (board [0] [y] == board [1] [y] && board [0] [y] == board [2] [y] && board [0] [y] != '_' && board [1] [y] != '_' && board [2] [y] != '_') {
			return true;
		}
		else if (board [x] [0] == board [x] [1] && board [x] [0] == board [x] [2] && board [x] [0] != '_' && board [x] [1] != '_' && board [x] [2] != '_') {
			return true;
		}
		else if (board [0] [0] == board [1] [1] && board [0] [0] == board [2] [2] && board [0] [0] != '_' && board [1] [1] != '_' && board [2] [2] != '_') {
			return true;
		}
		else if (board [2] [0] == board [1] [1] && board [2] [0] == board [0] [2] && board [2] [0] != '_' && board [1] [1] != '_' && board [0] [2] != '_') {
			return true;
		}
		else {
			return false;
		}
	}
}