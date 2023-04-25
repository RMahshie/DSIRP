#include <iostream>
#include <vector>
using namespace std;

vector<int> random_vector(int n, int upper_bound)
{
    vector<int> vec(n);

    for (int i = 0; i < vec.size(); i++) {
        vec[i] = rand() % upper_bound;
    }

    return vec;
}

void print_vector(const vector<int>& vec)
{
    for (int i = 0; i < vec.size(); i++) {
        cout << vec[i] << " ";
    }
}

int main() {
	int num_values = 10;
	int upper_bound = 10;
	vector<int> vector = random_vector(num_values, upper_bound);
	print_vector(vector);

}
