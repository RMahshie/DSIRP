#include <iostream>
#include <cstdlib>
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

int main () {
	int num_values = 100000;
	int upper_bound = 10;
	vector<int> vec = random_vector(num_values, upper_bound);
	vector<int> histogram(upper_bound, 0);

	for (int i = 0; i < num_values; i++) {
    		int index = vec[i];
    		histogram[index]++;
	}
	
	print_vector(histogram);
	
	return 0;
}
