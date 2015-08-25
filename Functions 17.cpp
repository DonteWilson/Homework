#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	int quit;

	while(quit != -1){

		srand(time(0));

		int username;
		int randomNum;

		cout << "1.Rock"  << endl;
		cout << "2.Paper" << endl;
		cout << "3.Scissors" << endl;

		cin >> username;
		cout << endl;

		randomNum = (rand() % 3) + 1;

		if (username-1)
		{
			return 0;
		}
		if (randomNum == username)
		{
			cout << "Tie!" << username << endl;
		}
		if ((randomNum == 1 && username == 2) ||
			(randomNum == 3 && username == 1) ||
			(randomNum == 2 && username == 3))
		{
			cout << "you win!" << endl;
		}
		else
		{
			cout << "you lose!" << endl;
		}



	}
	return 0;
	
}

