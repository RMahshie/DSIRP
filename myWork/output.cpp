#include <iostream>

int main() {
  int hour, minute;
  char colon;

  hour = 11;
  minute = 59;
  colon = ':';

  std::cout << "The current time is " << hour << colon << minute << std::endl;
}
