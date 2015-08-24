#include <iostream>
void PrintInteger(int variable)
{
	std::cout << variable << std::endl;
}
int main()
{
	int the_variable = 1;
	PrintInteger(the_variable);
	{
		PrintInteger(the_variable);
		int the_variable = 2;
		PrintInteger(the_variable);
		{
			PrintInteger(the_variable);
			int the_variable = 3;
			PrintInteger(the_variable);
		}
		PrintInteger(the_variable);	}	PrintInteger(the_variable);	system("pause");}	// The output of this program is 1,1,2,2,3.2.1		