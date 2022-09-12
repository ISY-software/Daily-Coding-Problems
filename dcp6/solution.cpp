// vim: foldlevel=99
#include <iostream>
#include <stdint.h>


template <class T>
class Node {       
  public:             
    T val;

};

int main(int argc, char *argv[])
{
    int varA = 23;
    int varB = 10;
    int* dirA = &varA;
    int* dirB = &varB;
    uintptr_t xor_ptr = (uintptr_t)dirA ^ (uintptr_t)dirB;

    std::cout << varA << std::endl;
    std::cout << varB << std::endl;
    std::cout << dirA << std::endl;
    std::cout << dirB << std::endl;
    std::cout << (*dirA) << std::endl;
    std::cout << (*dirB) << std::endl;
    std::cout << xor_ptr << std::endl;
    std::cout << ((void *)(xor_ptr ^ (uintptr_t)dirA)) << std::endl;
}
