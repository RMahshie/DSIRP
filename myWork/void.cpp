#include <iostream>

void new_line() {
    std::cout << std::endl;
}

int main() {
    std::cout << "Result: " << new_line() + 7 << std::endl;
    return 0;
}
