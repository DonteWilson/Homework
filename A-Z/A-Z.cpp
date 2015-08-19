#include <iostream>

int main()
{
	char alp1, alp2, answer, answer1, answer2;
	int sum;

	std::cout << "Enter The First Letter Of Your Choice ";
	std::cin >> alp1;
	std::cout << "Enter The Second Letter Of Your Choice: ";
	std::cin >> alp2;
	sum = (alp1 + alp2) / 2;
	answer = char(sum);
	std::cout << answer << " Lies halfway between the two alphabets." << std::endl;
	system("pause");
	
	
	//I did too much work previously, and unnessary coding. 
	//Started using char correctly.
	
	return 0;

}