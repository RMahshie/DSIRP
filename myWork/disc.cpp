#include <iostream>

int add(int a, int b) {
    return a + b;
}

int main() {
    add(3, 4);
    std::cout << "Function call completed" << std::endl;
    return 0;
}
