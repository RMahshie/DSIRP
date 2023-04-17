#include <iostream>
using namespace std;
#include <math.h>

int main(){
	double x = 1.0;
	while (x < 66536) {
        	cout << x << "\t" << log(x) / log(2.0) << endl;
    		x = x * 2.0;
	}
	return 0;


}
