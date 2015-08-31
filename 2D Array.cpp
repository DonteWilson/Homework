#include <iostream>
#include <string.h>

const int r = 3;
const int c = 9;
using namespace std;

int main()
{
	char array[r][c] = { { 'D','o','n','t','e' },
						{ 'M','a','r','q','u','i','n','c','y' },
						{ 'W','i','l','s','o','n' } };

	for (int r = 0; r < 3; r++)
	{
		for (int c = 0; c < 9; ++c)
		{
			if ((int)array[r][c] != 0)
			{
				cout << (int)array[r][c] << " ";
			}
		}
		cout << endl;
	}

	system("pause");
	return 0;

}