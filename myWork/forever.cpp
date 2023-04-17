#include <iostream>
using namespace std;

void lool_forever(int n) {
    while (true) {
        cout << "n is now " << n << "." << endl;
        n = n + 1;
    }
}

void recurse_forever(int n) {
    cout << "n is now " << n << "." << endl;
    recurse_forever(n + 1);
}


int main() {
	/*lool forever goes until max int and recurse goes for 262,017 and gave a segmentation fault this is becuase the recursive call is executed enough that the call stack overflows. This is known as stack overflow and calls this infinite recursion error */   
	recurse_forever(1);
	return 0;
}
