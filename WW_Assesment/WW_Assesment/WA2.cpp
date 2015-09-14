#include "WA.h"
using namespace std;
// formation of grid
void MakeGrid()
{
	char grid[4][4] = {
		{ '0','1','2','3' },
		{ '0','1','2','3' },
		{ '0','1','2','3' },
		{ '0','1','2','3' } };
	// displays the character within the grid
	char character = '*';
	//position of character.
}

int main() {

	int done = 0;
	char choice;
	
	cout << "Welcome to:" << endl;
	cout << "Wumpus World!" << endl;
	cout << endl;
	cout << "Choose an Option:" << endl;
	cout << "1 - Play Wumpus World" << endl;
	cout << "2 - Help" << endl;
	cout << "3 - Quit" << endl;
	cout <<"" ;
	cin >> choice;

	
	//Makes a switch statment for player choice.
	switch (choice)
	{
	case '1':
		system("cls");
		cout << "Thanks for playing Wumpus World\n" << endl;
		
	
		break;
	// A Players Guide to the game and gives tem basic understanding.
	case '2':
		cout <<" Controls "<< endl;
		cout <<" ------------------ - "<< endl;
		cout <<"W - Moves the Robot Up "<< endl;
		cout <<"A - Moves the Robot Left "<< endl;
		cout <<"S - Moves the Robot Down "<< endl;
		cout <<"D - Moves the Robot Right "<< endl;
		cout << "Q - Shoots the Arrow" << endl;
		cout << "" << endl;
		cout << "Instructions On How To Play" << endl;
		cout << "--------------------------" << endl;
		cout << "1. The Robot starts in a 2D grid, which gives the player 16 cells to move around and explore the area." << endl;
		cout << "2. By using the controls listed above, navigate your character around the grid to find Gold and the Wumpus itself." << endl;
		cout << "3. Avoid traveling farther than the grids demensions or it will result in a death and a restart of the game."<< endl;
		cout << "4. Once you find the gold, make your way back to the start without running into the Wumpus." << endl;
		system("pause");
		return  (choice);
		{
		}
		cout << "" << endl;
		break;
		system("cls");
	case '3':
		return 0;
		break;
	default:
		system("cls");
		cout << "Invalid Choice" << endl;
		return main();
		break;
	}
	//Prints Grid 
	MakeGrid();
	int begin = 1;
	switch(begin)
		case 1:
	{
		{Robot Robot(0, 0, 119);
		Robot.WA();
		}
	}
	//Prompts the user the option to retry
	int retry;
	cout << "Press r to reset or etc to quit" << endl;
	cin >> retry;
	switch (retry)
	{
	//ASCII code for r
	case 114:
	{
		system("cls");
		return main();
	}
	default:
	return 0;
	}
	
	cout << "\nWhere would you like to move?\n" << endl;
	cin.get();


	


	
	system("pause");
	return 0;

}