#include <iostream>
using namespace std;

void print_twice(char phil) {
    cout << phil << phil << endl;
}

int main() {
    char argument = "boobookeys";
    print_twice(argument);
    return 0;
}
