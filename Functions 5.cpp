#include <iostream>
#include <cstdlib>
#include <ctime>



int coinToss(void)
{
	int randomNumber;
	randomNumber = 1 + rand() % 2;
	return randomNumber;
} 
int main()
{
	int howManyTimes = 0;
	int randomNumber = 0;
	std::string headTail = "";

	std::cout << "How many times to toss the coin?";
	std::cin >> howManyTimes;

		srand((time(0)));

	for (int i = 1; 1 <= howManyTimes; i++)
	{
		randomNumber = coinToss();
		if (randomNumber == 1)
			headTail = "head";
		else
		
			headTail = "tail";


			std::cout << "headTail" << std::endl;
		
	}
	return 0;

	system("pause");
}