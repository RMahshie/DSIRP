#include <iostream>
#include <string>
using namespace std;

string stringToUpper(string word) {
	string result;
	for(int x = 0; x < word.length(); x++) {
		result += toupper(word[x]);
	}
	return result;
}

string stringToLower(string word) {
        string result;
        for(int x = 0; x < word.length(); x++) {
                result += tolower(word[x]);
        }
        return result;
}

int main() {
	string word;
	cout << "Enter a word: ";
	cin >> word;
	cout << stringToUpper(word) << endl;
	cout << stringToLower(word) << endl;
	return 0;
}
