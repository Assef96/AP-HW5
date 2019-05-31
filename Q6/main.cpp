#include <iostream>
#include <math.h>
#include "CGaussSolver.h"
long double func(const long double& x)
{
    long double xN = 0.5 * x + 0.5;
    return pow(xN, 3) * std::cos(pow(xN, 2)) / (1 + xN);
}

int main()
{
    int N;
    std::cin >> N;
    CGaussSolver cgs{func, 0.0L, 1.0L, N};
    cgs.exec();
    std::cout << cgs.getResult() << std::endl;

    return 0;
}