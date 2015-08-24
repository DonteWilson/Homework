#include <iostream>
using namespace std;

int addition(int a, int b)
{
	std::cout << "Give me 2 numbers" << std::endl;
	std::cin.get();
	int r;
	r = a + b;
	return r;
}

int main()
{
	int z;
	z = addition(10.6,-67.8);
	cout << "The result is " << z;

	system("pause");

	//confused
}