#include "functions.h"
#include <iostream>
#include <cassert>

void TestAdd() {
    assert(Add(2, 3) == 5);
    std::cout << "TestAdd passed!" << std::endl;
}

void TestSubtract() {
    assert(Subtract(5, 3) == 2);
    std::cout << "TestSubtract passed!" << std::endl;
}

int main() {
    TestAdd();
    TestSubtract();
    std::cout << "All tests passed!" << std::endl;
    return 0;
}



