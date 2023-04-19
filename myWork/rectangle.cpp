#include <iostream>
using namespace std;

struct Rectangle {
    point corner;
    double width, height;
};

void print_point(Point p)
{
    cout << "(" << p.x << ", " << p.y << ")" << endl;
}

point  lowerRight(Rectangle& box) {
	
	double x = box.corner.x + box.width;
    	double y = box.corner.y - box.height;
    	point result = {x, y};
    	return result;

}


int main() {


	Rectangle box = {{0.0, 0.0}, 100.0, 200.0};
	point right = lowerRight(box);
	print_point(right);
	return 0;



}
