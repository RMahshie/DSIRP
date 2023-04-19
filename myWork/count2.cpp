#include <iostream>
#include <string>
using namespace std;




void count(string word,char letter) {

        int count = 0;
        int index = 0;

      	while(index < word.length()) {
		

		if( word.find(letter, index) != -1) {
			count ++;
			index = word.find(letter, index) + 1;
		}
		

}
        cout << count << endl;
}

int main() {

        count("Mississippi", 'i');
        return 0;

}
