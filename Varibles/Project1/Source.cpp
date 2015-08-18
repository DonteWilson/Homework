#include <iostream>
int main()
{
	bool Team = 1;
	bool Feeds = 0;
	if  (Team != Feeds)	
{
	std::cout << "Victory" << std::endl;
	std::cin.get();
	return 0;

}
	else
	{
		std::cout << "Defeat" << std::endl;
		std::cin.get();
		return 0;
	}



}