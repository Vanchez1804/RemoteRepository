// test.cpp
#include "functions.h"
#include <iostream>
#include <cassert>

void TestAdd() {
    assert(Add(2, 3) == 5);  // 2 + 3 должно быть равно 5
    assert(Add(-1, -1) == -2); // -1 + -1 должно быть равно -2
    assert(Add(0, 0) == 0);  // 0 + 0 должно быть равно 0
    std::cout << "TestAdd passed!" << std::endl;
}

void TestSubtract() {
    assert(Subtract(5, 3) == 2);  // 5 - 3 должно быть равно 2
    assert(Subtract(-1, -1) == 0); // -1 - (-1) должно быть равно 0
    assert(Subtract(0, 0) == 0);  // 0 - 0 должно быть равно 0
    std::cout << "TestSubtract passed!" << std::endl;
}

int main() {
    TestAdd();
    TestSubtract();
    std::cout << "All tests passed!" << std::endl;
    return 0;
}

