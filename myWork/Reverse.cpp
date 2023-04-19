#include <iostream>
#include <string>
using namespace std;

void reverse(string s) {
	string newWord;
	for (int i = s.length()-1; i >=0; i--) {
		newWord += s[i];

}
	cout << newWord;
}

int main() {

	reverse("cow" );
	return 0;

}
