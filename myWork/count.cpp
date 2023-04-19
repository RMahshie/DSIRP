#include <iostream>
#include <string>
using namespace std;




void count(string word,char letter) {
	
	int count = 0;
	int index = 0;

	while (index < word.length()) {
    	if (word[index] == letter) {
        	count = count + 1;
    	}
    	index = index + 1;
	}	
	cout << count << endl;
}

int main() {

	count("Mississippi", 'i');
	return 0;

}
