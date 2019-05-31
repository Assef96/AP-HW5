#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

void display(const std::vector<int>& vec);
int main()
{
    std::cout << "A:" << std::endl;
    std::vector<int> vec1(100);
    std::iota(vec1.begin(), vec1.end(), 1);
    std::vector<int> vec2(10);
    std::iota(vec2.begin(), vec2.end(), 1);
    display(vec1);
    display(vec2);

    std::cout << "Be:" << std::endl;
    vec2.insert(vec2.end(), vec1.begin(), vec1.end());
    display(vec2);

    std::cout << "Je:" << std::endl;
    std::vector<int> odd_vec(vec1.size());
    auto func{[](const int& a){ return a % 2 == 1; }};
    auto it = std::copy_if(vec1.begin(), vec1.end(), odd_vec.begin(), func);
    odd_vec.erase(it, odd_vec.end());
    display(odd_vec);

    std::cout << "De:" << std::endl;
    std::vector<int> reverse_vec(vec1.rbegin(), vec1.rend());
    display(reverse_vec);
    
    std::cout << "He:" << std::endl;
    std::sort(vec2.begin(), vec2.end());
    display(vec2);
    
    return 0;

}

void display(const std::vector<int>& vec) {
    for(auto iter{vec.begin()}; iter != vec.end(); iter++)
        std::cout << *iter << ' ';
    std::cout << "\n\n";
}