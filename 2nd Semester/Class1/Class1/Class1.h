#ifndef CLASS1_H
#define CLASS1_H
#include <string>
using namespace std;


template <typename T>
struct Vector3
{
	T x, y, z;

};
class Shape
{
private:
	int sides;
	string tag;
	Vector3<float> Pos;

public:

	void Draw();
	void Move(Vector3<float> Pos);

	Shape();
	~Shape();




};

#endif CLASS1_H
