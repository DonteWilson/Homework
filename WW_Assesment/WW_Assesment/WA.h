#ifndef WA_H
#define WA_H
#include <iostream>
#include <string>
using namespace std;
// Gives struct representing player
struct Player
{
	string name;
	bool alive;
	int x_pos = 0;
	int y_pos = 0;
	int dis;

};
// Struct displaying Objects 
struct Object
{
	string name;
	bool Exist;
	int e_x_p;
	int e_y_p;

};
class Robot
{
public:
	Robot(int, int, int);
	void WA();

private:
	int x_pos;
	int y_pos;
	int dis;
};
Robot::Robot(int x, int y, int d)
{
	int Pos_X = x;
	int Pos_Y = y;
	int dis = d;
}

void Robot::WA()
{
	Player Robot;
	Robot.alive = true;
	Robot.x_pos = 0;
	Robot.y_pos = 0;
	Robot.dis = 8;
	Object Pit;
	Pit.Exist = true;
	Pit.e_x_p = 1;
	Pit.e_y_p = 3;

	Object Pit2;
	Pit2.Exist = true;
	Pit2.e_x_p = 3;
	Pit2.e_y_p = 1;

	Object Wumpus;
	Wumpus.Exist = true;
	Wumpus.e_x_p = 2;
	Wumpus.e_y_p = 1;
	Object Gold;
	Gold.Exist = true;
	Gold.e_x_p = 3;
	Gold.e_y_p = 3;

	while (Robot.alive = 1)
	{
	 
	}

	int input;
	cin >> input;

	switch (input)
	{
	case 119:
	{
		cout << "You Head North." << endl;
		Robot.dis = 119;
		break;
	}
	case 115:
	{
		cout << "You Head South." << endl;
		Robot.dis = 115;
		break;
	}
	case 97:
	{
		cout << "You Head West." << endl;
		Robot.dis = 97;
		break;
	}
	case 100:
	{
		cout << "You Head East." << endl;
		Robot.dis = 100;
		break;
	}
	case 113:
	{
		int arrow = 1;

		if (arrow == 1)
		{
			cout << "You shoot the arrow." << endl;
			arrow = (arrow - 1);
			if (Robot.x_pos == 1)
			{
				if (Robot.y_pos == 1)
				{
					cout << "You killed the Wumpus" << endl;
					Wumpus.Exist = false;
				}

			}
			else if (Robot.x_pos == 3)
			{
				if (Robot.y_pos == 0)
				{
					cout << "You killed the Wumpus" << endl;
					Wumpus.Exist = false;
				}

			}
			else if (Robot.x_pos == 2)
			{
				if (Robot.y_pos == 3)
				{

					if (Robot.dis = 8)
					{
						cout << "You killed the Wumpus" << endl;
						Wumpus.Exist = false;
					}
				}

			}
			else
			{
				cout << "Your arrow misses." << endl;
			}
		}
		else
		{
			cout << "You have no more arrows." << endl;
		}

		break;
	}
	default:
	return Robot::WA();
	}

	




	if (Robot.x_pos == 1)
	{
		if (Robot.y_pos == 3)
		{
			cout << "You Died!" << endl;

		}

	}
	if (Robot.x_pos == 2)
	{
		if (Robot.y_pos == 1)
		{
			cout << "You Died!" << endl;

		}

	}

	if (Robot.x_pos == 3)
	{
		if (Robot.y_pos == 1)
		{
			cout << "You Died!" << endl;

		}

	}
}

#endif WA_H
