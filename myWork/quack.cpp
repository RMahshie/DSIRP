#include <iostream>
#include <string>
using namespace std;


int main() {

	string suffix = "ack";

	char letter = 'J';
	while (letter <= 'Q') {
    		string added;
		added += letter;
		if( letter == 'O' || letter == 'Q') {
			added += 'u';
		}
		cout << added + suffix << endl;
		letter++;
	}
	return 0;
}
