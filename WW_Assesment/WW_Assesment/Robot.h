#ifndef ROBOT_H
#define ROBOT_H

#include<iostream>
#include<string>
#include"WA.h"

using namespace std;


class Robot
{
public:
	Robot();
	~Robot();
	
	int posx();
	int posy();
	void Pits();
	void PlayerMove();
	void headshot();
	void Gold();
	void Wumpus();

private:
	int x;
	int y;
};


//Ends The Inclusion Of This Class
#endif ROBOT_H