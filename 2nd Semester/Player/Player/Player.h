#ifndef PLAYER_H
#define PLAYER_H
#include <iostream>
#include <string>
using namespace std;
template <typename T>
struct Vector
{
	T x, y, z;
};

class Actor
{
public:
	string name;
	int health;
	int damage;
	Vector<float>Pos;
	
    virtual void Update();
	virtual void move();
	void attack();
};

void Actor::Update()
{
	Actor::Update();
	move();
}

void Actor::move()
{

	printf("Default Move");

}

void Player::Update()
{
	move();
}

void Player::move()
{
	printf("Default Move");
}


class Player : public Actor
{
public:
	int inventory;


	void input();
	virtual void move();
	virtual void Update();


};

void Player::move()
{
	printf("Player Move");
}


class Enemy : public Actor
{
public:
	int LootTable[5];

	void AI();

};


#endif PLAYER_H