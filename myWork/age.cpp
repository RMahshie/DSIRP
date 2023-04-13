#include <iostream>
using namespace std;

void age(int n) {
	if (n > 16 && n < 65 ) 
   	 {
        	cout << "age is within the normal working age." << endl;
    	}
}

int main() {
	age(45);
	return 0;


}
