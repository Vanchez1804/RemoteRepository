#include "functions.h"
#include <iostream>

int Add(int a, int b) {
    return a + b;
}

int Subtract(int a, int b) {
    return a - b;
}

int main() {
    std::cout << "Hello, GitHub Actions!" << std::endl;

    // Вы можете вызвать тесты в основном коде, если хотите
    TestAdd();
    TestSubtract();

    return 0;
}




 
