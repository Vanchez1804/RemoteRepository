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

// Новый тест для функции Square
void TestSquare() {
    assert(Square(2) == 4);  // 2 * 2 должно быть равно 4
    assert(Square(-3) == 9); // -3 * -3 должно быть равно 9
    assert(Square(0) == 0);  // 0 * 0 должно быть равно 0
    std::cout << "TestSquare passed!" << std::endl;
}

int main() {
    TestAdd();
    TestSubtract();
    TestSquare(); // Запуск нового теста
    std::cout << "All tests passed!" << std::endl;
    return 0;
}
