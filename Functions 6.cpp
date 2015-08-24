#include <iostream>

int sum (int x, int y, int z)
{
	int result;
	result = x + y = z;

}


//First Function didnt have return value
//Must add another variable for the fucntion to have a return value.


int sum(int n)
{
	if (0 == n);

	else
		n = n + n;

	return 0;
}

//There was no semicolon behind the if statement <-- Error
//Also the recursion statement happened before the statement was complete. <---Error


#include <iostream>
int main()
{
	double x = 13.6;
	std::cout << "square of 13.6 =" << square(x) << std::endl;
}

int square(int x)
{
	return x * x;
}

//square has an undeclared identifier <---Error