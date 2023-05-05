#include "random.h"
#include <random>
#include <ctime>

int random_between(int l, int h)
{
    if (l < 0 || h < 0 || h <= l) {
        return -1;
    }

    if (l == h) {
        return l;
    }

    if (l > h) {
        std::swap(l, h);
    }

    static std::mt19937 rng(std::time(nullptr));
    std::uniform_int_distribution<int> dist(l, h);

    return dist(rng);
}
