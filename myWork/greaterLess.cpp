#include <iostream>
using namespace std;

void greaterLess(int a, int b) {
    if (a > b) {
        cout << "a more than b" << endl;
    } else if (b > a) {
        cout << "b more than a" << endl;
    } else {
        cout << "they are equal" << endl;
    }
}

int main() {
  greaterLess(4, 5); // call the function
  return 0;
}

