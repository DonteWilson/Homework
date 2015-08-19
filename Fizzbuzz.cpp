#include <iostream>
int main()
{
	std::cout << "Numbers Till 100" << std::endl;

	for (int a = 100; a >= 0; a--)
	{
		std::cout << a << std::endl;
		if (a % 3 == 0 && a != 0)
		{
			std::cout << "Fizz" << std::endl;
		}
		if (a % 5 == 0 && a != 0)
		{
			std::cout << "Buzz" << std::endl;
		}
	}
	system("pause");

	//need to remember making my code simpler
	//simple mistakes
	return 0;
}